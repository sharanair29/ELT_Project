

WITH RAW_PROFILE_EXPERIENCE AS (
    SELECT * FROM {{ source('airbyte_database', 'profile_experience') }}
)

SELECT 
    _AIRBYTE_EXPERIENCE_HASHID AS HASHID_EXPERIENCE,
    _AIRBYTE_RAW_PROFILE_HASHID AS PROFILE_ID,
    STARTDATE AS JOB_STARTDATE,
    ENDDATE AS JOB_ENDDATE,
    TITLE,
    COMPANY AS COMPANY_NAME,
    LOCATION,
    DESCRIPTION AS JOB_DESCRIPTION,
    DELETED AS JOB_DELETED
FROM
    RAW_PROFILE_EXPERIENCE