# Write your MySQL query statement below
-- select e.departmentId as Department, e.name as Employee, e.salary as Salary from Employee as e inner join Department as d on e.id = d.id order by d.departmentId;

select Department, Employee, Salary from
(
    select d.name as Department, e.name as Employee, e.salary as Salary, dense_rank() over (partition by d.id order by e.salary desc) as r
    from Employee e
    left join
    Department d 
    on e.departmentId  = d.id 
) temp
where r = 1


-- select name, salary