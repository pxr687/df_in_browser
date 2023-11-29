import pandas as _pd
import webbrowser as _webbrowser
import os as _os
from time import sleep
import matplotlib as _mpl
import matplotlib.pyplot as _plt
import aspose.words as _aw

def show_df(df, name='temp', decimal_places=3, delete=True, delete_pause=0.7):
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

    decimal_places: int
        Temporarily set what how many decimal places to show numbers to. Default
        is 3.

    delete : Bool
        Boolean indicating whether to delete the temporary HTML file after
        it is shown in the browser. Default is True.    

    delete_pause : Bool
        Number indicate how long to wait before deleting the temporary HTML file.
        You may want to change this if your browser is taking a long time
        to open the file (e.g. so it is getting deleted before it is shown).
        Default is 0.7 seconds. 

    Example
    ----------

    from show_in_browser import show_df
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # create dataframe
    df = pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                    'score_2': np.random.normal(1000, 2, 100),
                    'name': np.repeat(['A', 'B'], 50)})

    # show the dataframe in browser
    show_df(df)
    """
    # coerce input to dataframe (user may often want to use it on a
    # pandas series e.g. the output of groupby etc.)
    df = _pd.DataFrame(df)

    # use a specific number of decimal places for display, without altering 
    # data
    with _pd.option_context('display.precision', decimal_places):

        # convert the dataframe to HTML
        html_df = df.to_html()

        # write a temporary HTML file
        with open(name+'.html', 'w') as file:
            file.write(html_df)

        # display the dataframe in browswer
        _webbrowser.get().open('file://' + _os.path.realpath(name+'.html'))

        # delete the temporary file (after a pause to allow display in browser)
        if delete == True:
            sleep(delete_pause)
            _os.remove(_os.path.realpath(name+'.html'))


def show_plt_plot(name="temp_plot", delete=True, delete_pause=0.7,
                  interact=False):
    """Show a matplotlib.pyplot plot in the default browser, from the command
     line.

     Works like plt.show() - run it after your plotting commands.

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

    Example
    ----------
    from show_in_browser import show_plt_plot
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # create dataframe
    df = pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                       'score_2': np.random.normal(1000, 2, 100),
                       'score_3': np.random.normal(10, 2, 100)})

    # create 3D scatterplot to show in browser
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(df['score_1'], df['score_2'], df['score_3'])

    # show in browser
    show_plt_plot()  
    """
    # if the plot is interactive (e.g. a 3D scatterplot)...
    if interact == True:

        # close previous figures to avoid errors
        _plt.close()

        # get a record of the current matplotlib backend
        original_mpl_backend = _plt.get_backend()

        # switch the backend to WebAgg, allowing plot interaction in a browser
        _mpl.use('WebAgg')

        # show the plot
        _plt.show()

        # restore original backend setting
        _mpl.use(original_mpl_backend)
    
    # if the plot is NOT interactive...
    if interact == False:
        
        # store some filenames (png and html)
        name_png = name+".png"
        name_html = name+".html"

        # sometimes aspose-words creates a junk file like "temp_plot.001.png",
        # store its name as a string so it can be deleted
        junk_name = name+".001.png" 

        # save the current figure
        _plt.savefig(name_png)

        # create a temporary html file containing the figure
        doc = _aw.Document()
        _aw.DocumentBuilder(doc).insert_image(_os.path.realpath(name_png))
        doc.save(name_html)

        # open the temporary html file, then close the matplotlib figure (to
        # avoid errors)
        _webbrowser.get().open('file://' + _os.path.realpath(name_html))
        _plt.close()

        # delete the temporary file (after a pause to allow display in browser)
        if delete == True:
            sleep(delete_pause)
            _os.remove(_os.path.realpath(name_png))
            _os.remove(_os.path.realpath(name_html))
            if junk_name in _os.listdir():
                # if aspose-words created a junk file, delete it
                _os.remove(_os.path.realpath(junk_name)) 

def show_px_plot(fig, name="temp_plot", delete=True, delete_pause=0.7):
    """Show a plotly.express plot in the default browser, from the command line.

    Works like plt.show() - run it after your plotting commands.

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

    Example
    ----------
    from show_in_browser import show_px_plot
    import pandas as pd
    import numpy as np
    import plotly.express as px
    # create a dataframe
    df = pd.DataFrame({'x': np.random.normal(100, 10, 20),
                        'y': np.random.normal(100, 10, 20)})
                        
    # create a plotly graph
    fig = px.scatter(df, x='x', y='y')

    # show the graph in browser
    show_px_plot(fig)  
    """
    # write a temporary html file and open it in the browser
    name_html = name+".html"
    fig.write_html(name_html)
    _webbrowser.get().open('file://' + _os.path.realpath(name_html))

    # delete the temporary file (after a pause to allow display in browser)
    if delete == True:
        sleep(delete_pause)
        _os.remove(_os.path.realpath(name_html))