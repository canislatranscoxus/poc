import json

# Construct the request body.
task = {
        'app_engine_http_request': {  # Specify the type of request.
            'http_method': 'tasks_v2.HttpMethod.POST',
            'relative_uri': '/example_task_handler'
        }
}

print( json.dumps( task, indent = 4 ) )


task["http_request"] = {
    "headers" : {"Content-type": "application/json"}
}
 
print( json.dumps( task, indent = 4 ) )