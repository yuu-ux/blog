import os

bind = 'app:' + str(os.getenv('PORT', 8001))
workers = 1
reload = True
accesslog = '-'
errorlog = '-'
