from dagster import ScheduleDefinition, DefaultScheduleStatus
from ..jobs import jobs


person_schedule = ScheduleDefinition(
    job=jobs.extract_person,
    cron_schedule="0 0 * * 0",
    default_status=DefaultScheduleStatus.RUNNING,
)

company_schedule = ScheduleDefinition(
    job=jobs.extract_company,
    cron_schedule="0 0 1 * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
