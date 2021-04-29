import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
from io import StringIO
import numpy as np


def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def plot_graph(T, Last):

    fig, ax = plt.subplots()

    try:
        #plt.plot(T, Last)
        Last.plot()
    except Exception as e:
        print("Error plotting graph")

    # Formatting the xaxis - Dates
    locator = mdates.AutoDateLocator(maxticks=8)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    
    # Formatting the yaxis - $$ 
    ax.yaxis.set_major_formatter('${x:,.2f}')
    ax.yaxis.set_tick_params(which='major', labelcolor='green',
                         labelleft=True, labelright=False)
   
    #graph = mpld3.fig_to_html(fig)
    #return graph


    imgdata = StringIO()
    fig.savefig(imgdata, format='svg', bbox_inches="tight")
    imgdata.seek(0)

    graph = imgdata.getvalue()
    return graph
    
