# coding: utf-8

from pyccel.stdlib import *

#$ header legendre(int) results(double [:], double [:])
def legendre(p):
    k = p + 1
    x = zeros(k, double)
    w = zeros(k, double)
    if p == 1:
        x[0] = -0.577350269189625765
        x[1] =  0.577350269189625765
        w[0] =  1.0
        w[1] =  1.0
    elif p == 2:
        x[0] = -0.774596669241483377
        x[1] = 0.0
        x[2] = 0.774596669241483377
        w[0] = 0.55555555555555556
        w[1] = 0.888888888888888889
        w[2] = 0.55555555555555556
    elif p == 3:
        x[0] = -0.861136311594052575
        x[1] = -0.339981043584856265
        x[2] = 0.339981043584856265
        x[3] = 0.861136311594052575
        w[0] = 0.347854845137453853
        w[1] = 0.65214515486254615
        w[2] = 0.65214515486254614
        w[3] = 0.34785484513745386
    elif p == 4:
        x[0] = -0.906179845938663993
        x[1] = -0.538469310105683091
        x[2] = 0.0
        x[3] = 0.538469310105683091
        x[4] = 0.906179845938663993
        w[0] = 0.236926885056189088
        w[1] = 0.478628670499366468
        w[2] = 0.56888888888888889
        w[3] = 0.478628670499366468
        w[4] = 0.23692688505618909
    elif p == 5:
        x[0] = -0.932469514203152028
        x[1] = -0.661209386466264514
        x[2] = -0.238619186083196909
        x[3] = 0.238619186083196909
        x[4] = 0.661209386466264514
        x[5] = 0.932469514203152028
        w[0] = 0.171324492379170345
        w[1] = 0.360761573048138608
        w[2] = 0.467913934572691047
        w[3] = 0.467913934572691047
        w[4] = 0.36076157304813861
        w[5] = 0.171324492379170345
    elif p == 6:
        x[0] = -0.94910791234275852
        x[1] = -0.74153118559939444
        x[2] = -0.405845151377397167
        x[3] = 0.0
        x[4] = 0.405845151377397167
        x[5] = 0.74153118559939444
        x[6] = 0.949107912342758525
        w[0] = 0.129484966168869693
        w[1] = 0.27970539148927667
        w[2] = 0.381830050505118945
        w[3] = 0.417959183673469388
        w[4] = 0.38183005050511895
        w[5] = 0.279705391489276667
        w[6] = 0.129484966168869693
    return x,w
