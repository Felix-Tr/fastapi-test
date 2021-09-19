### Fastapi Test

The repository is a fastapi test with a simple dockerization.

To build the container run:

`sudo docker build -t fastapi ./`

`sudo docker run -d --name fastapi-test -p 80:80 fastapi`

now the integer to string endpoint should be accessible via http://127.0.0.1/convert/, 
for details on the json body see http://127.0.0.1/docs.