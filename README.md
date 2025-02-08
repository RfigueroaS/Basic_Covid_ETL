# Basic COVID-19 ETL Pipeline
ETL pipeline to process and analise global data related to COVID-19 confirmed cases.

## Tecnologies
- **Python**: To clean and transform the data.
- **Pandas**: For dataset manipulation.
- **SQLite**: To store the processed data.
- **Metabase**: Data analysis and visualization.
- **Cron (automation)**

## ETL process
1. **Extraction**: Downloaded the dataset 'RAW_global_confirmed_cases.csv' from kaggle.
2. **Transformation**: Use of pandas to clean the data and convert from "wide" to "long" format.
3. **Load**: Stored the data in a SQLite database.

## Data scheme
Table `confirmed_cases`:
- country (TEXT)
- date (DATE)
- cases (INTEGER)

## SQL Query example
```sql
SELECT country, MAX(cases) as total_cases
FROM confirmed_cases
GROUP BY country
ORDER BY total_cases DESC;
```
[![SQL Query](https://imgur.com/a/Dybxvly "SQL Query")](Query "SQL Query")
 ![](https://i.imgur.com/gdh45kp.png)

## Visualization
[![Metabase dashboard](https://imgur.com/a/6UHRuGc "Metabase dashboard")](Dashboard "Metabase dashboard")
