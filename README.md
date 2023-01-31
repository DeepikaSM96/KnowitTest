# KnowitTest
Created New Repository in Github with the initial commit.
Install the Docker from docker.com and Postgresql database to use it locally
Using sql shell(psql) logged in with the password which we used during the installation and connected to server with the below details
host:localhost Port:5432 and username as postgres.
To connect or sync docker with postgresql use the below command in prompt:
docker run --name postgresql -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=my password -p 5432:5432 -v /data:/var/lib/postgresql/data -d postgres
This will pull the image to the docker container 
Using python script databse can be populated with information form API using the URL

