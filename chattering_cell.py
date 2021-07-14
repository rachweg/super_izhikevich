#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:17:52 2021

@author: rachweg
"""

import izhikevich_cells as izh

class cCell(izh.izhCell):
    """ model spike rates of chattering """
    def __init__(self, stimVal):
        """ reassign parameters """
        super().__init__(stimVal)
        self.celltype = 'Chattering'
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = 0.03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
        self.stimVal = stimVal
        
myCell = cCell(4000)
myCell.simulate()
if __name__=='__main__':
    izh.plotMyData(myCell)

