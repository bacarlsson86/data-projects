Question 1:
24.3.1

Question 2:
postgres:5433
OR
postgres:5432
5433 is mapped to 5432, so they amount to the same thing
OR

Question 3:
1. 104,802
SELECT COUNT(*)
FROM green_taxi_data 
WHERE lpep_pickup_datetime > '2019-09-30' 
AND lpep_dropoff_datetime < '2019-11-01'
AND trip_distance <= 1

2. 198,925
SELECT COUNT(*)
FROM green_taxi_data 
WHERE lpep_pickup_datetime > '2019-09-30' AND lpep_dropoff_datetime < '2019-11-01'
AND 1 < trip_distance AND trip_distance <=3

3. 109,603
SELECT COUNT(*)
FROM green_taxi_data 
WHERE lpep_pickup_datetime > '2019-09-30' AND lpep_dropoff_datetime < '2019-11-01'
AND 3 < trip_distance AND trip_distance <= 7

4. 27678
SELECT COUNT(*)
FROM green_taxi_data 
WHERE lpep_pickup_datetime > '2019-09-30' AND lpep_dropoff_datetime < '2019-11-01'
AND 7 < trip_distance AND trip_distance <= 10

5. 35189
SELECT COUNT(*)
FROM green_taxi_data 
WHERE lpep_pickup_datetime > '2019-09-30' AND lpep_dropoff_datetime < '2019-11-01'
AND 10 < trip_distance

- 104,802;  198,924;  109,603;  27,678;  35,189
For some reason 2 is off by 1?

Question 4:
2019-10-31

Question 5:
What are the top pickup locations with fares over 13,000 in aggregate?

East Harlem North, East Harlem South, Morningside Heights

SELECT total_sum, joint_sum."Zone"
FROM (SELECT SUM(g.total_amount) total_sum, z."Zone"
FROM green_taxi_data g
INNER JOIN zones z
ON g."PULocationID" = z."LocationID"
WHERE DATE_TRUNC('day',g.lpep_pickup_datetime) = '2019-10-18'
GROUP BY z."Zone"
ORDER BY total_sum DESC) AS joint_sum
WHERE total_sum > 13000

Question 6:
87.30

SELECT g.tip_amount, zdo."Zone" "drop off zone"
FROM green_taxi_data g
JOIN zones zpu
ON g."PULocationID" = zpu."LocationID"
JOIN zones zdo
ON g."PULocationID" = zdo."LocationID"
WHERE g.tip_amount = (
SELECT MAX(tip_amount)
FROM green_taxi_data g
JOIN zones zpu
ON g."PULocationID" = zpu."LocationID"
JOIN zones zdo
ON g."PULocationID" = zdo."LocationID"
WHERE zpu."Zone" = 'East Harlem North'
)

7. terraform init, terraform apply -auto-approve, terraform destroy