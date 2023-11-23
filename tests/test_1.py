from df_in_browser import show_df
import pandas as pd
import numpy as np

def test_1():
    # create dataframe
    df = pd.DataFrame({'score': np.random.normal(100, 10, 100),
                    'name': np.repeat('name', 100)})

    # test with a DataFrame
    show_df(df)

    # test with a Series
    show_df(df['score'])