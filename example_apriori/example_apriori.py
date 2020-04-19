import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori 
excel_file = 'testingpa.xls'
print(np.array(movies))
df=pd.DataFrame(np.array(movies),columns=['cocacola', 'chips', 'chiken','tissue','bun','chocolate'])
records = []  
for i in range(0, 6):  
    records.append([str(movies.values[i,j]) for j in range(0, 6)])

association_rules = apriori(records, min_support=1, min_confidence=1)  
association_results = list(association_rules)
#print(association_results)
for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    if(len(pair)>1):
     items = [x for x in pair]
     print("Rule: " + items[0] + " -> " + items[1])
    else:
     items = [x for x in pair]
     print("Rule: " + items[0] )
    
    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
