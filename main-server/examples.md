curl -X POST http://localhost:5001/register \
    -H "Content-Type: application/json" \
    -d '{
        "username": "newuser1",
        "password": "password123",
        "first_name": "John",
        "last_name": "Green",
        "date_of_birth": "1990-01-01",
        "email": "johngreen@example.com",
        "phone_number": "1234567890"
    }'


curl -X POST http://localhost:5001/login \
    -H "Content-Type: application/json" \
    -d '{
        "username": "newuser1",
        "password": "password123"
    }'


curl -X PUT http://localhost:5001/update \
-H "Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMzI3NjkxMiwianRpIjoiMTQ0ZDBlNzEtZWFkZC00M2VlLWJkODctMDU2YWVjZWVmN2QxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5ld3VzZXIxIiwibmJmIjoxNzEzMjc2OTEyLCJjc3JmIjoiZWJmMjRmZTktNzZhNy00NTUwLWIwZDItMGNlNmQ2YmU1M2FhIiwiZXhwIjoxNzEzMjgwNTEyfQ.8zQhnWVIzxsdXmaKMCUulHhFR2BrpaLF6TDFQXmr3wA"" \
    -H "Content-Type: application/json" \
    -d '{
        "username": "newuser1",
        "first_name": "John Updated",
        "phone_number": "123"
    }'
