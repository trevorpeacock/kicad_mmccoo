default: venv

VENV_PATH = venv

venv:
	virtualenv --python /usr/bin/python3 $(VENV_PATH)
	bash -c ". $(VENV_PATH)/bin/activate && pip install dxfgrabber numpy scipy shapely"

clean:
	rm -dfr $(VENV_PATH)
