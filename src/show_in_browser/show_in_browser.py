import pandas as _pd
import webbrowser as _webbrowser
import _os
from time import sleep
import matplotlib.pyplot as _plt
import aspose.words as _aw

def show_df(df, name='temp', delete=True):
    """Show a pandas dataframe in browser, from command line.

    Parameters
    ----------
    df : pandas DataFrame (can also be a Series)
        The DataFrame (or Series) to be displayed in the browser.

    name : str
        The name of the temporary HTML file generated (which contains the 
        information from the dataframe). This is useful for keeping track of 
        what the dataframe shows if you are opening multiple tabs showing
        different dataframes. In most browsers the name of the temporary file
        will be displayed on the tab that displays that particular dataframe.
        You may want to use names like "control_group" etc. to make it clearer
        what information is shown on the dataframe in that tab. 

    delete : Bool
        Boolean indicating whether to delete the temporary HTML file after
        it is shown in the browser. Default is True.    
    """
    # coerce input to dataframe (user may often want to use it on a
    # pandas series e.g. the output of groupby etc.)
    df = _pd.DataFrame(df)

    # convert the dataframe to HTML
    html_df = df.to_html()

    # write a temporary HTML file
    with open(name+'.html', 'w') as file:
        file.write(html_df)

    # display the dataframe in browswer
    _webbrowser.open(file.name)

    # delete the temporary file (after a pause to allow display in browser)
    if delete == True:
        sleep(0.5)
        _os.remove(name+'.html')


def show_plot(name="temp_plot.png"):
    _plt.savefig(name)

