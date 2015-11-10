# Chipotle Command Line Homework
## November 3, 2015
## Fannie Tseng


**1. Code to arrive at answers **
Note: I cloned the Dat1 and Dat8 repos onto my machine — was there a better way to do this?

head chipotle.tv    

tail chipotle.tsv    

wc chipotle.tsv     

grep "Steak Burrito" chipotle.tsv|wc    

grep "Chicken Burrito" chipotle.tsv|wc  

grep “Chicken Burrito" chipotle.tsv| grep "Black Beans" | wc  

grep “Chicken Burrito" chipotle.tsv| grep "Pinto Beans" | wc  

find . -name ‘*.tsv’  

find . -name ‘*.csv’  
grep -r -i dictionary . | wc -l  




**2. Answers to questions**
i. Each column is a variable that each describes a different element of customer orders. Each row represents unique item(s) that are being ordered. 

ii. There appear to be 1,834 orders in the dataset.

iii. There are 4,623 lines in the dataset.

iv. It looks like the chicken burrito is more popular, because the chicken burrito appears more as lines in the file. However, I am not entirely sure, because of the quantity variable. I didn’t know how to create a sum of the quantities in the command line; it is possible that the quantity of steak burritos ordered was higher.

v.  Chicken burritos more often have black beans — black beans were ordered 282 times with chicken burritos and 105 times with pinto beans.

vi. **Note: I needed to do this with two commands:**

find . -name ‘*.tsv’

./chipotle.tsv

./sms.tsv

find . -name ‘*.csv’

./airlines.csv
./bank-additional.csv
./bikeshare.csv
./drinks.csv
./hitters.csv
./imdb_1000.csv
./titanic.csv
./ufo.csv
./vehicles_test.csv
./vehicles_train.csv
./yelp.csv

vii. There were 84 occurrences of the word “dictionary” in the DAT8 repo.

