/*Query 1: Retrieve all employees whose address is in Elgin,IL*/
select * from employees where address like '%Elgin,IL';

/*Query 2: Retrieve all employees who were born during the 1970's.*/
select * from employees where b_date like '197%';

/*Query 3: Retrieve all employees in department 5 whose salary is between 60000 and 70000*/
select * from employees where dep_id = 5 and salary between 60000 and 70000;

/*Query 4A: Retrieve a list of employees ordered by department ID.*/
select * from employees order by dep_id;

/*Query 4B: Retrieve a list of employees ordered in descending order by
department ID and within each department ordered alphabetically in
descending order by last name.*/
select * from employees order by dep_id desc, l_name desc;

/*Query 5A: For each department ID retrieve the number of employees in the department.*/
select dep_id, count(dep_id) as count from employees group by dep_id;

/*Query 5C: For each department retrieve the number of employees in the
department, and the average employees salary in the department.*/
select dep_id, count(dep_id) as count,  avg(salary) as avg_salary from employees group by dep_id;

/*Query 5D: In Query 5C order the result set by Average Salary.*/
select dep_id , count(dep_id) as num_employees, avg(salary) as avg_salary from employees group by dep_id  order by avg_salary;

/*Query 5E: In Query 5D limit the result to departments with fewer than 4 employees.*/
select dep_id, count(dep_id) as num_employees, avg(salary) as avg_salary from employees group by dep_id having count(dep_id) < 4 order by avg_salary;

/*BONUS Query 6: Similar to 4B but instead of department ID use department
name. Retrieve a list of employees ordered by department name, and within
each department ordered alphabetically in descending order by last name.*/
select * from employees as E, departments as D where E.dep_id = D.dept_id_dep order by D.dep_name, E.l_name desc;

