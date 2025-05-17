import os

bind = 'admin:' + str(os.getenv('PORT', 8002))
workers = 1
reload = True
accesslog = '-'
errorlog = '-'
