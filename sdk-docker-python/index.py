import docker


client = docker.from_env()


# client.containers.run("hello-world", detach=True)

# client.containers.run("nginx:latest", detach=True, ports={"80/tcp": 8081})

list_container = client.containers.list(all=True)

for container in list_container:
    print(container.name, container.status, container.image.tags, container.ports)