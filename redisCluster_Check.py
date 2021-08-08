import os

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

for node in nodes:
    myCmd = "ssh ubuntu@" + node + " 'redis-cli --cluster check " + node + ":6378'"
    os.system(myCmd)

    break
