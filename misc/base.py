#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:14:41 2020

@author: twguest
"""

import numpy as np

def check_nan(array):
    return print(np.isnan(array).any())