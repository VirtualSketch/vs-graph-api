# vs-graph-api

## Run with docker

<hr />

**Build docker image**
````docker
docker build . --no-cache -t python-server
````
**First run container**
````docker
docker run --name python-server -d -p 5000:5000 -t python-server
````

**Run container**
````docker
docker start python-server
````

**Stop container**
````docker
docker stop python-server
````