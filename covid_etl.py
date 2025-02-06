#Importing necessary libraries
import kagglehub
import pandas as pd
import sqlite3

#Downloading latest Dataset version
path = kagglehub.dataset_download("antgoldbloom/covid19-data-from-john-hopkins-university")

#Reading the updated data with pandas
df = pd.read_csv(path+'/RAW_global_confirmed_cases.csv')

#Melting date columns, to turn them into rows instead
df_melted = df.melt(
    id_vars = ['Country/Region', 'Province/State', 'Lat', 'Long'],
    var_name = 'date',
    value_name = 'confirmed_cases'
)

#Converting dates into a standard format
df_melted['date'] = pd.to_datetime(df_melted['date'], format='%m/%d/%y', errors='coerce')

#Grouping by contries
df_country = df_melted.groupby(['Country/Region', 'date'])['confirmed_cases'].sum().reset_index()

#Deleting rows with negative values or errors
df_country = df_country[df_country['confirmed_cases'] >= 0]

#Connecting to database (SQLite)
connection = sqlite3.connect('covid_database.db')

#Creating the table
connection.execute('''
                   CREATE TABLE IF NOT EXISTS confirmed_cases (
                        country TEXT,
                        date DATE,
                        cases INTEGER
                   );
''')

#Saving the data
df_country.rename(columns={'Country/Region': 'country', 'confirmed_cases':'cases'})[['country','date','cases']].to_sql(
    'confirmed_cases',
    connection,
    if_exists='replace',
    index=False
)

connection.close()