setup:
	pip install -r requirements.txt

up:
	python -m uvicorn main:app --reload

test:
	curl -v -X POST -H "Content-Type: application/json" -d @test.json  http://localhost:8000/study