export PYTHONPATH=./:$PYTHONPATH

AUTHTOKEN = 

testSTAR:
	python3 -B ./tests/test_stars.py -t $(AUTHTOKEN)
