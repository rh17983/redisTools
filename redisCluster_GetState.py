import subprocess
import time
import logging

state_check_interval = 60
fileName = "redisCluster_Nodes.txt"

loggingFormat = '%(asctime)s %(levelname)-4s: %(message)s'
logging.basicConfig(filename='redis_cluster_states.log', filemode='a', format=loggingFormat, level=logging.INFO, datefmt='%y.%m.%d.%H.%M')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter(loggingFormat))
logging.getLogger('').addHandler(console)

f = open(fileName, 'r')
node = f.readline().rstrip('\n')
f.close()

myCmd = "ssh ubuntu@" + node + " 'redis-cli -h " + node + " -p 6378 cluster info | grep \"cluster_state:\"'"

while True:
    returned_output = str(subprocess.check_output(myCmd, shell=True))

    if returned_output.find("cluster_state:ok") != -1:
        returned_output = "Live"
    else:
        returned_output = "Fail"

    logging.info(returned_output)
    time.sleep(state_check_interval)
