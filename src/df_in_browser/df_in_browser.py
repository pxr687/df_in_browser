import pandas as pd
import webbrowser
import os
from time import sleep

def show_df(df, name='temp', delete=True):
    """Show a pandas dataframe in browser, from command line.

    Parameters
    ----------
    df : pandas DataFrame (can also be a Series)
        The DataFrame (or Series) to be displayed in the browser.

    name : str
        The name of the temporary HTML file generated (contains the information
        from the dataframe)

    delete : Bool
        Boolean indicating whether to delete the temporary HTML file after
        it is shown in the browser. Default is True.    
    """
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