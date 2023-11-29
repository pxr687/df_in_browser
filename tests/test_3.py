# tests of plotly-to-browser function(s)
from show_in_browser import show_px_plot
import pandas as pd
import numpy as np
import plotly.express as px

def test_px_plot():
    df = pd.DataFrame({'x': np.random.normal(100, 10, 20),
                        'y': np.random.normal(100, 10, 20)})

    fig = px.scatter(df, x='x', y='y')

    show_px_plot(fig)