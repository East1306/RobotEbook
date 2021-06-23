#!/usr/bin/env python3

import rvcprint
import numpy as np
import matplotlib.pyplot as plt


import runpy

# TODO refactor this
dict = runpy.run_path("rvc5_2.py")
g = globals()
for key in ['bd', 'sim']:
    g[key] = dict[key]

# Simulate the model
sim.options.animation = False
sim.options.graphics = True
out = sim.run(bd, T=150, dt=0.2)

# make fig 1 current
plt.figure(1)
plt.title('')  # remove the title

rvcprint.rvcprint()

