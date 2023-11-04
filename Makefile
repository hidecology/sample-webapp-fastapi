setup:
	pip install -r requirements.txt

up:
	python -m uvicorn main:app --reload

test:
	curl -v -X GET http://localhost:8000/