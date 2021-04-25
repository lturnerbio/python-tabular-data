#! /usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats


dataframe = pd.read_csv("iris.csv")

def regression(df):

    """
    Module to regress petal length against sepal length for our includedIris dataset.
    Parameters
    ----------
    df: dataframe
        The dataframe containing the data we are looking for. Must have "petal_length_cm" and "seapl_length_cm" columns.
    Returns
    ----------
    regression
        The regression object which contains the slope and intercept of our regression, and other regression parameters.
    Example
    -----------
    >>> regression(versicolor)
    regression
    """

#if __name__ == '__main__':
#    regression = regression(df)


"""
This first section should define the versicolor sub dataset only

Figure should be created after running regression
"""


versicolor = dataframe[dataframe.species == 'Iris_versicolor']
versicolor_x = versicolor.petal_length_cm
versicolor_y = versicolor.sepal_length_cm
regression_versicolor = stats.linregress(versicolor_x, versicolor_y)
versicolor_slope = regression_versicolor.slope
#versicolor_intercept = regression.intercept
plt.scatter(versicolor_x, versicolor_y, label = 'Data')
plt.plot(versicolor_x, versicolor_slope * versicolor_x + regression_versicolor, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress_versicolor.png")


"""
This section should define the virginica sub dataset

Figure should be created after running resgression and should only have values from the virginica sub dataset
"""

virginica = dataframe[dataframe.species == 'Iris_virginica']
virginica_x = virginica.petal_length_cm
virginica_y = virginica.sepal_length_cm
regression_virginica = stats.linregress(virginica_x, virginica_y)
virginica_slope = regression_virginica.slope
#intercept = regression.intercept
plt.scatter(virginica_x, virginica_y, label = 'Data')
plt.plot(virginica_x, virginica_slope * virginica_x + regression_virginica, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress_virginica.png")


"""
This last section should define the setosa sub dataset

Figure should be created after running regression and should only have values from the setosa sub dataset
"""

setosa = dataframe[dataframe.species == 'Iris_setosa']
setosa_x = setosa.petal_length_cm
setosa_y = setosa.sepal_length_cm
regression_setosa = stats.linregress(setosa_x, setosa_y)
setosa_slope = regression_setosa.slope
#intercept = regression.intercept
plt.scatter(setosa_x, setosa_y, label = 'Data')
plt.plot(setosa_x, setosa_slope * setosa_x + regression_setosa, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress_setosa.png")


