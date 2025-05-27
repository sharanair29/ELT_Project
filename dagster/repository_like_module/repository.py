from dagster import repository
from .jobs import run_dbt_job
from .jobs import jobs
from .schedules import schedules
from .sensors import sensors

@repository
def repository_like_module():
    return [
        run_dbt_job,
        jobs.extract_company_job,
        jobs.extract_profile_job,
        schedules.company_schedule,
        schedules.profile_schedule
        ]