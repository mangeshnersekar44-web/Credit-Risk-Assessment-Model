-- Active: 1772520994257@@127.0.0.1@3306@credit_risk_db

SELECT COUNT(*) FROM credit_data;
SELECT * FROM credit_data LIMIT 5;
DESCRIBE credit_data;

-- Check total records
SELECT COUNT(*) AS total_records
FROM credit_data;

-- ============================================================
--  Loan Default Distribution
-- ============================================================

SELECT 
    loan_status,
    COUNT(*) AS total_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM credit_data), 2) AS percentage
FROM credit_data
GROUP BY loan_status;




-- ============================================================
--  Default Rate by Loan Grade
-- ============================================================

SELECT 
    loan_grade,
    COUNT(*) AS total_loans,
    ROUND(AVG(loan_status) * 100, 2) AS default_rate_percentage
FROM credit_data
GROUP BY loan_grade
ORDER BY default_rate_percentage DESC;



-- ============================================================
--  Default Rate by Home Ownership
-- ============================================================

SELECT 
    person_home_ownership,
    COUNT(*) AS total_loans,
    ROUND(AVG(loan_status) * 100, 2) AS default_rate_percentage
FROM credit_data
GROUP BY person_home_ownership
ORDER BY default_rate_percentage DESC;


-- ============================================================
-- Default Rate by Loan Intent
-- ============================================================

SELECT 
    loan_intent,
    COUNT(*) AS total_loans,
    ROUND(AVG(loan_status) * 100, 2) AS default_rate_percentage
FROM credit_data
GROUP BY loan_intent
ORDER BY default_rate_percentage DESC;


-- ============================================================
--  Income Comparison (Default vs Non-Default)
-- ============================================================

SELECT 
    loan_status,
    ROUND(AVG(person_income), 2) AS avg_income
FROM credit_data
GROUP BY loan_status;


-- ============================================================
--  High Risk Pattern Analysis
-- ============================================================

-- High income but defaulted
SELECT *
FROM credit_data
WHERE person_income > 100000
AND loan_status = 1;

-- Large loan & high interest rate
SELECT *
FROM credit_data
WHERE loan_amnt > 20000
AND loan_int_rate > 15;


-- ============================================================
--  Credit History Risk Analysis
-- ============================================================

SELECT 
    CASE 
        WHEN cb_person_cred_hist_length < 5 THEN 'Short History'
        WHEN cb_person_cred_hist_length BETWEEN 5 AND 10 THEN 'Medium History'
        ELSE 'Long History'
    END AS credit_history_group,
    ROUND(AVG(loan_status) * 100, 2) AS default_rate_percentage
FROM credit_data
GROUP BY credit_history_group
ORDER BY default_rate_percentage DESC;


-- ============================================================
--  Create View for Dashboard
-- ============================================================

CREATE OR REPLACE VIEW default_summary AS
SELECT 
    loan_grade,
    COUNT(*) AS total_loans,
    ROUND(AVG(loan_status) * 100, 2) AS default_rate_percentage
FROM credit_data
GROUP BY loan_grade;