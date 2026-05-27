# Write your MySQL query statement below


select avg(salary) as SecondHighestSalary from(
    select salary, dense_rank() over(order by salary desc) as rn
    from Employee
) t
where rn = 2;