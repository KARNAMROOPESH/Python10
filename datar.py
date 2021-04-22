import pandas as pd
import numpy as np


coffes = pd.read_csv('./coffe.csv')
coffel = np.array(coffes['Coffee in ml'])
sleepl = np.array(coffes['sleep in hours'])
c = np.corrcoef(coffel , sleepl)
print(c)


mark = pd.read_csv('./marks.csv')
marks = np.array(mark['Marks In Percentage'])
days = np.array(mark['Days Present'])
c1 = np.corrcoef(marks , days)
print(c1)

tv = pd.read_csv('./tv.csv')
tvs = np.array(tv['Size of TV'])
hrs = np.array(tv['	Average time spent watching TV in a week (hours)'])
c2 = np.corrcoef(tvs , hrs)
print(c2)