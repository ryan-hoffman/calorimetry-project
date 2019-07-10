default:
	@echo "targets (choose one): venv.install.ryan, venv.start.ryan, venv.install.paul, venv.start.paul, pip.install, pip.versions"

venv.install.paul:
	virtualenv --python=/Users/paul/anaconda/bin/python3 ./py363

venv.start.paul:
	@echo "execute this command in your shell: source ./py363/bin/activate"

# ryan will have his own path and preferred version of python 3
# modify these next two make targets appropriately
venv.install.ryan:
	virtualenv --python=/Users/paul/anaconda/bin/python3 ./py363

venv.start.ryan:
	@echo "execute this command (suitably modified) in your shell: source ./py363/bin/activate"

pip.install:
	pip install -r requirements.txt

pip.versions:
	pip list | egrep -ie '(dash)|(flask)'



