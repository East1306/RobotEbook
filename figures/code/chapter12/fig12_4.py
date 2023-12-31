#!/usr/bin/env python3

from RVC3.tools import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *
from matplotlib.ticker import ScalarFormatter
from matplotlib import cm

castle = Image.Read('castle2.png', dtype='float')

castle.adaptive_threshold(h=15).disp()
rvcprint.rvcprint()

