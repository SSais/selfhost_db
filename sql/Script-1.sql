-- renaming column names
ALTER TABLE strong
RENAME COLUMN "Date" TO date;
ALTER TABLE strong
RENAME COLUMN "Duration" TO duration;
ALTER TABLE strong
RENAME COLUMN "Workout Name" TO workout_name;
ALTER TABLE strong
RENAME COLUMN "Exercise Name" TO exercise_name;
ALTER TABLE strong
RENAME COLUMN "Set Order" TO set_order;
ALTER TABLE strong
RENAME COLUMN "Weight" TO weight;
ALTER TABLE strong
RENAME COLUMN "Reps" TO reps;


-- check rows
SELECT 
	COUNT(date)
FROM 
	strong;


-- check columns
SELECT 
	COUNT(*) as No_of_columns 
FROM 
	information_schema.columns 
WHERE 
	table_name ='strong';


-- remove the columns not required
ALTER TABLE strong
DROP COLUMN "Distance";
ALTER TABLE strong
DROP COLUMN "Seconds";
ALTER TABLE strong
DROP COLUMN "Notes";
ALTER TABLE strong
DROP COLUMN "Workout Notes";
ALTER TABLE strong
DROP COLUMN "RPE";


-- checking for nulls
SELECT 
	date, workout_name, duration, exercise_name, set_order, weight, reps  
FROM 
	strong
where date is null;


-- primary key added
ALTER TABLE strong 
ADD COLUMN id SERIAL PRIMARY KEY;


-- ordering by asc/desc for each column to check for anomalous results
select * from strong order by date asc;
select * from strong order by date desc;

-- duration is a string I need to change it into an integer
select * from strong order by duration asc;
select * from strong order by duration desc;

select * from strong order by set_order asc;
select * from strong order by set_order desc;

select * from strong order by weight asc;
select * from strong order by weight desc;


--noticed that I have entered some workouts as 0 reps when I have skipped them, so I will delete rows with 0 reps
select * from strong order by reps asc;
select * from strong order by reps desc;


-- removing rows where reps = 0
BEGIN TRANSACTION; -- learned about transaction to be safer when removing data
DELETE FROM strong
WHERE reps = 0;
COMMIT; 


-- renaming a table (optional)
ALTER TABLE strong RENAME TO strong_origonal;


