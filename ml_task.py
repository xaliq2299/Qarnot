import qarnot

conn = qarnot.connection.Connection(client_token = 'd9c8824f6320ce2142d5f5dd07031e016eabcd16433572a6120b058372f1eea7')
task = conn.create_task("label cats and dogs", "docker-batch", 40)

task.constants['DOCKER_REPO'] = 'tensorflow/tensorflow'
task.constants['DOCKER_TAG'] = '1.12.0'
task.constants['DOCKER_CMD'] = "bash /job/label.sh /job/${INSTANCE_ID}.jpg"

task.resources = [ conn.retrieve_bucket('scripts-polytechnique'),
conn.retrieve_bucket('dogscats-small-polytechnique'),
conn.retrieve_bucket('model-polytechnique')]
task.results = conn.create_bucket('sorted-polytechnique')

task.submit()
