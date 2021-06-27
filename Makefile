export PYTHONPATH=./:$PYTHONPATH

testSTAR:
	python3 -B ./tests/test_stars.py
