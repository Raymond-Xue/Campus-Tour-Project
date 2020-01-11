# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:19:09 2019

@author: 薛代豪
"""
class Time:
    #Calculate Time for each travel method
    def time_calculation(self, length, RoadType, walk):
        
        length = float(length)
        
        if walk == 1:
            if RoadType == '(F)' or RoadType == '(f)' or RoadType == '(b)':
                time = length / 272
            elif RoadType == '(U)' or RoadType == '(u)':
                time = length / (272 * 0.9)
            elif RoadType == '(D)' or RoadType == '(d)':
                time = length / (272 * 1.1)
            elif RoadType == '(s)':
                time = length / (272 * 0.5)
            elif RoadType == '(t)':
                time = length / (272 * 0.9)
            else:
                time = length / 272
        else:
            if RoadType == '(F)':
                time = length / (272 * 2.0)
            elif RoadType == '(U)':
                time = length / (272 * 1.1)
            elif RoadType == '(D)':
                time = length / (272 * 5.0)
            else:
                time = length / (272 * 2.0)
                
        return time