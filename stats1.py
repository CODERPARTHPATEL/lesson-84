import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

###Import dataset###

data = pd.read_csv('Titanic Dataset.csv')
data.head()

###**Mean Value Of Age and Fare**"""

mean_age = np.mean(data['Age'])
print('mean age of passengers is -',mean_age)

mean_fares = np.mean(data['Fare'])
print('mean_fares is -',mean_fares)