# Million Song Data Lake and Data Warehouse

## Project Overview

This project simulates the work of a data engineer at **Sparkify**, a music streaming startup. Sparkify wants to migrate its user activity and song metadata from AWS S3 into a cloud-based analytical platform. As part of this initiative, we built an **ETL pipeline** using **Databricks** and **Delta Lake**, transforming raw JSON files into a **star schema** data warehouse optimized for analytical queries.

---

## Data Sources

- **Song Data**: Metadata about songs and artists  
  `s3://techcatalyst-public/song_data`

- **Log Data**: User activity logs from the Sparkify app  
  `s3://techcatalyst-public/log_data`

---

## Technologies Used

- **Databricks** (Pyspark, Delta Lake)
- **AWS S3** (Raw data storage)
- **Delta Lake Tables** (Staging and production layers)
- **Star Schema Design** (Fact and dimension tables)

---

## Entity Relationship Diagram (ERD)

![ERD Diagram](./Star_schema.png)

---

## ETL Architecture and Process

![ETL Process](./ETL_Process.png)



---


## Delta Lake Tables
Delta Lake tables are a reliable and scalable storage layer for Sparkify’s data. By converting thousands of raw JSON files into just five structured tables, we:
- Improve query performance and data reliability
- Indexed and optimized
- Simplify data exploration for analysts
- Allows for handling of large scale analytics with spark
- Analysts can use SQL
- This architecture supports Sparkify’s goal of understanding user behavior and song popularity without the overhead of managing raw files.


---


## Deltabricks vs Snowflake

- SQL-native querying via Spark SQL
- Delta Lake for scalable, reliable storage
- Integrated notebooks and ML tools
- Cost savings (no additional license)

---

## Summary of process
- Extract: Read raw JSON files from S3.
- Stage: Store raw data as Delta Tables in Databricks.
- Transform: Clean and normalize data into structured tables.
- Load: Create star schema tables for analytics.

---

## Example Queries

```
-- How many songs have no year?
select count(*) ​
from songs_dim ​
where year = 0
```
-- What is the user gender counts?
```
select gender, count(*)​
from users_dim ​
group by gender​
order by count(*) desc
```

-- What is the count of paid and free users?
```
select SP.level, count(*)​
from songplays_fact SP​
join users_dim U on SP.user_id = U.userId AND SP.level = U.level​
group by SP.level
```

-- What is the averate total session duration?
```
WITH DUR_BY_SESS AS (​
SELECT SUM(duration) AS TOTAL_LISTENED​
FROM songplays_view​
GROUP BY session_id​
ORDER BY session_id DESC​
)
SELECT AVG(TOTAL_LISTENED)​
FROM DUR_BY_SESS​
```
