from dagster import op

from dagster_airbyte import airbyte_resource, airbyte_sync_op
from ..shared import constants
from dagster_dbt import dbt_rpc_sync_resource


my_airbyte_resource = airbyte_resource.configured(constants.AIRBYTE_CONFIG)

## Extract and Load from source ##
extract_person_api = airbyte_sync_op.configured(
    {"connection_id": "aa94fbc2-8f03-4f22-bee4-3e7bf67a50bb"}, name="extract_person_api"
)
extract_company_s3 = airbyte_sync_op.configured(
    {"connection_id": "4bebbd7c-de07-4f63-b635-c3a0c3e662c8"}, name="extract_company_s3"
)


custom_dbt_rpc_resource = dbt_rpc_sync_resource.configured(constants.DBT_CONFIG)
