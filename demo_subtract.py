from pyspark import SparkContext

sc=SparkContext('local[2]','Intersection Example program')

Officer_salary=[25000,30000,35000,40000,20000,25000]

labour_salary=[40000,7000,8000,25000,30000,6000,4500]

Officer_salary_rrd=sc.parallelize(Officer_salary)

labour_salary_rrd=sc.parallelize(labour_salary)

subtract_rrd=labour_salary_rrd.subtract(Officer_salary_rrd)

print(subtract_rrd.count())

print(subtract_rrd.collect())