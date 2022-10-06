import pandas as pd
from datetime import date

# read the file in and covert the birthdate column to a datetime
df = pd.read_csv('vanco.csv', parse_dates=['birthdate'])

# function
def calc_age(bd: pd.Series) -> pd.Series:
    today = pd.to_datetime(date.today())  # convert today to a pandas datetime
    return (today - bd) / pd.Timedelta(days=365.25)  # divide by days to get years


# call function and assign the values to a new column in the dataframe
df['age (years)'] = calc_age(df.birthdate)
