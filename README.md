# df_in_browser

A simple python package to display a pandas dataframe in the browser. It is
intended to be run from the command line, for better visualisation of 
dataframes than viewing within the terminal.

Usage:

```
from df_in_browser import show_df
import pandas as pd
import numpy as np

# create dataframe
df =  pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                    'score_2': np.random.normal(1000, 2, 100),
                    'name': np.repeat(['A', 'B'], 50)})

# show a DataFrame in a browser
show_df(df)

# show a Series derived from the dataframe in a browser
show_df(df['score'])
```
