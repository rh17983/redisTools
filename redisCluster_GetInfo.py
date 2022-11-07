import os

ssh_params = "-i /home/usi/.ssh/controller-root -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

for node in nodes:
    myCmd = "ssh " + ssh_params + " ubuntu@" + node + " 'redis-cli -h " + node + " -p 6378 cluster info'"
    os.system(myCmd)

    break
