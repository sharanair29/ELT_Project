{% snapshot scd_raw_company %}
{{
config(
       target_schema='dev',
       unique_key='_AIRBYTE_AB_ID',
       strategy='timestamp',
       updated_at='_AIRBYTE_EMITTED_AT',
       invalidate_hard_deletes=True
) }}
select * FROM {{ source('airbyte_database', 'company') }}
{% endsnapshot %}