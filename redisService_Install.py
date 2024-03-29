import threading
import os

ssh_params = "-i /home/usi/.ssh/controller-root -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

fileNameNodes = "redisService_nodes_to_install.txt"
nodes = [line.rstrip('\n') for line in open(fileNameNodes)]

fileNameInstallationSource = "redis_installation.sh"
fileNameInstallationTarget = "/home/ubuntu/redis_installation.sh"

fileNameInstallationSource_2 = "redis-5.0.5.tar.gz"
fileNameInstallationTarget_2 = "/home/ubuntu/redis-5.0.5.tar.gz"


class myThread(threading.Thread):

    def __init__(self, threadID, name, counter, node):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.node = node

    def run(self):
        print(self.name, ": Started.")

        # time.sleep(3)

        myCmd = "scp " + ssh_params + " " + fileNameInstallationSource + " ubuntu@" + self.node + ":" + fileNameInstallationTarget
        os.system(myCmd)

        myCmd = "scp " + ssh_params + " " + fileNameInstallationSource_2 + " ubuntu@" + self.node + ":" + fileNameInstallationTarget_2
        os.system(myCmd)

        myCmd = "ssh " + ssh_params + " ubuntu@" + self.node + " 'sudo chown -R $USER:$USER " + fileNameInstallationTarget + "'"
        os.system(myCmd)

        myCmd = "ssh " + ssh_params + " ubuntu@" + self.node + " 'chmod +x " + fileNameInstallationTarget + "'"
        os.system(myCmd)

        myCmd = "ssh " + ssh_params + " ubuntu@" + self.node + " 'sudo " + fileNameInstallationTarget + "'"
        os.system(myCmd)

        print(self.name, ": Exit.")


threads = []
i = 0
for node in nodes:
    threads.append(myThread("T" + str(i), "T" + str(i), i, node))
    i += 1

for t in threads:
    t.start()

for t in threads:
    t.join()

exit(0)
