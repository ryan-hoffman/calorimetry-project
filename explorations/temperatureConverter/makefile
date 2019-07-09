default:
	@echo "targets (choose one): venv.install, venv.start, pip.install, pip.versions"

venv.intall:
	virtualenv --python=/Users/paul/anaconda/bin/python3 ./py363

venv.start:
	source py363/bin/activate

pip.install:
	pip install -r requirements.txt

pip.versions:
	pip list | egrep -ie '(dash)|(flask)'



