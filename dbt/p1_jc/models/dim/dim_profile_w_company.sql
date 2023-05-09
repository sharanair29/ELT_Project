
WITH 

P AS (
        SELECT * FROM {{ ref('dim_profile_cleansed') }}
),

J AS (
        SELECT * FROM {{ ref('dim_experience_cleansed') }} WHERE CURRENT_JOB = 'TRUE'
),

E AS (
        SELECT MAX(EDU_END) AS EDU_END  FROM {{ ref('dim_education_cleansed') }} GROUP BY PROFILE_ID
),

C AS (
        SELECT * FROM {{ ref('dim_company_cleansed') }}
) 
 
SELECT * FROM P

NATURAL JOIN J

NATURAL JOIN E

NATURAL JOIN C

