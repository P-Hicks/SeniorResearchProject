import numpy as np
from sklearn.linear_model import LinearRegression
from notebook_utils.dataframes import get_stats_df
import scipy.stats as stats


def pearsons_correlation(x, y):

    correlation_coefficient, p_value = stats.pearsonr(x, y)

    print("Correlation coefficient:", correlation_coefficient)
    print("P-value:", p_value)
