BASEDIR=$(PWD)/tests/basics/
PYTHON_INTERPRETER=python3
PYTHONPATH=../../
.PHONY: game_clock camera game_object

all: game_clock camera game_object
	

camera:
	@-$(PYTHON_INTERPRETER) $(BASEDIR)/camera.py;

game_clock:
	@-make -C $(BASEDIR)/game_clock

game_object:
	@-$(PYTHON_INTERPRETER) $(BASEDIR)/game_object.py;