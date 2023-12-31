#!/usr/bin/env python3

import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *
from matplotlib.ticker import ScalarFormatter
from matplotlib import cm

function [uv,A,B] = cameraModel(T1,T2,T3,qx,qy,qz,P1,P2,P3,f,rhox,rhoy,u0,v0)
#CAMERAMODEL
#    [UV,A,B] = CAMERAMODEL(T1,T2,T3,QX,QY,QZ,P1,P2,P3,F,RHOX,RHOY,U0,V0)

#    This function was generated by the Symbolic Math Toolbox version 6.3.
#    04-Nov-2015 15:51:31

t2 = qx.^2
t3 = t2.*2.0
t4 = qy.^2
t5 = t4.*2.0
t6 = t3+t5-1.0
t7 = qz.^2
t8 = -t2-t4-t7+1.0
t9 = sqrt(t8)
t10 = conj(t9)
t11 = qx.*qz.*2.0
t12 = qy.*t10.*2.0
t13 = t11+t12
t14 = qy.*qz.*2.0
t23 = qx.*t10.*2.0
t15 = t14-t23
t16 = t7.*2.0
t17 = t5+t16-1.0
t18 = qx.*qy.*2.0
t19 = qz.*t10.*2.0
t20 = t18+t19
t21 = t11-t12
t22 = P3.*t6
t24 = T1.*t13
t25 = T2.*t15
t27 = T3.*t6
t28 = P1.*t13
t29 = P2.*t15
t26 = t22+t24+t25-t27-t28-t29
t30 = t3+t16-1.0
t31 = t18-t19
t32 = t14+t23
t33 = 1.0./t26
t34 = 1.0./rhox
t35 = t26.*u0
t36 = P1.*t17
t37 = T2.*t20
t38 = T3.*t21
t42 = T1.*t17
t43 = P2.*t20
t44 = P3.*t21
t39 = t36+t37+t38-t42-t43-t44
t40 = f.*t34.*t39
t41 = t35+t40
t45 = 1.0./t26.^2
t46 = qz.*2.0
t47 = 1.0./t10
t51 = qx.*qy.*t47.*2.0
t48 = t46-t51
t49 = t10.*2.0
t57 = t2.*t47.*2.0
t50 = t49-t57
t52 = qy.*2.0
t69 = qx.*qz.*t47.*2.0
t53 = t52-t69
t54 = t46+t51
t55 = P3.*qx.*4.0
t56 = T1.*t48
t58 = P2.*t50
t87 = T3.*qx.*4.0
t88 = P1.*t48
t89 = T2.*t50
t59 = t55+t56+t58-t87-t88-t89
t63 = t4.*t47.*2.0
t60 = t49-t63
t61 = qx.*2.0
t68 = qy.*qz.*t47.*2.0
t62 = t61-t68
t64 = P3.*qy.*4.0
t65 = T2.*t54
t66 = T1.*t60
t90 = T3.*qy.*4.0
t91 = P2.*t54
t92 = P1.*t60
t67 = t64+t65+t66-t90-t91-t92
t70 = t52+t69
t71 = t61+t68
t95 = t7.*t47.*2.0
t72 = t49-t95
t73 = P1.*t62
t74 = P2.*t70
t93 = T1.*t62
t94 = T2.*t70
t75 = t73+t74-t93-t94
t76 = 1.0./rhoy
t77 = t26.*v0
t78 = T2.*t30
t79 = P1.*t31
t80 = P3.*t32
t83 = P2.*t30
t84 = T1.*t31
t85 = T3.*t32
t81 = t78+t79+t80-t83-t84-t85
t86 = f.*t76.*t81
t82 = t77-t86
uv = [t33.*t41t33.*t82]
if nargout > 1
    t96 = t13.*u0
    t97 = t96-f.*t17.*t34
    t98 = t33.*t97
    t99 = t15.*u0
    t100 = f.*t20.*t34
    t101 = t99+t100
    t102 = t33.*t101
    t103 = t6.*u0
    t104 = t103-f.*t21.*t34
    t105 = t6.*t41.*t45
    t106 = t13.*v0
    t107 = f.*t31.*t76
    t108 = t106+t107
    t109 = t33.*t108
    t110 = t15.*v0
    t111 = t110-f.*t30.*t76
    t112 = t33.*t111
    t113 = t6.*v0
    t114 = t113-f.*t32.*t76
    t115 = t6.*t45.*t82
    A = reshape([t98-t13.*t41.*t45,t109-t13.*t45.*t82,t102-t15.*t41.*t45,t112-t15.*t45.*t82,t105-t33.*t104,t115-t33.*t114,t33.*(t59.*u0-f.*t34.*(P2.*t53+P3.*t54-T2.*t53-T3.*t54))-t41.*t45.*t59,t33.*(t59.*v0+f.*t76.*(P2.*qx.*4.0-P3.*t50-P1.*t70-T2.*qx.*4.0+T3.*t50+T1.*t70))-t45.*t59.*t82,t33.*(t67.*u0+f.*t34.*(P1.*qy.*4.0+P3.*t60-P2.*t62-T1.*qy.*4.0-T3.*t60+T2.*t62))-t41.*t45.*t67,t33.*(t67.*v0-f.*t76.*(P3.*t48+P1.*t71-T3.*t48-T1.*t71))-t45.*t67.*t82,-t33.*(t75.*u0-f.*t34.*(P1.*qz.*4.0-P2.*t72-P3.*t71-T1.*qz.*4.0+T2.*t72+T3.*t71))+t41.*t45.*t75,-t33.*(t75.*v0-f.*t76.*(P2.*qz.*4.0-P3.*t53+P1.*t72-T2.*qz.*4.0+T3.*t53-T1.*t72))+t45.*t75.*t82],[2,6])
end
if nargout > 2
    B = reshape([-t98+t13.*t41.*t45,-t109+t13.*t45.*t82,-t102+t15.*t41.*t45,-t112+t15.*t45.*t82,-t105+t33.*t104,-t115+t33.*t114],[2,3])
end

