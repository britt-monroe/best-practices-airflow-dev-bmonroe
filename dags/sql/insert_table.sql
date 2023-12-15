INSERT INTO `airflow_best_practices`.`powerball_winning_numbers_multiplier_3`
SELECT * FROM airflow_best_practices.powerball_winning_numbers
WHERE Multiplier = '3';
