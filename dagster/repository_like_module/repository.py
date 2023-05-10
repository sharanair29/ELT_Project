from dagster import repository, job, op
from .assets import assets
from .jobs import jobs
from .schedules import schedules
from .sensors import sensors
from .ops import ops
from dagster_dbt import dbt_run_op


# DBT TEST


@job(resource_defs={"dbt": ops.custom_dbt_rpc_resource})
def my_dbt_rpc_job():
    dbt_run_op()


@repository
def repository_like_module():
    return [
        jobs.dependencies_airbyte_dbt,
        my_dbt_rpc_job,
        jobs.extract_company,
        jobs.extract_person,
        # my_dbt_job,
        schedules.company_schedule,
        schedules.person_schedule,
    ]
