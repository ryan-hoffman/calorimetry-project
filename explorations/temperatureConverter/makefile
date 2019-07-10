default:
	@echo "targets (choose one): venv.install, venv.start, pip.install, pip.versions"

venv.intall.paul:
	virtualenv --python=/Users/paul/anaconda/bin/python3 ./py363

venv.start.paul:
	source py363/bin/activate

# ryan will have his own path and preferred version of python 3
# modify these next two make targets appropriately
venv.intall.ryan:
	virtualenv --python=/Users/paul/anaconda/bin/python3 ./py363

venv.start.ryan:
	source py363/bin/activate

pip.install:
	pip install -r requirements.txt

pip.versions:
	pip list | egrep -ie '(dash)|(flask)'



