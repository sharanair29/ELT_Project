Mock APIs were used for two data sources in the formats as below:

Source 1 : Profile

https://mocki.io/v1/d28204d5-99e7-4795-b8f5-79fc1ca94617

Source 2 : Company

https://mocki.io/v1/bcc2aa32-0eee-4058-bafa-2a9aa5030995

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


The `dagster` folder contains a sub-folder called `repository_like_module` which has subfolders for dagster assets, jobs, ops and schedules. Airbyte connection ids were used to schedule airbyte jobs from dagster. DBT-RPC was used to schedule dbt runs from dagster and this version is deprecated from version 1.5 onwards which is why this project utilizes dbt version 1.4.

The dagster folder has Dockerfiles that were taken from the example https://docs.dagster.io/examples/deploy_docker.

The `dbt` folder contains the dbt project as well as a Dockerfile to containerize it.

To check the health of each component:

## DBT

Send a GET request to http://localhost:8580/ with the raw json as below.


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
