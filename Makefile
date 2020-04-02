clean-pycache:
	find . | grep -E "(__pycache__$)" | xargs rm -rfv;