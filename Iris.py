#! /usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats


dataframe = pd.read_csv("iris.csv")

"""
 This first section should define the versicolor sub dataset only

Figure should be created after running regression
"""

versicolor = dataframe[dataframe.species == 'Iris_versicolor']
x = versicolor.petal_length_cm
y = versicolor.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress_versicolor.png")


"""
This section should define the virginica sub dataset

Figure should be created after running resgression and should only have values from the virginica sub dataset
"""

virginica = dataframe[dataframe.species == 'Iris_virginica']
x = virginica.petal_length_cm
y = virginica.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress_virginica.png")


"""
This last section should define the setosa sub dataset

Figure should be created after running regression and should only have values from the setosa sub dataset
"""

setosa = dataframe[dataframe.species == 'Iris_setosa']
x = setosa.petal_length_cm
y = setosa.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress_setosa.png")
