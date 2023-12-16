pull:
	git pull

push:
	git add .
	git commit -m "update"
	git push 

rp:
# mk rp reps=100 command='python PyTests/int_safety2.py'
	repetitions=$(reps) && \
    for i in $$(seq 1 $$repetitions); do \
        echo "Executing command $$i time(s):"; \
        $(command); \
        echo "------------------------------------"; \
    done