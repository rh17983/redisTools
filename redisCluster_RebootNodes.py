import os

fileName = "redisCluster_NodesToReboot.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

for node in nodes:
    myCmd = "ssh ubuntu@" + node + " 'sudo reboot'"
    os.system(myCmd)
