import os
import time

ssh_params = "-i /home/usi/.ssh/controller-root -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

# Start Redis on each node
for node in nodes:
    # Copy the service configuration to each node
    myCmd = 'scp ' + ssh_params + ' 6378.conf ubuntu@' + node + ':~/6378.conf'
    os.system(myCmd)

    myCmd = "ssh " + ssh_params + " ubuntu@" + node + " 'sudo mv -f ~/6378.conf /etc/redis/6378.conf' "
    os.system(myCmd)

    # Set the owner of the service configuration file
    myCmd = "ssh " + ssh_params + " ubuntu@" + node + " 'sudo chown -R $USER:$USER /etc/redis/6378.conf'"
    os.system(myCmd)

    # Start the service on the each node
    myCmd = "ssh " + ssh_params + " ubuntu@" + node + " 'sudo service redis_6378 start'"
    os.system(myCmd)

time.sleep(30)

# Assemble the cluster
nodes_with_ports = ""
i = 0
for node in nodes:
    if i != 0:
        nodes_with_ports = nodes_with_ports + " "

    nodes_with_ports = nodes_with_ports + node + ":6378"
    i = i + 1

myCmd = "ssh " + ssh_params + " ubuntu@" + nodes[0] + " 'redis-cli --cluster create " + nodes_with_ports + " --cluster-replicas 1'"
os.system(myCmd)

exit(0)
