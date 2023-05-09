WITH 

COMPANY AS (
        SELECT COMPANY_ID, COMPANY_NAME FROM {{ ref('dim_company_cleansed') }}
),

L AS (
        SELECT * FROM {{ ref('src_locationcompany') }}
),

SOCIAL AS (
       SELECT * FROM {{ ref('src_companysocialmedia') }}
)

SELECT * FROM COMPANY 
NATURAL JOIN SOCIAL
NATURAL JOIN L