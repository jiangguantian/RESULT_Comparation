# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:29:14 2015

@author: zhanggaoyang
"""
import numpy as np
from matplotlib import pyplot as plt
SJ = np.arange(8,21)
NAME_T = []
for i in SJ:
    NAME_T.append('T_%s' % i)


for i in np.arange(SJ.size):
    NAME = NAME_T[i]
    #T_i文件修改，并生成T_i数组
    f = open("E:\RESULT_Comparation\%s.TXT" % (NAME))  
    f_1 = open("E:\RESULT_Comparation\%s_1.TXT" % (NAME), 'w')  
    line = f.readline()  
    while line:  
        string = line.replace(' ',',')  
        f_1.write(string)  
        line = f.readline()      
          
    f.close()  
    f_1.close() 
    
    f_1 = open("E:\RESULT_Comparation\%s_1.TXT" % (NAME))  
    f = open("E:\RESULT_Comparation\%s.TXT" % (NAME), 'w')  
    line = f_1.readline()  
    while line:  
        string = line.replace(',0.00','0.00')  
        f.write(string)
        line = f_1.readline()
          
    f.close()  
    f_1.close()

names = locals() 
for i in SJ:
    names['T_%s'%i] = np.loadtxt("E:\RESULT_Comparation\T_%s.TXT" % i, delimiter=',')



T_SHICE = np.loadtxt("E:\RESULT_Comparation\T_SHICE.TXT", delimiter=',')
#实测距离数组
SCJL = [range(0,9), range(9,15), range(15,21), range(21,26), range(26,34), range(34,42), range(42,52), range(52,62), range(62,68), range(68,70)]

DIS11 = T_SHICE[SCJL[0],0]
DIS22 = T_SHICE[SCJL[1],0]
DIS44 = T_SHICE[SCJL[2],0]
DIS55 = T_SHICE[SCJL[3],0]
DISEE = T_SHICE[SCJL[4],0]
DISFF = T_SHICE[SCJL[5],0]
DISAA = T_SHICE[SCJL[6],0]
DISBB = T_SHICE[SCJL[7],0]
DISCC = T_SHICE[SCJL[8],0]
DISDD = T_SHICE[SCJL[9],0]

JM11 = ['11','22','44','55','EE','FF','AA','BB','CC','DD']
for i in JM11:
    names['N%s'%i] = names['DIS%s'%i].size
#N11 = DIS11.size
#N22 = DIS22.size
#N44 = DIS44.size
#N55 = DIS55.size
#NEE = DISEE.size
#NFF = DISFF.size
#NAA = DISAA.size
#NBB = DISBB.size
#NCC = DISCC.size
#NDD = DISDD.size

for i in SJ: 
    names['T%s_11'%i] = T_SHICE[SCJL[0],i-7]
    names['T%s_22'%i] = T_SHICE[SCJL[1],i-7]
    names['T%s_44'%i] = T_SHICE[SCJL[2],i-7]
    names['T%s_55'%i] = T_SHICE[SCJL[3],i-7]
    names['T%s_EE'%i] = T_SHICE[SCJL[4],i-7]
    names['T%s_FF'%i] = T_SHICE[SCJL[5],i-7]
    names['T%s_AA'%i] = T_SHICE[SCJL[6],i-7]
    names['T%s_BB'%i] = T_SHICE[SCJL[7],i-7]
    names['T%s_CC'%i] = T_SHICE[SCJL[8],i-7]
    names['T%s_DD'%i] = T_SHICE[SCJL[9],i-7]
    
    
#T15_11 = T_SHICE[0:9,8]
#T15_22 = T_SHICE[9:15,8]
#T15_44 = T_SHICE[15:21,8]
#T15_55 = T_SHICE[21:26,8]
#T15_EE = T_SHICE[26:34,8]
#T15_FF = T_SHICE[34:42,8]
#T15_AA = T_SHICE[42:52,8]
#T15_BB = T_SHICE[52:62,8]
#T15_CC = T_SHICE[62:68,8]
#T15_DD = T_SHICE[68:70,8]


DIS1 = [0,5.00E-03,1.00E-02,1.50E-02,2.00E-02,2.50E-02,3.00E-02,3.50E-02,4.00E-02,4.50E-02,5.00E-02,5.50E-02,6.00E-02,6.50E-02,7.00E-02,7.50E-02,8.00E-02,8.50E-02,9.00E-02,9.50E-02,0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37,0.375,0.38,0.385,0.39,0.395,0.4,0.405,0.41,0.415,0.42,0.425,0.43,0.435,0.44,0.445,0.45,0.455,0.46,0.465,0.47,0.475,0.48,0.485,0.49,0.495,0.5,0.505,0.51,0.515,0.52,0.525,0.53,0.535,0.54,0.545,0.55,0.555,0.56,0.565,0.57,0.575,0.58,0.585,0.59,0.595,0.6,0.605,0.61,0.615,0.62,0.625,0.63,0.635,0.64,0.645,0.65,0.655,0.66,0.665,0.67,0.675,0.68,0.685,0.69,0.695,0.7,0.705,0.71,0.715,0.72,0.725,0.73,0.735,0.74,0.745,0.75,0.755,0.76,0.765,0.77,0.775,0.78,0.785,0.79,0.795,0.8]
DIS2 = [0,5.00E-03,1.00E-02,1.50E-02,2.00E-02,2.50E-02,3.00E-02,3.50E-02,4.00E-02,4.50E-02,5.00E-02,5.50E-02,6.00E-02,6.50E-02,7.00E-02,7.50E-02,8.00E-02,8.50E-02,9.00E-02,9.50E-02,0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37,0.375,0.38,0.385,0.39,0.395,0.4,0.405,0.41,0.415,0.42,0.425,0.43,0.435,0.44,0.445,0.45,0.455,0.46,0.465,0.47,0.475,0.48,0.485,0.49,0.495,0.5]
DIS4 = [0,7.50E-03,1.50E-02,2.25E-02,3.00E-02,3.75E-02,4.50E-02,5.25E-02,6.00E-02,6.75E-02,7.50E-02,8.25E-02,9.00E-02,9.75E-02,0.105,0.1125,0.12,0.1275,0.135,0.1425,0.15,0.1575,0.165,0.1725,0.18,0.1875,0.195,0.2025,0.21,0.2175,0.225,0.2325,0.24,0.2475,0.255,0.2625,0.27,0.2775,0.285,0.2925,0.3,0.3075,0.315,0.3225,0.33,0.3375,0.345,0.3525,0.36,0.3675,0.375,0.3825,0.39,0.3975,0.405,0.4125,0.42,0.4275,0.435,0.4425,0.45,0.4575,0.465,0.4725,0.48,0.4875,0.495,0.5025,0.51,0.5175,0.525,0.5325,0.54,0.5475,0.555,0.5625,0.57,0.5775,0.585,0.5925,0.6,0.6075,0.615,0.6225,0.63,0.6375,0.645,0.6525,0.66,0.6675,0.675,0.6825,0.69,0.6975,0.705,0.7125,0.72,0.7275,0.735,0.7425,0.75]
DIS5 = [0,7.50E-03,1.50E-02,2.25E-02,3.00E-02,3.75E-02,4.50E-02,5.25E-02,6.00E-02,6.75E-02,7.50E-02,8.25E-02,9.00E-02,9.75E-02,0.105,0.1125,0.12,0.1275,0.135,0.1425,0.15,0.1575,0.165,0.1725,0.18,0.1875,0.195,0.2025,0.21,0.2175,0.225,0.2325,0.24,0.2475,0.255,0.2625,0.27,0.2775,0.285,0.2925,0.3,0.3075,0.315,0.3225,0.33,0.3375,0.345,0.3525,0.36,0.3675,0.375,0.3825,0.39,0.3975,0.405,0.4125,0.42,0.4275,0.435,0.4425,0.45,0.4575,0.465,0.4725,0.48,0.4875,0.495,0.5025,0.51,0.5175,0.525,0.5325,0.54,0.5475,0.555,0.5625,0.57,0.5775,0.585,0.5925,0.6]
DISE = [0,5.00E-02,1.00E-01,1.50E-01,2.00E-01,2.50E-01,3.00E-01,3.50E-01,4.00E-01,4.50E-01,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9,2.95,3,3.05,3.1,3.15,3.2,3.25,3.3,3.35,3.4,3.45,3.5,3.55,3.6,3.65,3.7,3.75,3.8,3.85,3.9,3.95,4,4.05,4.1,4.15,4.2,4.25,4.3,4.35,4.4,4.45,4.5,4.55,4.6,4.65,4.7,4.75,4.8,4.85,4.9,4.95,5,5.05,5.1,5.15,5.2,5.25,5.3,5.35,5.4,5.45,5.5,5.55,5.6,5.65,5.7,5.75,5.8,5.85,5.9,5.95,6,6.05,6.1,6.15,6.2,6.25,6.3,6.35,6.4,6.45,6.5,6.55,6.6,6.65,6.7,6.75,6.8,6.85,6.9,6.95,7]
DISF = [0,5.00E-02,1.00E-01,1.50E-01,2.00E-01,2.50E-01,3.00E-01,3.50E-01,4.00E-01,4.50E-01,5.00E-01,5.50E-01,6.00E-01,6.50E-01,7.00E-01,7.50E-01,8.00E-01,8.50E-01,9.00E-01,9.50E-01,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9,2.95,3,3.05,3.1,3.15,3.2,3.25,3.3,3.35,3.4,3.45,3.5,3.55,3.6,3.65,3.7,3.75,3.8,3.85,3.9,3.95,4,4.05,4.1,4.15,4.2,4.25,4.3,4.35,4.4,4.45,4.5,4.55,4.6,4.65,4.7,4.75,4.8,4.85,4.9,4.95,5,5.05,5.1,5.15,5.2,5.25,5.3,5.35,5.4,5.45,5.5,5.55,5.6,5.65,5.7,5.75,5.8,5.85,5.9,5.95,6,6.05,6.1,6.15,6.2,6.25,6.3,6.35,6.4,6.45,6.5,6.55,6.6,6.65,6.7,6.75,6.8,6.85,6.9,6.95,7]
DISA = [0,5.75E-02,0.115,0.1725,0.23,0.2875,0.345,0.4025,0.46,0.5175,0.575,0.6325,0.69,0.7475,0.805,0.8625,0.92,0.9775,1.035,1.0925,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9,2.95,3,3.05,3.1,3.15,3.2075,3.265,3.3225,3.38,3.4375,3.495,3.5525,3.61,3.6675,3.725,3.7825,3.84,3.8975,3.955,4.0125,4.07,4.1275,4.185,4.2425,4.3,4.35,4.4,4.45,4.5,4.55,4.6,4.65,4.7,4.75,4.8,4.85,4.9,4.95,5,5.05,5.1,5.15,5.2,5.25,5.3,5.35,5.4,5.45,5.5,5.55,5.6,5.65,5.7,5.75,5.8,5.85,5.9,5.95,6,6.05,6.1,6.15,6.2,6.25,6.3,6.35,6.4,6.45,6.5,6.55,6.6,6.65,6.7,6.75,6.8,6.85,6.9,6.95,7,7.05,7.1,7.15,7.2,7.25,7.3,7.35,7.4,7.45,7.5,7.55,7.6,7.65,7.7,7.75,7.8,7.85,7.9,7.95,8,8.05,8.1,8.15,8.2,8.25,8.3,8.325,8.35,8.375,8.4,8.425,8.45,8.475,8.5,8.525,8.55,8.575,8.6,8.625,8.65,8.675,8.7,8.725,8.75,8.775,8.8]
DISB = [0,5.75E-02,1.15E-01,1.73E-01,2.30E-01,2.88E-01,3.45E-01,4.03E-01,4.60E-01,5.18E-01,0.575,0.6325,0.69,0.7475,0.805,0.8625,0.92,0.9775,1.035,1.0925,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9,2.95,3,3.05,3.1,3.15,3.2075,3.265,3.3225,3.38,3.4375,3.495,3.5525,3.61,3.6675,3.725,3.7825,3.84,3.8975,3.955,4.0125,4.07,4.1275,4.185,4.2425,4.3,4.35,4.4,4.45,4.5,4.55,4.6,4.65,4.7,4.75,4.8,4.85,4.9,4.95,5,5.05,5.1,5.15,5.2,5.25,5.3,5.35,5.4,5.45,5.5,5.55,5.6,5.65,5.7,5.75,5.8,5.85,5.9,5.95,6,6.05,6.1,6.15,6.2,6.25,6.3,6.35,6.4,6.45,6.5,6.55,6.6,6.65,6.7,6.75,6.8,6.85,6.9,6.95,7,7.05,7.1,7.15,7.2,7.25,7.3,7.35,7.4,7.45,7.5,7.55,7.6,7.65,7.7,7.75,7.8,7.85,7.9,7.95,8,8.05,8.1,8.15,8.2,8.25,8.3,8.325,8.35,8.375,8.4,8.425,8.45,8.475,8.5,8.525,8.55,8.575,8.6,8.625,8.65,8.675,8.7,8.725,8.75,8.775,8.8]
DISC = [0,5.00E-03,1.00E-02,1.50E-02,2.00E-02,2.50E-02,3.00E-02,3.50E-02,4.00E-02,4.50E-02,5.00E-02,5.50E-02,6.00E-02,6.50E-02,7.00E-02,7.50E-02,8.00E-02,8.50E-02,9.00E-02,9.50E-02,0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37,0.375,0.38,0.385,0.39,0.395,0.4,0.405,0.41,0.415,0.42,0.425,0.43,0.435,0.44,0.445,0.45,0.455,0.46,0.465,0.47,0.475,0.48,0.485,0.49,0.495,0.5]
DISD = [0,1.00E-02,2.00E-02,3.00E-02,4.00E-02,5.00E-02,6.00E-02,7.00E-02,8.00E-02,9.00E-02,1.00E-01,1.10E-01,1.20E-01,1.30E-01,1.40E-01,1.50E-01,1.60E-01,1.70E-01,1.80E-01,1.90E-01,0.2]




for sj in SJ: 
	
    JM1 = ['1','2','4','5','E','F','A','B','C','D']
    for i in JM1:
        names['T%s_%s'%(sj,i)] = np.copy(names['T%s_%s%s'%(sj,i,i)])
        #T15_1 = np.copy(T15_11)
        #T15_2 = np.copy(T15_22)
        #T15_4 = np.copy(T15_44)
        #T15_5 = np.copy(T15_55)
        #T15_E = np.copy(T15_EE)
        #T15_F = np.copy(T15_FF)
        #T15_A = np.copy(T15_AA)
        #T15_B = np.copy(T15_BB)
        #T15_C = np.copy(T15_CC)
        #T15_D = np.copy(T15_DD)

    for i in np.arange(N11):
        index = DIS1.index(DIS11[i])
        names['T%s_1'%sj][i] = names['T_%s'%sj][index,0]

    for i in np.arange(N22):
        index = DIS2.index(DIS22[i])
        names['T%s_2'%sj][i] = names['T_%s'%sj][index,1]
    for i in np.arange(N44):
        index = DIS4.index(DIS44[i])
        names['T%s_4'%sj][i] = names['T_%s'%sj][index,2]
    for i in np.arange(N55):
        index = DIS5.index(DIS55[i])
        names['T%s_5'%sj][i] = names['T_%s'%sj][index,3]
    for i in np.arange(NEE):
        index = DISE.index(DISEE[i])
        names['T%s_E'%sj][i] = names['T_%s'%sj][index,4]
    for i in np.arange(NFF):
        index = DISF.index(DISFF[i])    
        names['T%s_F'%sj][i] = names['T_%s'%sj][index,5]
    for i in np.arange(NAA):
        index = DISA.index(DISAA[i])    
        names['T%s_A'%sj][i] = names['T_%s'%sj][index,6]
    for i in np.arange(NBB):
        index = DISB.index(DISBB[i])    
        names['T%s_B'%sj][i] = names['T_%s'%sj][index,7]
    for i in np.arange(NCC):
        index = DISC.index(DISCC[i])    
        names['T%s_C'%sj][i] = names['T_%s'%sj][index,8]
    for i in np.arange(NDD):
        index = DISD.index(DISDD[i])    
        names['T%s_D'%sj][i] = names['T_%s'%sj][index,9]



#T15_1 = np.copy(T15_11)
#T15_2 = np.copy(T15_22)
#T15_4 = np.copy(T15_44)
#T15_5 = np.copy(T15_55)
#T15_E = np.copy(T15_EE)
#T15_F = np.copy(T15_FF)
#T15_A = np.copy(T15_AA)
#T15_B = np.copy(T15_BB)
#T15_C = np.copy(T15_CC)
#T15_D = np.copy(T15_DD)
#
#
#for i in np.arange(N11):
#    index = DIS1.index(DIS11[i])
#    T15_1[i] = T_15[index,0]
#for i in np.arange(N22):
#    index = DIS2.index(DIS22[i])
#    T15_2[i] = T_15[index,1]
#for i in np.arange(N44):
#    index = DIS4.index(DIS44[i])
#    T15_4[i] = T_15[index,2]
#for i in np.arange(N55):
#    index = DIS5.index(DIS55[i])
#    T15_5[i] = T_15[index,3]
#for i in np.arange(NEE):
#    index = DISE.index(DISEE[i])
#    T15_E[i] = T_15[index,4]
#for i in np.arange(NFF):
#    index = DISF.index(DISFF[i])    
#    T15_F[i] = T_15[index,5]
#for i in np.arange(NAA):
#    index = DISA.index(DISAA[i])    
#    T15_A[i] = T_15[index,6]
#for i in np.arange(NBB):
#    index = DISB.index(DISBB[i])    
#    T15_B[i] = T_15[index,7]
#for i in np.arange(NCC):
#    index = DISC.index(DISCC[i])    
#    T15_C[i] = T_15[index,8]
#for i in np.arange(NDD):
#    index = DISD.index(DISDD[i])    
#    T15_D[i] = T_15[index,9]
 

for sj in SJ: 
    names['T%s_1'%sj][8] = names['T%s_1'%sj][7]
    names['T%s_4'%sj][0] = 2 * names['T%s_4'%sj][1] - names['T%s_4'%sj][2]
    #T15_1[8] = T15_1[7]
    #T15_4[0] = 2 * T15_4[1] - T15_4[2]
    #
    #T18_1[8] = T18_1[7]
    #T18_4[0] = 2 * T18_4[1] - T18_4[2]
    #
    #T20_1[8] = T20_1[7]
    #T20_4[0] = 2 * T20_4[1] - T20_4[2]  
for sj in SJ:     
    JM1 = ['1','2','4','5','E','F','A','B','C','D']
    for i in JM1:
        names['fig%s_%s'%(sj,i)] = plt.figure('fig%s_%s'%(sj,i))
        plt.plot(names['DIS%s%s'%(i,i)], names['T%s_%s%s'%(sj,i,i)], 'r-', label='SHICE')
        plt.plot(names['DIS%s%s'%(i,i)], names['T%s_%s'%(sj,i)], 'g-', label='JISUAN')
        plt.savefig("E:\RESULT_Comparation\\%s点对比图\\fig%s_%s" % (sj,sj,i))
        plt.close('all')

#
#fig1 = plt.figure('fig1')
#plt.plot(DIS11, T15_11, 'r-', label='SHICE')
#plt.plot(DIS11, T15_1, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\fig1")
#
#fig2 = plt.figure('fig2')
#plt.plot(DIS22, T15_22, 'r-', label='SHICE')
#plt.plot(DIS22, T15_2, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\fig2")
#
#fig4 = plt.figure('fig4')
#plt.plot(DIS44, T15_44, 'r-', label='SHICE')
#plt.plot(DIS44, T15_4, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\fig4")
#
#fig5 = plt.figure('fig5')
#plt.plot(DIS55, T15_55, 'r-', label='SHICE')
#plt.plot(DIS55, T15_5, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\fig5")
#
#figE = plt.figure('figE')
#plt.plot(DISEE, T15_EE, 'r-', label='SHICE')
#plt.plot(DISEE, T15_E, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\figE")
#
#figF = plt.figure('figF')
#plt.plot(DISFF, T15_FF, 'r-', label='SHICE')
#plt.plot(DISFF, T15_F, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\figF")
#
#figA = plt.figure('figA')
#plt.plot(DISAA, T15_AA, 'r-', label='SHICE')
#plt.plot(DISAA, T15_A, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\figA")
#
#figB = plt.figure('figB')
#plt.plot(DISBB, T15_BB, 'r-', label='SHICE')
#plt.plot(DISBB, T15_B, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\figB")
#
#figC = plt.figure('figC')
#plt.plot(DISCC, T15_CC, 'r-', label='SHICE')
#plt.plot(DISCC, T15_C, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\figC")
#
#figD = plt.figure('figD')
#plt.plot(DISDD, T15_DD, 'r-', label='SHICE')
#plt.plot(DISDD, T15_D, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\figD")
#
#plt.close('all')




#下面的程序绘制关键点处一天的温度变化实测值与计算值的比较图
GJD11 = ['11','22','33','44','55','66','77','88','99','1010','1111','1212']
GJD1 = ['1','2','3','4','5','6','7','8','9','10','11','12']
#关键点对应在SHICE数据中的行号
HH = [42,44,48,52,54,58,27,29,32,35,37,40]
#T11 = T_SHICE[42, :]
for i in GJD11: 
    names['T%s'%i] = T_SHICE[HH[0],1:]
    names['T%s'%i] = T_SHICE[HH[1],1:]
    names['T%s'%i] = T_SHICE[HH[2],1:]
    names['T%s'%i] = T_SHICE[HH[3],1:]
    names['T%s'%i] = T_SHICE[HH[4],1:]
    names['T%s'%i] = T_SHICE[HH[5],1:]
    names['T%s'%i] = T_SHICE[HH[6],1:]
    names['T%s'%i] = T_SHICE[HH[7],1:]
    names['T%s'%i] = T_SHICE[HH[8],1:]
    names['T%s'%i] = T_SHICE[HH[9],1:]

for i in GJD1: 
    names['T%s'%i] = np.copy(names['T%s%s'%(i,i)])
#T1 = np.copy(T11)
#T1 = T_8[0,6]
for i in SJ: 
    T1[i-8] = names['T_%s'%i][0,6]
    T2[i-8] = names['T_%s'%i][2,6]    
    T3[i-8] = names['T_%s'%i][6,6]    
    T4[i-8] = names['T_%s'%i][0,7]    
    T5[i-8] = names['T_%s'%i][2,7]    
    T6[i-8] = names['T_%s'%i][6,7]    
    T7[i-8] = names['T_%s'%i][1,4]    
    T8[i-8] = names['T_%s'%i][3,4]    
    T9[i-8] = names['T_%s'%i][6,4]    
    T10[i-8] = names['T_%s'%i][1,5]    
    T11[i-8] = names['T_%s'%i][3,5]    
    T12[i-8] = names['T_%s'%i][6,5]    

sjd = 0
for gjd in GJD1:    
    names['fig%s'%gjd] = plt.figure('fig%s'%gjd)
    plt.plot(SJ, names['T%s%s'%(gjd,gjd)], 'r-', label='SHICE')
    plt.plot(SJ, names['T%s'%(gjd)], 'g-', label='JISUAN')
    sjd = sjd +1
    plt.savefig("E:\RESULT_Comparation\\关键点全天温度对比图\\fig%s点" % SJ[sjd])
    plt.close('all')
    
#fig1 = plt.figure('fig1')
#plt.plot(DIS11, T15_11, 'r-', label='SHICE')
#plt.plot(DIS11, T15_1, 'g-', label='JISUAN')
#plt.savefig("E:\RESULT_Comparation\\15点对比图\\fig1")    
    
    
    
