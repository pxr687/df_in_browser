import pandas as pd
import webbrowser
import os
from time import sleep

def show_df(df, name='temp', delete=True):
    """Show a pandas dataframe in browser, from command line."""
    # coerce input to dataframe (user may often want to use it on a
    # pandas series e.g. the output of groupby etc.)
    df = pd.DataFrame(df)

    # convert the dataframe to HTML
    html_df = df.to_html()

    # write a temporary HTML file
    with open(name+'.html', 'w') as file:
        file.write(html_df)

    # display the dataframe in browswer
    webbrowser.open(file.name)

    # delete the temporary file (after a pause to allow display in browser)
    if delete == True:
        sleep(2)
        os.remove(name+'.html')