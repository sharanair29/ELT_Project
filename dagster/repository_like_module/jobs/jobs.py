from dagster import job
from dagster_dbt import dbt_cli_resource, dbt_run_op
from ..ops import ops

@job(resource_defs={"airbyte": ops.my_airbyte_resource})
def extract_profile_job():
    ops.extract_profile()


@job(resource_defs={"airbyte": ops.my_airbyte_resource})
def extract_company_job():
    ops.extract_company()


@job(resource_defs={
    "dbt": dbt_cli_resource.configured({
        "project_dir": "/usr/app/dbt",
        "profiles_dir": "/root/.dbt"
    })
})
def run_dbt_job():
    dbt_run_op()