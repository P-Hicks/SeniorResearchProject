import numpy as np
from sklearn.linear_model import LinearRegression
from notebook_utils.dataframes import get_stats_df
import scipy.stats as stats


def run_linear_regression(df, x_df, y_df):

    x = x_df.to_numpy().reshape((-1, 1))
    y = y_df.to_numpy()

    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)
    # print(f"coefficient of determination (r^2): {r_sq}")
    # print(f"intercept: {model.intercept_}")
    # print(f"slope: {model.coef_}")
    return r_sq, model.coef_, model.intercept_

