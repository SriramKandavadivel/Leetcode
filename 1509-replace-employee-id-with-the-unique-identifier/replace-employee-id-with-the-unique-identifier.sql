# Write your MySQL query statement below
select unique_id,name from Employees left Join EmployeeUNI on Employees.id = EmployeeUNI.id;