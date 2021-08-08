import os
import time

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

# Stop Redis service and delete the cluster configuration and DB on each node
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


time.sleep(30)

# Start Redis on each node with new configuration
for node in nodes:

    # Copy the service configuration to each node
    myCmd = 'scp 6378.conf ubuntu@' + node + ':~/6378.conf'
    os.system(myCmd)

    myCmd = "ssh ubuntu@" + node + " 'sudo mv -f ~/6378.conf /etc/redis/6378.conf' "
    os.system(myCmd)

    # Set the owner of the service configuration file
    myCmd = "ssh ubuntu@" + node + " 'sudo chown -R $USER:$USER /etc/redis/6378.conf' "
    os.system(myCmd)

    # Start the service on the each node
    myCmd = "ssh ubuntu@" + node + " 'sudo service redis_6378 start' "
    os.system(myCmd)

time.sleep(60)

# Reset Cluster
for node in nodes:
    # Reset
    myCmd = "ssh ubuntu@" + node + " 'redis-cli -h " + node + " -p 6378 -c cluster reset'"
    print(myCmd)
    os.system(myCmd)

# Build the Cluster
nodes_with_ports = ""
i = 0
for node in nodes:
    if i != 0:
        nodes_with_ports = nodes_with_ports + " "

    nodes_with_ports = nodes_with_ports + node + ":6378"
    i = i + 1

myCmd = "ssh ubuntu@" + nodes[0] + " 'redis-cli --cluster create " + nodes_with_ports + " --cluster-replicas 1'"
os.system(myCmd)

# Start metricbeats agents on the cluster nodes
os.chdir('../ansible-beat/')
print("Working directory changed to: " + str(os.getcwd()))

myCmd = "ansible-playbook playbook.yml -i hosts2 --tags 'start'"
os.system(myCmd)

exit(0)
