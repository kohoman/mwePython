#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:03:51 2017

@author: khoman
"""
import numpy as np
import scipy.constants

# ... given data ...
    
# ... physical constants and properties ...

pi = scipy.constants.pi
Ru = scipy.constants.R   #(molar gas constant)

# ... analysis ...

x=np.linspace(0,5,5)

# ... answers ...

anum = 'abcde'
avar = [r'$x$',r'$y$',r'$z$',r'$a$',r'$b$']
ans = zip(anum,avar,x)
print('\n')
for i in range(len(ans)):
   print('Answer ({}): {} = {!s}\n'.format(*ans[i]))