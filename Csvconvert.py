# import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("data.csv")

# Convert the DataFrame to a JSON file
df.to_json("data.json", orient='records')

# Convert the DataFrame to a Excel file
df.to_excel("data.xlsx", engine='xlsxwriter')

# Convert the DataFrame to a pickle file
df.to_pickle("data.pkl")

# Convert the DataFrame to a CSV file
df.to_csv("data.csv")

