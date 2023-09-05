# Getting Started for the Course 

### Airflow Docker Setup 
1. Download the community edition of Docker 
2. Make sure you have Docker Compose V2 installed locally 
3. Follow the install guide from Airflow docs: [Install Airflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
4. Run docker compose to initialize instance `docker compose up airflow-init` - the account created has *the login airflow* and *the password airflow*.


**Tip:** make sure to allocate at least 4GB of memory for your Airflow image in Docker 

### Running Airflow 
1. Run `docker compose up` 
2. The webserver is available at: http://localhost:8080. The default account is the one from above. 

### Cleaning Up Docker and Airflow 
1. Run `docker compose down --volumes --rmi all`
