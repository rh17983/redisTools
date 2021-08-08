import os

fileName = "redisCluster_Nodes.txt"
nodes = [line.rstrip('\n') for line in open(fileName)]

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
myCmd = "ansible-playbook ~/ansible-beat/playbook.yml -i hosts2 --tags 'start'"
os.system(myCmd)

exit(0)
