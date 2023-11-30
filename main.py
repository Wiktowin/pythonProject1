import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# your data string
data_string = data_string = """2013-11-26,26,November,2013,19,Youth (<25),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,8,45,120,590,360,950
2015-11-26,26,November,2015,19,Youth (<25),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,8,45,120,590,360,950
2014-03-23,23,March,2014,49,Adults (35-64),M,Australia,New South Wales,Accessories,Bike Racks,Hitch Rack - 4-Bike,23,45,120,1366,1035,2401
2016-03-23,23,March,2016,49,Adults (35-64),M,Australia,New South Wales,Accessories,Bike Racks,Hitch Rack - 4-Bike,20,45,120,1188,900,2088
2014-05-15,15,May,2014,47,Adults (35-64),F,Australia,New South Wales,Accessories,Bike Racks,Hitch Rack - 4-Bike,4,45,120,238,180,418
2016-05-15,15,May,2016,47,Adults (35-64),F,Australia,New South Wales,Accessories,Bike Racks,Hitch Rack - 4-Bike,5,45,120,297,225,522
2014-05-22,22,May,2014,47,Adults (35-64),F,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,4,45,120,199,180,379
2016-05-22,22,May,2016,47,Adults (35-64),F,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,2,45,120,100,90,190
2014-02-22,22,February,2014,35,Adults (35-64),M,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,22,45,120,1096,990,2086
2016-02-22,22,February,2016,35,Adults (35-64),M,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,21,45,120,1046,945,1991
2013-07-30,30,July,2013,32,Young Adults (25-34),F,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,8,45,120,398,360,758
2015-07-30,30,July,2015,32,Young Adults (25-34),F,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,8,45,120,398,360,758
2013-07-15,15,July,2013,34,Young Adults (25-34),M,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,7,45,120,349,315,664
2015-07-15,15,July,2015,34,Young Adults (25-34),M,Australia,Victoria,Accessories,Bike Racks,Hitch Rack - 4-Bike,7,45,120,349,315,664
2013-08-02,2,August,2013,29,Young Adults (25-34),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,5,45,120,369,225,594
2015-08-02,2,August,2015,29,Young Adults (25-34),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,7,45,120,517,315,832
2013-09-02,2,September,2013,29,Young Adults (25-34),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,2,45,120,148,90,238
2015-09-02,2,September,2015,29,Young Adults (25-34),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,1,45,120,74,45,119
2014-01-22,22,January,2014,29,Young Adults (25-34),M,Canada,British Columbia,Accessories,Bike Racks,Hitch Rack - 4-Bike,1,45,120,74,45,119"""

# Create a DataFrame from the string
data = pd.read_csv(StringIO(data_string), header=None)

# Rename columns for clarity
data.columns = ["Date", "Day", "Month", "Year", "Age", "Category", "Gender", "Country", "State", "Product_Type", "Produkt", "Sub_Category", "Quantity", "Unit_Cost", "Unit_Price", "Profit", "Costs", "Revenue"]

# Convert date format
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')

# Visualize data (e.g., revenue by product category)
plt.figure(figsize=(12, 6))
sns.barplot(x='Product_Type', y='Revenue', data=data)
plt.title('Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Revenue')
plt.show()

