BASEDIR=$(PWD)/tests/basics/
PYTHON_INTERPRETER=python3
PYPATH=../../
.PHONY: game_clock camera game_object

all: game_clock camera game_object
	

camera:
	@-PYTHONPATH=$(PYPATH) $(PYTHON_INTERPRETER) $(BASEDIR)/camera.py;

game_clock:
	@-make -C $(BASEDIR)/game_clock

game_object:
	@-PYTHONPATH=$(PYPATH) $(PYTHON_INTERPRETER) $(BASEDIR)/game_object.py;