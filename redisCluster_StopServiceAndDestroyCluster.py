import os

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

for node in nodes:
    myCmd = "ssh ubuntu@" + node + " 'sudo service redis_6378 stop'"
    os.system(myCmd)

    myCmd = "ssh ubuntu@" + node + " 'sudo rm /var/run/redis_6378.pid -f'"
    os.system(myCmd)

    myCmd = "ssh ubuntu@" + node + " 'sudo rm -f /var/lib/redis/6378/dump.rdb'"
    os.system(myCmd)
    
    myCmd = "ssh ubuntu@" + node + " 'sudo rm -f /var/lib/redis/6378/nodes-6378.conf'"
    os.system(myCmd)

    myCmd = "ssh ubuntu@" + node + " 'sudo rm -f /etc/redis/6378.conf'"
    os.system(myCmd)

exit(0)
