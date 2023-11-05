setup:
	pip install -r requirements.txt

up:
	python -m uvicorn main:app --reload

test-all:
	curl -v -X GET http://localhost:8000/midTermResults

test-eng:
	curl -v -X GET http://localhost:8000/midTermResults/english

test-math:
	curl -v -X GET http://localhost:8000/midTermResults/math

test-japanese:
	curl -v -X GET http://localhost:8000/midTermResults/japanese

test-society:
	curl -v -X GET http://localhost:8000/midTermResults/society

test-post:
	curl -v -X POST -H "Content-Type: application/json" -d @test-society.json http://localhost:8000/midTermResults

test-post-error:
	curl -v -X POST -H "Content-Type: application/json" -d @test-invalid.json http://localhost:8000/midTermResults