import qarnot

conn = qarnot.connection.Connection(client_token = 'd9c8824f6320ce2142d5f5dd07031e016eabcd16433572a6120b058372f1eea7')
task = conn.create_task("hello polytechnique", "docker-batch", 3)

task.constants['DOCKER_REPO'] = 'ubuntu'
task.constants['DOCKER_TAG'] = '20.04'
task.constants['DOCKER_CMD'] = "echo hello polytechnique from instance number ${INSTANCE_ID}"

task.run()

# print(task.stdout())
