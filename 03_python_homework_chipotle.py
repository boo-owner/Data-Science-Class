'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
import csv
with open('chipotle.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    file_nested_list=[]
    for row in f_tsv:
        file_nested_list.append(row)

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

header = file_nested_list[0]
data = file_nested_list[1:]
print data[0:5]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps and then code each step
'''
print len(file_nested_list)

#Remove dollar signs from prices
from copy import deepcopy

data2=deepcopy(data)
for X in data2:
    if '$' in X[4]:
        for Y in X:
            if Y==X[4]:
                new_element=''
                for Z in Y: 
                    if Z!='$':
                        new_element=new_element+Z
                X[4]=new_element            

print data[0:10]
print data2[0:10]

order_num=''
order_cost_lista=[]
order_cost_listb=[]
for X in data2:
    if order_num!=X[0]:
        order_num=X[0]
        total_item_cost=float(X[1])*float(X[4])
        order_cost_lista=[]
        order_cost_lista.append(order_num)
        order_cost_lista.append(total_item_cost)
        order_cost_listb.append(order_cost_lista)
    else:
        total_item_cost=float(X[1])*float(X[4])
        order_cost_lista[-1]=order_cost_lista[-1]+total_item_cost
        order_cost_listb[-1]=order_cost_lista

#print order_cost_listb  

total_cost=0
for X in order_cost_listb:
    total_cost=total_cost+X[1]

print total_cost 
avg_cost=total_cost/1834
print avg_cost  

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

list_soda = []
for X in data:
    if (X[2]=='Canned Soda') or (X[2]=='Canned Soft Drink'):
        if X[3] not in list_soda:
            list_soda.append(X[3])

print list_soda      
                
'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
#create list with burrito toppings only
toppings=[]
for X in data:
    if 'Burrito' in X[2]:
        toppings.append(X[3])

#Remove commas so that we can count elements in list        
toppings2=[]
for X in range(0,len(toppings)):
    toppings2.append(toppings[X].split(','))

#create list with number of toppings as each element, also tally total number of toppings
count3=0       
count2=[]
for X in toppings2:
    count=len(X)
    count2.append(count)
    count3=count3+count

#average toppings equals total number of toppings divided by number of burritos
avg_toppings=count3/len(count2)

print toppings2[0:10]
print count2[0:10]
print avg_toppings
'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

dictionary = {}
for X in data2:
    if 'Chips' in X[2]:
        if X[2] not in dictionary:
            dictionary[X[2]]=float(X[1])
        else:
            dictionary[X[2]]=dictionary[X[2]]+float(X[1]) 
print dictionary

# with defaultdict
from collections import defaultdict
dictionary = defaultdict(int)
for X in data2:
    if 'Chips' in X[2]:
        if dictionary[X[2]]==0:
            dictionary[X[2]]=float(X[1])
        else:
            dictionary[X[2]]=dictionary[X[2]]+float(X[1])

print dictionary
'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
#do customers like black beans or pinto beans better with their burritos, tacos or bowls?
#create list with burrito, tacos and bowl toppings only
toppings=[]
for X in data:
    if ('Burrito' in X[2]) or ('Bowl' in X[2]) or ('Tacos' in X[2]):
        toppings.append(X[3])

print toppings
#Remove commas so that we can count elements in list        
toppings2=[]
for X in range(0,len(toppings)):
    toppings2.append(toppings[X].split(','))
print toppings2

count_pinto=0
count_black=0

for X in toppings2:
    for Y in X:
        if 'Pinto Beans' in Y:
            count_pinto=count_pinto+1
        if 'Black Beans' in Y:
            count_black=count_black+1

print count_pinto
print count_black

# black beans are more popular