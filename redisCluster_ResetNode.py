import os

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

# Stop Redis service and delete the cluster configuration and DB on each node
for node in nodes:
    # Reset
    myCmd = "ssh ubuntu@" + node + " 'redis-cli -h " + node + " -p 6378 -c cluster reset'"
    print(myCmd)
    os.system(myCmd)

exit(0)
