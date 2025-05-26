from dagster import op

from dagster_airbyte import airbyte_resource, airbyte_sync_op
from ..shared import constants
from dagster_dbt import dbt_rpc_sync_resource


my_airbyte_resource = airbyte_resource.configured(constants.AIRBYTE_CONFIG)

## Extract and Load from source ##
extract_profile = airbyte_sync_op.configured(
    {"connection_id": "ffb2a90f-d69f-4477-8d9b-8e7b87773d42"}, name="extract_profile"
)
extract_company = airbyte_sync_op.configured(
    {"connection_id": "45642395-ea02-4f7b-a340-1f8f23629e1c"}, name="extract_company"
)


custom_dbt_rpc_resource = dbt_rpc_sync_resource.configured(constants.DBT_CONFIG)
