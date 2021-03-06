'''
CLASS: Getting Data from APIs

Exercise 1 - retrieving US Census language use data

'''
# Link to the Census Bureau language stats API description page

# Look through the API description links and examples to see what use you have avaialble

# Use the requests library to interact with a URL

import requests
# Use a URL example in a browser to see the result returned and the use request to access with python
# http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625')

# modify the request to get languges 625 through 650 so we can see a larger sample of what is returned from the request
# Hint the syntax for more than one language number is similar to one we use for multiple elements in a list


# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# Convert to jason()
r.json()

# 
#look at the contents of the output of the jason() method.  It looks like it can easily become a list of lists

# Convert the jason() method output into a dataframe with the first list as the column header and the rest as rows of data
import pandas as pd
data = pd.DataFrame(r.json()[1:])
data.columns = r.json()[0]
# Sort the dataframe decending by the number of people speaking the language
# Check the data type of 'EST', the number of people that speak the language
data['EST']=data.EST.convert_objects(convert_numeric=True)
data.sort(['EST'], ascending = False)

# Now create a new request that brings in the stats for all the us and primary languages
# See the websites links for syntax for us and range of language nunbers
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=us&LAN=601:999')

data2=pd.DataFrame(r.json()[1:])
### Bonus
# Create a loop that will collect the counts of Spanish language speakers by state
stringnum=[]
for num in range (1,81):
    stringnum.append(str(num))

for i,value in enumerate(stringnum):
    if len(value)==1:
         value2='0' + value
         stringnum[i] = value.replace(value, value2)


r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625')