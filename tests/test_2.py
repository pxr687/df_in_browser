# tests of matplotlib-to-browser function(s)
from show_in_browser import show_plt_plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_plt_plot():
    # create dataframe
    df = pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                    'score_2': np.random.normal(1000, 2, 100),
                    'name': np.repeat(['A', 'B'], 50)})
    # create 2D scatterplot to show in browser
    plt.figure()
    plt.scatter(df['score_1'], df['score_2'])
    show_plt_plot()

def test_plt_plot_3D():
    # create dataframe
    df = pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                    'score_2': np.random.normal(1000, 2, 100),
                    'score_3': np.random.normal(10, 2, 100)})
    # create 3D scatterplot to show in browser
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['score_1'], df['score_2'], df['score_3'])
    show_plt_plot()

def test_plt_plot_3D_interact():
    # create dataframe
    df = pd.DataFrame({'score_1': np.random.normal(100, 10, 100),
                    'score_2': np.random.normal(1000, 2, 100),
                    'score_3': np.random.normal(10, 2, 100)})
    # create 3D scatterplot to interact with in browser
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['score_1'], df['score_2'], df['score_3'])
    show_plt_plot(interact=True)

if __name__ == "__main__":
    test_plt_plot()
    test_plt_plot_3D()  
    test_plt_plot_3D_interact()