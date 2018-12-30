install_deps:
	pip3 install -r requirements.py

submit:
	sbatch job.sh

run-local:
	python3 run.py