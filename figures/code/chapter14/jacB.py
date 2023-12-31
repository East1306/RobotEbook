#!/usr/bin/env python3

import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *
from matplotlib.ticker import ScalarFormatter
from matplotlib import cm

function B = jacB(P1,P2,P3,T1,T2,T3,f,qx,qy,qz,rho,u0,v0)
#JACB
#    B = JACB(P1,P2,P3,T1,T2,T3,F,QX,QY,QZ,RHO,U0,V0)

#    This function was generated by the Symbolic Math Toolbox version 6.3.
#    02-Nov-2015 20:25:49

t2 = qy.^2
t3 = qz.^2
t4 = qx.^2
t5 = t2.*2.0
t6 = t4.*2.0
t7 = t5+t6-1.0
t8 = qx.*qz.*2.0
t9 = -t2-t3-t4+1.0
t10 = sqrt(t9)
t11 = conj(t10)
t12 = qy.*t11.*2.0
t13 = t8+t12
t14 = qy.*qz.*2.0
t17 = qx.*t11.*2.0
t15 = t14-t17
t16 = P3.*t7
t18 = T1.*t13
t19 = T2.*t15
t28 = T3.*t7
t29 = P1.*t13
t30 = P2.*t15
t20 = t16+t18+t19-t28-t29-t30
t21 = 1.0./rho
t22 = t3.*2.0
t23 = t5+t22-1.0
t24 = qx.*qy.*2.0
t25 = qz.*t11.*2.0
t26 = t24+t25
t27 = t8-t12
t31 = 1.0./t20
t32 = t20.*u0
t33 = P1.*t23
t34 = T2.*t26
t35 = T3.*t27
t40 = T1.*t23
t41 = P2.*t26
t42 = P3.*t27
t36 = t33+t34+t35-t40-t41-t42
t37 = f.*t21.*t36
t38 = t32+t37
t39 = 1.0./t20.^2
t43 = t6+t22-1.0
t44 = t24-t25
t45 = t14+t17
t46 = t20.*v0
t47 = T2.*t43
t48 = P1.*t44
t49 = P3.*t45
t52 = P2.*t43
t53 = T1.*t44
t54 = T3.*t45
t50 = t47+t48+t49-t52-t53-t54
t55 = f.*t21.*t50
t51 = t46-t55
B = reshape([-t31.*(t13.*u0-f.*t21.*t23)+t13.*t38.*t39,-t31.*(t13.*v0+f.*t21.*t44)+t13.*t39.*t51,-t31.*(t15.*u0+f.*t21.*t26)+t15.*t38.*t39,-t31.*(t15.*v0-f.*t21.*t43)+t15.*t39.*t51,t31.*(t7.*u0-f.*t21.*t27)-t7.*t38.*t39,t31.*(t7.*v0-f.*t21.*t45)-t7.*t39.*t51],[2,3])

