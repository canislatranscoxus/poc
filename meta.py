import json

s = " {
'wsgi.errors': <gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x3e8a06d68ac0>, 
'wsgi.version': (1, 0), 
'wsgi.multithread': True, 
'wsgi.multiprocess': True, 
'wsgi.run_once': False, 
'wsgi.file_wrapper': <class 'gunicorn.http.wsgi.FileWrapper'>, 
'SERVER_SOFTWARE': 'gunicorn/19.9.0', 
'wsgi.input': <gunicorn.http.body.Body object at 0x3e8a06d68af0>, 
'gunicorn.socket': <socket.socket fd=10, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8081), raddr=('127.0.0.1', 44387)>, 

'REQUEST_METHOD': 'POST', 
'QUERY_STRING': '', 
'RAW_URI': '/handler_animal/', 
'SERVER_PROTOCOL': 'HTTP/1.1', 
'HTTP_HOST': 'basmatiyes.ue.r.appspot.com', 
'HTTP_X_FORWARDED_FOR': '0.1.0.2, 169.254.1.1', 
'HTTP_X_FORWARDED_PROTO': 'http', 
'HTTP_FORWARDED': 'for="0.1.0.2";proto=http', 
'CONTENT_LENGTH': '44', 
'HTTP_USER_AGENT': 'AppEngine-Google; (+http://code.google.com/appengine)', 
'CONTENT_TYPE': 'application/octet-stream', 

'HTTP_X_APPENGINE_QUEUENAME': 'qshop', 
'HTTP_X_APPENGINE_TASKNAME': '7810216398822569047', 
'HTTP_X_APPENGINE_TASKRETRYCOUNT': '0', 
'HTTP_X_APPENGINE_TASKEXECUTIONCOUNT': '0', 

'HTTP_X_APPENGINE_TASKETA': '1613009612.074631', 
'HTTP_X_APPENGINE_COUNTRY': 'ZZ', 

'HTTP_X_CLOUD_TRACE_CONTEXT': '14f70876a01f6aa532f126d453bffd05/5986830863264743622;o=1', 
'HTTP_TRACEPARENT': '00-14f70876a01f6aa532f126d453bffd05-53157ef3573d80c6-01', 
'HTTP_X_APPENGINE_TIMEOUT_MS': '609999', 
'HTTP_X_APPENGINE_HTTPS': 'off', 
'HTTP_X_APPENGINE_USER_IP': '0.1.0.2', 
'HTTP_X_GOOGLE_INTERNAL_SKIPADMINCHECK': 'true', 
'HTTP_X_APPENGINE_REQUEST_LOG_ID': '602492cc00ff0143aff470b19d0001707e6261736d6174697965730001323032313032313174303231313530000100', 
'HTTP_X_APPENGINE_DEFAULT_VERSION_HOSTNAME': 'basmatiyes.ue.r.appspot.com', 
'wsgi.url_scheme': 'http', 
'REMOTE_ADDR': '127.0.0.1', 
'REMOTE_PORT': '44387', 
'SERVER_NAME': '0.0.0.0', 
'SERVER_PORT': '8081', 
'PATH_INFO': '/handler_animal/', 
'SCRIPT_NAME': ''} "


j = json.loads( s )

print( json.dumps( j, indent= 4 ) )
