import docker


client = docker.from_env()


# client.containers.run("hello-world", detach=True)

# client.containers.run("nginx:latest", detach=True, ports={"80/tcp": 8081})

#list_container = client.containers.list(all=True)

#for container in list_container:
#    print(container.name, container.id, container.status, container.image.tags, container.ports)

container = client.containers.get("61c1807520d2f430f8c5e040a3bffd2f7a18d6fc34df32a848a8144219620c55")

container.remove(force=True)