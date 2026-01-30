SELECT
    i.INGREDIENT_TYPE,
    SUM(f.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF f
JOIN ICECREAM_INFO i
  ON f.FLAVOR = i.FLAVOR
GROUP BY i.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC;


'''
같은코드 / inner join 할 때는 where 쓰는게 더 직관적 
    outerjoin 은 join 써야함 
select i.ingredient_type, sum(f.total_order) as total_order
from first_half f, icecream_info i
where f.flavor = i.flavor
group by i.ingredient_type
order by total_order asc

'''
