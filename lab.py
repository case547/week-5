import pandas as pd
import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect("./Comp2Sample.sqlite")
cur = conn.cursor()

# View content
df = pd.read_sql_query("SELECT * FROM CONTRIBUTORS", conn)
print(df)

# Print amount from each contributor
da = pd.read_sql_query("SELECT id FROM contributors", conn)
print(da)

# Show histogram of data
n, bins, patches = plt.hist(x=df.amount, bins=15)
plt.show()

# Find biggest contribution
da = pd.read_sql_query("SELECT MAX(amount) FROM contributors;", conn)
print(da)

# Show number of contributions
dc = pd.read_sql_query("SELECT count(amount) FROM contributors;", conn)
print(dc)

# Find number of contributors who gave more than 200
dcrich = pd.read_sql_query("SELECT count(amount) FROM contributors WHERE amount > 200;", conn)
print(dcrich)

# Find number of distinct postcodes
dczip = pd.read_sql_query("SELECT count(DISTINCT zip) FROM contributors;", conn)
print(dczip)

# Close the database
conn.close()