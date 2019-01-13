install_deps:
	pip3 install -r requirements.txt

submit:
	sbatch job.sh

submit-test:
	sbatch test_job.sh

run-local:
	python3 run.py

test-local:
	python3 demo.py