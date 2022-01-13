from tabulate import tabulate
import docker


client = docker.from_env()
containers = client.containers.list()

info =  {
  'Status': ['running'], 
  'Running': ['True'], 
  'Paused': ['False'], 
  'Restarting': ['False'], 
  'OOMKilled': ['False'], 
  'Dead': ['False'], 
  'Pid': ['1402'], 
  'ExitCode': ['0'], 
  'Error': [''], 
  'StartedAt': ['2022-01-13T02:16:13.8461167Z'], 
  'FinishedAt': ['2022-01-12T10:56:44.4811929Z']
}
# print(tabulate(container.attrs["State"], headers='keys', tablefmt='fancy_grid', showindex=True))

test = {
  'Status': 'running', 
  'Running': True, 
  'Paused': False, 
  'Restarting': False, 
  'OOMKilled': False, 
  'Dead': False, 
  'Pid': 1402, 
  'ExitCode': 0, 
  'Error': '', 
  'StartedAt': '2022-01-13T02:16:13.8461167Z', 
  'FinishedAt': '2022-01-12T10:56:44.4811929Z'
}

def covert_to_table(dict):
  return 1

def format_dictionary(containers: list):

  if len(containers) == 0:
    print("There are no containers running. Please start the container in docker.")
    return

  for container in containers:
    print(container.attrs)
    print("======================================================================================================", end='\n')


format_dictionary(containers=containers)

# print(tabulate(info, headers='keys', tablefmt='fancy_grid'))
