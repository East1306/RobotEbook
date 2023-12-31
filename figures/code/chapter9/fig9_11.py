#!/usr/bin/env python3

import matplotlib.pyplot as plt
from RVC3.tools import rvcprint

import bdsim

import vloop_test
vloop_test.sim.set_options(hold=False)

vloop_test.bd['disturbance'].set_param('value', 40/107.815)
out = vloop_test.sim.run(vloop_test.bd, 1, dt=1e-3, watch=["demand[0]", "VLOOP/out[0]"])


plt.plot(out.t, out.y0, 'r', label='demand')
plt.plot(out.t, out.y1, 'b', label='actual')
plt.grid(True)
plt.xlim(0, 0.6)
plt.ylim(-5, 55)

plt.legend()
plt.ylabel(r'$\mathbf{\omega}\, (\mathrm{rad\, s^{-1}})$')
plt.xlabel('Time (s)')

rvcprint.rvcprint()