import threading
import os

fileNameNodes = "memtier_benchmark_nodes_to_install.txt"
nodes = [line.rstrip('\n') for line in open(fileNameNodes)]

fileNameInstallationSource = "memtier_benchmark_installation.sh"
fileNameInstallationTarget = "/home/ubuntu/memtier_benchmark_installation.sh"


class myThread(threading.Thread):

    def __init__(self, arg_threadID, arg_name, arg_counter, arg_node):
        threading.Thread.__init__(self)

        self.threadID = arg_threadID
        self.name = arg_name
        self.counter = arg_counter
        self.node = arg_node

    def run(self):
        print(self.name, ": Staring")

        myCmd = 'scp ' + fileNameInstallationSource + ' ubuntu@' + self.node + ':' + fileNameInstallationTarget
        os.system(myCmd)

        myCmd = "ssh ubuntu@" + self.node + " 'sudo chown -R $USER:$USER " + fileNameInstallationTarget + "'"
        os.system(myCmd)

        myCmd = "ssh ubuntu@" + self.node + " 'chmod +x " + fileNameInstallationTarget + "'"
        os.system(myCmd)

        myCmd = "ssh ubuntu@" + self.node + " 'sudo " + fileNameInstallationTarget + "'"
        os.system(myCmd)

        print(self.name, ": Exiting")


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
