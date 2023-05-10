from dagster import job
from ..ops import ops
from dagster_dbt import dbt_run_op

# Extract and Load with Airbyte only


@job(resource_defs={"airbyte": ops.my_airbyte_resource})
def extract_person():
    ops.extract_person_api()


@job(resource_defs={"airbyte": ops.my_airbyte_resource})
def extract_company():
    ops.extract_company_s3()


## Extract, Load with Airbyte and DBT Models


@job(
    resource_defs={
        "dbt": ops.custom_dbt_rpc_resource,
        "airbyte": ops.my_airbyte_resource,
    }
)
def dependencies_airbyte_dbt():
    dbt_run_op([ops.extract_person_api(), ops.extract_company_s3()])
