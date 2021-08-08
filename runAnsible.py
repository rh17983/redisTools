import os

# Start metricbeats agents on the cluster nodes
os.chdir('../ansible-beat/')
print("Working directory changed to: " + str(os.getcwd()))

myCmd = "ansible-playbook playbook.yml -i hosts2 --tags 'start'"
os.system(myCmd)