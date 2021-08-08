# Redis tools

##### Case 0 - nitial installation:
1. redisService_Install.py
2. redisCluster_StopServiceAndDestroyCluster.py
3. redisCluster_StartServiceAndBuildCluster.py

##### Case 1 - Install the Redis service on the nodes and build the Cluster from scratch:
1. redisService_Install.py : Installs and starts the Redis service on each node specified in redisService_nodes_to_install.txt file. The script uses the redis_installation.sh script.
2. redisCluster_Build.py : Builds the Cluster from the nodes (redisCluster_Nodes.txt) with active Redis service.


##### Case 2 - Rebuild the Cluster:
1. redisCluster_RebootNodes.py : Reboot of the nodes specified in redisCluster_Nodes.txt file. OPTIONAL.
2. redisCluster_Rebuild.py : combines the functionality of the StopServiceAndDestroyCluster and StartServiceAndBuildCluster scripts:
    * Stops Redis service and deletes the cluster configuration and DB on each node (redisCluster_Nodes.txt)
    * Start Redis on each node with new configuration (redisCluster_Nodes.txt)
    * Builds the new cluster (redisCluster_Nodes.txt)


##### Case 3 - Stop Redis on the nodes, Destroy Cluster, Start Redis on the nodes with new configuration, Build Cluster:
1. redisCluster_StopServiceAndDestroyCluster.py : Stops Redis service on the cluster nodes (redisCluster_Nodes.txt), deletes configuration and DB of the Cluster.
2. redisCluster_StartServiceAndBuildCluster.py: Starts Redis service on the nodes (redisCluster_Nodes.txt) and builds the Cluster.

##### Trubleshooting
1. Message: [ERR] Node 192.168.200.134:6378 is not empty. Either the node already knows other nodes (check with CLUSTER NODES) or contains some key in database 0.
Solution: redis-cli -h 192.168.200.134 -p 6378 -c cluster reset

##### Helpers:
1. redisCluster_Check.py : returns status of the Cluster (uses redisCluster_Nodes.txt)
2. redisCluster_GetInfo.py : returns info of the Cluster (uses redisCluster_Nodes.txt)
3. redisCluster_GetNodes.py : returns nodes of the Cluster (uses redisCluster_Nodes.txt)

# Memtier Benchmark:
1. memtier_benchmark_Install.py : Installs the Memtier Benchmark on the nodes indicated in the memtier_benchmark_nodes_to_install.txt file.