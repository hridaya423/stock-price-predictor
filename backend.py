import mindsdb_sdk

# Connect to MindsDB server running on localhost
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

project = server.get_project()

Microsoft = project.models.get('microsoftpredictor')
Amazon = project.models.get('amazonpredictor')
Apple = project.models.get('applepredictor')
Tesla = project.models.get('teslapredictor')