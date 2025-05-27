from dagster import op

from dagster_airbyte import airbyte_resource, airbyte_sync_op
from ..shared import constants


my_airbyte_resource = airbyte_resource.configured(constants.AIRBYTE_CONFIG)

## Extract and Load from source ##
extract_profile = airbyte_sync_op.configured(
    {"connection_id": "d14c97e3-db2c-487f-9a1c-bc5de54b623b"}, name="extract_profile"
)
extract_company = airbyte_sync_op.configured(
    {"connection_id": "eca91860-de45-4c63-83ca-3d9e1e219c32"}, name="extract_company"
)




# add
from dagster_dbt import dbt_run_op 