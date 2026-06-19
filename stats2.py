import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

###IMport Dataset###

data = pd.read_csv('Titanic Dataset.csv')
data.head()

###**Meadiam Value Of Age and Fare**"""

median_age = np.median(data['Age'])
print('median age of passengers is -',median_age)


median_fare = np.median(data['Fare'])
print('median_fare of passengers is -',median_fare)

###mode values of age and PClass###

mode_age = stats.mode(data['Age'])
print('mode value of age -',mode_age)

mode_class = stats.mode(data['Pclass'])
print('mode value of PCLass -',mode_class)

###mode value of catagroical feature###

mode_gender = data['Gender'].value_counts().index[0]
print('mode of feature gender -',mode_gender)