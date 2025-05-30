Mock APIs were used for two data sources in the formats as below:

Source 1 : Profile

https://mocki.io/v1/bfb9dc25-d4ad-457c-a3a7-ec3bc7abb088

Source 2 : Company

https://mocki.io/v1/b14560dc-c072-43cb-97a5-03ffd590eee3

Copy the `.example.env` file to `.env` and add your snowflake credentials

To build the required images run:

`docker compose -f docker-compose.yml -f docker-compose.airbyte.yml build`

To run the containers:

`docker compose -f docker-compose.yml -f docker-compose.airbyte.yml up`

![jc_architecture](https://github.com/sharanair29/ELT_Project/assets/94154731/72b43cdf-c410-4abc-93a7-f5a77b38bbb3)

# Input Data Model 
![input_data_model](https://github.com/sharanair29/ELT_Project/assets/94154731/f09ee2d9-b2fe-4a3d-8775-249dd4f747e6)

# DBT Data Flow
![dbtdataflow](https://github.com/sharanair29/ELT_Project/assets/94154731/94c4f7fa-bd12-4f23-bfa1-13d04e5dd734)

# Docker Network
![docker_network](https://github.com/sharanair29/ELT_Project/assets/94154731/ac0c5107-40b1-4b8f-841d-3da5256f3957)


The `dagster` folder contains a sub-folder called `repository_like_module` which has subfolders for dagster assets, jobs, ops and schedules. Airbyte connection ids were used to schedule airbyte jobs from dagster. DBT-CLI was used to schedule dbt runs from dagster.

The dagster folder has Dockerfiles that were taken from the example https://docs.dagster.io/examples/deploy_docker.

The `dbt` folder contains the dbt project as well as a Dockerfile to containerize it, this is no longer needed since we have moved from DBT-RPC to DBT-CLI.

To check the health of each component:

## DBT (Ignore this section)

Send a GET request to http://localhost:8580/jsonrpc with the raw json as below.


`
{
    "jsonrpc": "2.0",
    "method": "status",
    "id": "2db9a2fe-9a39-41ef-828c-25e04dd6b07d"
}
`

You should receive the output:

`
{
    "result": {
        "logs": [],
        "state": "ready",
        "error": null,
        "timestamp": "2023-05-09T15:23:01.873680Z",
        "pid": 1
    },
    "id": "2db9a2fe-9a39-41ef-828c-25e04dd6b07d",
    "jsonrpc": "2.0"
}
`

## Airbyte

Send a GET request to http://localhost:8000/api/v1/health/

You should receive the output:

`
{
    "available": true
}
`

## Dagster

Send a POST request using GraphQL to http://localhost:3000/graphql as below:

`{version}`

You should receive the output:

`
{
    "data": {
        "version": "1.3.2"
    }
}
`

Create a snowflake account on the free trial version. 

Open Airbyte on localhost:8000

Create a new source ---> insert your Mock API URL with the File Connector

Create a new destination to Snowflake:

![alt text](__readme_images/image.png)

As per the image above, upon selection snowflake you will get a list of steps on what scripts to run on Snowflake to create the necessary entities

Hit Run All:
![alt text](__readme_images/image-1.png)

Set up the destination and run your first manual run from the source to the destination and on snowflake you should have the denormalized and normalized raw output.

![alt text](__readme_images/image-19.png)

Source:
![alt text](__readme_images/image-20.png)


Destination:
![alt text](__readme_images/image-21.png)

Connections:
![alt text](__readme_images/image-22.png)


Now you have a successful pipeline. To orchestrate this from dagster with the respective dbt transformations: 
To find the connection id:
![alt text](__readme_images/image-11.png)

Use this connection id within your dagster files to schedule a job:
![alt text](__readme_images/image-12.png)

Open Dagster UI on localhost:3000 from your browser:

![alt text](__readme_images/image-13.png)

![alt text](__readme_images/image-14.png)


![alt text](__readme_images/image-15.png)
![alt text](__readme_images/image-18.png)
DBT Models Output:
![alt text](__readme_images/image-17.png)