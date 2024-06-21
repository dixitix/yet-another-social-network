curl -X GET 'http://localhost:50052/healthcheck'

docker exec -it 17dc530e9738 clickhouse-client

curl -X GET 'http://localhost:50052/likes'

curl -X GET 'http://localhost:50052/views'

curl -X PUT 'http://localhost:5001/like/6675993dbcf2f7a7c39bee20' \
-H "Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxODk5MzczOCwianRpIjoiMzJmZWQxYmUtZTkyZi00ZjY5LWIxYWItM2I3NWRlNjI0MDc3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5ld3VzZXIxIiwibmJmIjoxNzE4OTkzNzM4LCJjc3JmIjoiYjk3OGI1MTYtNDUxMS00NDE4LTk4YjctMGVkZmU5ZGQ5M2QzIiwiZXhwIjoxNzE4OTk3MzM4fQ.7AcG-kwCgG_hPlBGsHCWs0kz7aXN0aAMGdrHKhi0Vag""

curl -X PUT 'http://localhost:5001/view/6675993dbcf2f7a7c39bee20' \
-H "Authorization: Bearer  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxODk5MjA3NSwianRpIjoiNDhlYzEzZjktMWYyMS00YWM0LWEyZDMtM2ZjMTU4YjliYjhkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5ld3VzZXIxIiwibmJmIjoxNzE4OTkyMDc1LCJjc3JmIjoiNzM3MGQ4M2MtMWUyMC00ODIzLTkzNmMtYWQzMDA5NzNlODIyIiwiZXhwIjoxNzE4OTk1Njc1fQ.xME3LBbPL7HZTqlin-anTG8iEVC6faIoOWpS6MKMW8M""

