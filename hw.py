import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stats

data = pd.read_csv('Titanic Dataset.csv')
###meadian of SibSp###

median_sibsp = np.median(data['SibSp'])
print(median_sibsp)

mean_sibsp = np.mean(data['SibSp'])
print(mean_sibsp)

mode_sibsp = stats.mode(data['SibSp'])
print(mode_sibsp)