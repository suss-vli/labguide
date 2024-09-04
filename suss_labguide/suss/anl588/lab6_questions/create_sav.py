import pyreadstat

# Read the original .sav file
df, meta = pyreadstat.read_sav('test_prisons.sav')

# Modify the dataframe as needed
modified_df = df.iloc[:101]  # Keep only the first 101 rows, for example

# Write the modified dataframe to a new .sav file
pyreadstat.write_sav(modified_df, 'test_case.sav')
