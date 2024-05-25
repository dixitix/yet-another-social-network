curl -X POST http://localhost:5001/register \
    -H "Content-Type: application/json" \
    -d '{
        "username": "newuser",
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
        "username": "newuser",
        "password": "password123"
    }'


curl -X PUT http://localhost:5001/update \
-H "Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMzIwNjAyNywianRpIjoiNDRiYWQ5ZWUtNDlhZC00YmRmLTgwNGMtMTQwNTIxOGUwNThmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5ld3VzZXIiLCJuYmYiOjE3MTMyMDYwMjcsImNzcmYiOiJmZmRiMzI5Zi1kYzVlLTQ1YTUtYTM0YS00MGMwZjlhNWZiMjgiLCJleHAiOjE3MTMyMDk2Mjd9.raF7ONjalGFjXtMifb6lS7v9cw8O3JPgEkMtebRLQIM"" \
    -H "Content-Type: application/json" \
    -d '{
        "username": "newuser",
        "first_name": "John Updated",
        "phone_number": "123"
    }'
