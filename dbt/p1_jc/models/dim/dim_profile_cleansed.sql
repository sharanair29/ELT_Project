{{
    config(
        materialized = 'view'
    )
}}

WITH 

EXPERIENCE AS (
    SELECT PROFILE_ID, SUM(MONTHS) AS MONTHS_EXPERIENCE, COUNT(MONTHS) AS NO_OF_JOBS
    FROM {{ ref('dim_experience_cleansed') }} GROUP BY PROFILE_ID
),

EDU AS (
        SELECT PROFILE_ID, SUM(MONTHS) AS MONTHS_EDUCATION, COUNT(MONTHS) AS NO_OF_EDU
        FROM {{ ref('dim_education_cleansed') }} GROUP BY PROFILE_ID
),

P AS (
        SELECT * FROM {{ ref('src_profile') }}
),

LOC AS (
        SELECT * FROM {{ ref('src_location') }}
),

S AS (
        SELECT PROFILE_ID, COUNT(SKILL_TYPE) AS SKILL_COUNT
        FROM {{ ref('src_skills') }} GROUP BY PROFILE_ID
)

SELECT * FROM P

NATURAL JOIN LOC

NATURAL JOIN EXPERIENCE

NATURAL JOIN EDU

NATURAL JOIN S