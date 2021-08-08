import os
import time

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

# Stop Redis service and delete the cluster configuration and DB on each node
for node in nodes:
    myCmd = "ssh ubuntu@" + node + " 'sudo service redis_6378 status'"
    os.system(myCmd)

exit(0)
