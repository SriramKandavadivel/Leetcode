# Write your MySQL query statement below
select s.student_id, s.student_name , b.subject_name, (
    select Count(*)
    from Examinations e where e.student_id = s.student_id and b.subject_name = e.subject_name
) as attended_exams
from Students s ,Subjects b
order by s.student_id , b.subject_name  ;
