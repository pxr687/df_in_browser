import pandas as _pd
import webbrowser as _webbrowser
import os as _os
from time import sleep
import matplotlib as _mpl
import matplotlib.pyplot as _plt
import aspose.words as _aw

def show_df(df, name='temp', delete=True, delete_pause=0.7):
    """Show a pandas dataframe in the default browser, from the command line.

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
        what information is shown on the dataframe in that tab. Note: the name
        supplied does NOT need a file extension.

    delete : Bool
        Boolean indicating whether to delete the temporary HTML file after
        it is shown in the browser. Default is True.    

    delete_pause : Bool
        Number indicate how long to wait before deleting the temporary HTML file.
        You may want to change this if your browser is taking a long time
        to open the file (e.g. so it is getting deleted before it is shown).
        Default is 0.7 seconds.   
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
        sleep(delete_pause)
        _os.remove(name+'.html')


def show_plt_plot(name="temp_plot", delete=True, delete_pause=0.7,
                  interact=False):
    """Show a matplotlib.pyplot plot in the default browser, from the command
     line.

    Parameters
    ----------

    name : str
        The name of the temporary HTML file generated (which contains the 
        plot). Note: the name supplied does NOT need a file extension.

    delete : Bool
        Boolean indicating whether to delete the temporary HTML file after
        it is shown in the browser. Default is True.    
        
    delete_pause : Bool
        Number indicate how long to wait before deleting the temporary HTML file.
        You may want to change this if your browser is taking a long time
        to open the file (e.g. so it is getting deleted before it is shown).
        Default is 0.7 seconds.   
    """
    if interact == True:
        original_mpl_backend = _plt.get_backend()
        _mpl.use('WebAgg')
        _plt.show()
        _mpl.use(original_mpl_backend)

    if interact == False:
        name_png = name+".png"
        name_html = name+".html"
        _plt.savefig(name_png)
        doc = _aw.Document()
        builder = _aw.DocumentBuilder(doc)
        builder.insert_image(name_png)
        doc.save(name_html)
        _webbrowser.open(name_html)

        # delete the temporary file (after a pause to allow display in browser)
        if delete == True:
            sleep(delete_pause)
            _os.remove(name_png)
            _os.remove(name_html)

def show_px_plot(fig, name="temp_plot", delete=True, delete_pause=0.7):
    """Show a plotly.express plot in the default browser, from the command line.

    Parameters
    ----------
    fig: plotly.graph_objs._figure.Figure
        The plotly graph object which you want to open in a browser.

    name : str
        The name of the temporary HTML file generated (which contains the 
        plot). Note: the name supplied does NOT need a file extension.

    delete : Bool
        Boolean indicating whether to delete the temporary HTML file after
        it is shown in the browser. Default is True.    
        
    delete_pause : Bool
        Number indicate how long to wait before deleting the temporary HTML file.
        You may want to change this if your browser is taking a long time
        to open the file (e.g. so it is getting deleted before it is shown).
        Default is 0.7 seconds.   
    """
    name_html = name+".html"
    fig.write_html(name_html)
    _webbrowser.open(name_html)

    # delete the temporary file (after a pause to allow display in browser)
    if delete == True:
        sleep(delete_pause)
        _os.remove(name_html)