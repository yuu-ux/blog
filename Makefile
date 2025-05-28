.PHONY: all git_pull restart_app restart_admin reload_nginx

all: git_pull restart_app restart_admin reload_nginx

git_pull:
	ssh -i "$$HOME/.ssh/blog_app.pem" -t admin@ec2-44-240-253-182.us-west-2.compute.amazonaws.com "cd /home/blog && sudo git pull origin main"

restart_app:
	ssh -i "$$HOME/.ssh/blog_app.pem" admin@ec2-44-240-253-182.us-west-2.compute.amazonaws.com sudo systemctl restart blog-app

restart_admin:
	ssh -i "$$HOME/.ssh/blog_app.pem" admin@ec2-44-240-253-182.us-west-2.compute.amazonaws.com sudo systemctl restart blog-admin

reload_nginx:
	ssh -i "$$HOME/.ssh/blog_app.pem" admin@ec2-44-240-253-182.us-west-2.compute.amazonaws.com sudo systemctl reload nginx

