# David R. Thompson

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

from IPython.core.display import HTML
def css_styling():
    styles = open("data/custom.css", "r").read()
    return HTML(styles)
css_styling()

from matplotlib import rc
rc('text', usetex=False)

from IPython.core.pylabtools import figsize
figsize(9,9/1.618)
