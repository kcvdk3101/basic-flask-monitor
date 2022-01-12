import docker

client = docker.from_env()

container = client.containers.get('13e7ad937f')
print("======================================================================================================", end='\n')
print(container.attrs["State"], end='\n')
print("======================================================================================================", end='\n')
