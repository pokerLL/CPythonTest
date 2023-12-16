# pull push 

# Path: Makefile

pull:
	git pull origin master

push:
	git add .
	git commit -m "update"
	git push origin master