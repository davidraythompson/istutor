# David R. Thompson

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

from IPython.core.display import HTML
def css_styling():
    styles = open("../../python/styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

from matplotlib import rc
rc('text', usetex=False)

from IPython.core.pylabtools import figsize
figsize(11,11/1.618)
