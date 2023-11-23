from df_in_browser import show_df
import pandas as pd
import numpy as np

def test_1():
    # create dataframe
    df = pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                    'score_2': np.random.normal(1000, 2, 100),
                    'name': np.repeat(['A', 'B'], 50)})

    # test with a DataFrame
    show_df(df)

    # test with a Series
    show_df(df.groupby('name').mean())