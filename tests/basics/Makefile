BASEDIR=$(PWD)/tests/basics/
PYTHON_INTERPRETER=python3
PYTHONPATH=../../

run_all: clock camera game_object
	
camera:
	@-$(PYTHON_INTERPRETER) $(BASEDIR)/camera.py;

clock:
	@-make -C game_clock

game_object:
	@-$(PYTHON_INTERPRETER) $(BASEDIR)/game_object.py;