# df_in_browser

A simple python package to display a pandas dataframe in a browser. It is
intended to be run from the command line, for better visualisation of 
dataframes than viewing within the terminal.

Usage (in an ipython session):

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

# show a Series derived from the DataFrame in a browser
show_df(df['score_1'])
```
This will give you output of the following form, in your default browser:

![alt_text](https://github.com/pxr687/df_in_browser/blob/072d53b753f33392d6e40178161cda1405b41fcf/example.png)

<br>

And, for the second tab:
![alt_text](https://github.com/pxr687/df_in_browser/blob/a083ddc3d88650268d79edbf9fe438bd736f891c/example_2.png)
