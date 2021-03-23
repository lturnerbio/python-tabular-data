#! /usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats
if __name__ == '__main__'

dataframe = pd.read_csv("iris.csv")



versicolor = dataframe[dataframe.species = 'Iris_versicolor']

virginica = dataframe[dataframe.species = 'Iris_virginica']

setosa = dataframe[dataframe.species = 'Iris_setosa']

