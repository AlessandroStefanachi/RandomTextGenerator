#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:11:01 2022

@author: alessandro
"""

import pandas as pd
t=pd.read_csv(r'./test/model_test/model_real2')
t.plot(ylabel='RealCount/ModelPred',x='parole',logx=True)
desc_t=t.describe()
