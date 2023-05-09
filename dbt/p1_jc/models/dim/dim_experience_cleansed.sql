{{
    config(
        materialized = 'view'
    )
}}

WITH SRC_EXPERIENCE AS (
    SELECT * FROM {{ ref('src_experience') }}
) 

SELECT PROFILE_ID,
CASE
        WHEN JOB_STARTDATE = 'present' THEN CURRENT_TIMESTAMP
        ELSE CAST(JOB_STARTDATE AS TIMESTAMP)
END AS JOB_START,

CASE
        WHEN JOB_ENDDATE = 'present' THEN CURRENT_TIMESTAMP
        ELSE CAST(JOB_ENDDATE AS TIMESTAMP)
END AS JOB_END,

CASE
        WHEN JOB_ENDDATE = 'present' THEN 'TRUE'
        ELSE 'FALSE'
END AS CURRENT_JOB,

DATEDIFF(MONTH, JOB_START, JOB_END) AS MONTHS,
COMPANY_NAME,
LOCATION,
JOB_DESCRIPTION

FROM SRC_EXPERIENCE

WHERE JOB_DELETED = FALSE