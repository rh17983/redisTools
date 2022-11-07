import os

ssh_params = "-i /home/usi/.ssh/controller-root -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

for node in nodes:
    myCmd = "ssh " + ssh_params + " ubuntu@" + node + " 'redis-cli --cluster check " + node + ":6378'"
    os.system(myCmd)

    break
