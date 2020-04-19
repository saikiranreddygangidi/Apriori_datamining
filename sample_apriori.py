

import pandas as pd
import numpy as np
from apyori import apriori 
data = pd.read_excel('path_of_excel_file')
df=pd.DataFrame(np.array(data),columns=['list_of_column_names'])
records = []
shape=df.shape()
for i in range(0, shape[0]):  
    records.append([str(data.values[i,j]) for j in range(0, shape[1])])
print(records)
association_rules = apriori(records, min_support=1, min_confidence=1)  
association_results = list(association_rules)
for items in association_results:
    # first index of the inner list Contains base item and add item
    pair = items[0]
    item = [x for x in pair]
    if(len(pair)>1):
     print("Rule: " + items[0] + " -> " + items[1])
    else:
     print("Rule: " + items[0] )
    #second index of the inner list
    print("Support: " + str(item[1]))
    #third index of the list located at 0th of the third index of the inner list
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    