# Basic COVID-19 ETL Pipeline
ETL pipeline to process and analise global data related to COVID-19 confirmed cases.

## Tecnologies
- **Python**: To clean and transform the data.
- **Pandas**: For dataset manipulation.
- **SQLite**: To store the processed data.
- **Metabase**: Data analysis and visualization.

## ETL process
1. **Extraction**: Download of the dataset 'RAW_global_confirmed_cases.csv' from kaggle.
2. **Transformation**: Use of pandas to clean the data and convert from "wide" to "long" format.
3. **Load**: Stored the data in a SQLite database.

## Data scheme
Table `confirmed_cases`:
- country (TEXT)
- date (DATE)
- cases (INTEGER)

## SQL example Query
```sql
SELECT country, MAX(cases) as [Max number of cases]
FROM confirmed_cases
GROUP BY country
ORDER BY [Max number of cases] DESC;
```
 ![SQL Query](https://i.imgur.com/ZoK3k6f.png "SQL Query")

## Visualization
![Metabase dashboard](https://i.imgur.com/BmEhmJq.png "Metabase dashboard")