#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:43:15 2022

@author: hosni adil imad eddine
"""


def fib(n):
    a ,b ,i= 1,1,2
    
    if n>1:
        while i<=n:
            a ,b=n,a+b
    return a
