View this example in the Dagster docs at https://docs.dagster.io/examples/deploy_docker.

Copy the `.example.env` file to `.env` and add your snowflake credentials

To build the required images run:

`docker compose -f docker-compose.yml -f docker-compose.airbyte.yml build`

To run the containers:

`docker compose -f docker-compose.yml -f docker-compose.airbyte.yml up`

![jc_architecture](https://github.com/sharanair29/ELT_Project/assets/94154731/2d787e29-4a91-401c-b63a-e7355d055333)
![docker_network](https://github.com/sharanair29/ELT_Project/assets/94154731/ac0c5107-40b1-4b8f-841d-3da5256f3957)

The `dagster` folder contains a sub-folder called `repository_like_module` which has subfolders for dagster assets, jobs, ops and schedules. Airbyte connection ids were used to schedule airbyte jobs from dagster. DBT-RPC was used to schedule dbt runs from dagster and this version is deprecated from version 1.5 onwards which is why this project utilizes dbt version 1.4.