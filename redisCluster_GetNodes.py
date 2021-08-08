import os

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

for node in nodes:
    myCmd = "ssh ubuntu@" + node + " 'redis-cli -h " + node + " -p 6378 cluster nodes'"
    os.system(myCmd)

    break
