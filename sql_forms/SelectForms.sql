select * from t;
select a from t;
select a, b from t;
select a, count(*) as cnt from t group by a;
select * from t where f(a) = g(b);
select * from t where f(a) = g(b) or a > 1;
select * from t where f(a) = g(b) and b < 1;
select distinct a, b, c from t where f2(g(a), b) = h(v(c));
select * from t order by a;
select * from t limit 1;
select * from t order by a desc limit 0, 1;
select min(a), max(b) from t having f(sum(a)) > 1;
select sum(b) as c1, f(g(min(c))) as c2 from t group by a having g(g(g(count(distinct d)))) = 1;
select f(1) as col1, pi() as `length of circle divide on lentgh of diametr`;
select * from t limit 1 offset 5;
select `кирилический столбец` from t1, t2, t3, t4, t5;
select t1.a, t2.b, t4.c from t1, t2, t3, t4, t5 where t1.a > 1 and t2.b < 1 or t4.c in (0, 1, 2) order by t1.a asc, t2.b desc;
select t1.a, f(f2(t1.a, h2(1, t2.b)), g(t1.a + t2.b)) from t1 inner join t2 inner join t3;
select t1.a from t1 inner join t2;
select t1.a, t2.b from t1 inner join t2, t3;
select f(t1.a) + g(t2.b) as col1 from t1 inner join t2 on t1.c = t2.c;
select t1.a > 0 + t2.b*t1.c as col1 from t1 inner join t2 on t1.c = t2.c inner join t3;
select tt.b * tt.b * tt.c, sum(t1.a) from t1 cross join t2 as tt using(d) group by tt.b * tt.b * tt.c;
select firstT.*, secondT.* from t1 as firstT natural join t2 as secondT;
select * from t1 inner join t2 using (a) inner join t3 using(b) inner join t4 using(aa);
select t1.a, t2.b, nt.c from t1, t2 inner join t2 as nt on t2.c = nt.c and t2.a = nt.b order by t1.a, nt.b desc;
select t1.a, t2.b from t join tt using(c), ttt, t1 inner join t2 on t1.a = t2.b or t1.a = t2.a + t2.c cross join tt1 using(dd);
select case when t1.a in (1, 2, 3) then 'str1' when somecol * (t1.a%4) - floor((col * 2 + somecol - 4 * b)/0.3) then 'another_str' end as col1 from t1 straight_join tt;
select t1.*, t2.* from t1 left outer join t2 on t1.a = t2.a + t2.b where (t1.a * t2.c, 4 * t1.d) = (t2.a * t1.c, t2.dd / 4);
select * from t1, t2 left join t3 on true cross join t4, t5;
select * from t1, t2 inner join t3, t4 right join t5 on t4.aa = t5.bb order by 1, 2 desc;
select * from t1 right join t2 using(c) left join t3 using (b) left join t4 on t1.a = t3.b - t4.d;
select * from t1 cross join t2, t3 left join t4 on true join t5 on t4.a = t5.b, t6, t7, t8 right join t9 using (col) inner join t10;
select !a>0, bit_c1 ^ bit_c2 from t where ((c + b) >> d) or ( (a > 2) and b + c < d * 5 * c mod 2 ) or (a|b|c|d|bb) or d in (1, 2, a * 2, f(a));
select * from t1 inner join t2 using(c) into outfile 'file' character set cp1251 fields terminated by ';' lines terminated by '\r\n';
select t1.*, t2.* into outfile 'file' fields terminated by ',' enclosed by '"' lines starting by '--' from t1, t2 where t1.a = t2.b order by t1.c;
select * from t1 partition (c1, c2) as t_history order by col1, f(col2) desc;
select * from t1 partition (c1, c2) as t_history group by col1, f(col2) with rollup;