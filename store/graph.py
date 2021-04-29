import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
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

    #fig = plt.figure()

    fig, ax = plt.subplots()

    try:
        #plt.plot(T, Last)
        Last.plot()
    except Exception as e:
        print("Error plotting graph")

    #fmt = '${x:, .0f}'
    #tick = mtick.StrMethodFormatter(fmt)
    #ax.yaxis.set_major_formatter(tick)
    ax.yaxis.set_major_formatter('${x:1.2f}')
    #plt.xticks(rotate=25)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    graph = imgdata.getvalue()
    return graph
    
