import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


"""
        The function to draw  count of x and divide x according to hue parameter 
        Parameters:
            data: dataframe 
            string (x): the column from dataset on x axis.
            string (hue):the column from dataset should be used for colour encoding.   .
            string (labels): the labels in legend express on hue parameter .
            string (titles): the titles graphs.  
            palette :optional parameter color of graph
   """
def draw_hist(data,x,hue,labels,titles,shape,palette=None):
    g=sb.histplot(x=x,data=data,hue=hue,multiple=shape, palette = palette)
    plt.legend(title=titles, labels=labels)
    plt.show(g)
