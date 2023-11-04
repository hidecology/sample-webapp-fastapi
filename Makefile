setup:
	pip install -r requirements.txt

up:
	python -m uvicorn main:app --reload