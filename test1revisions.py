#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:25:04 2024

@author: andyguerrero
"""

proteins = ['PF13411.1', 'PF12728.1', 'PF01381.2',
            'PF00205.2','PF10875.1', 'PF05766.1',
            'PF00860.2', 'PF10766.1', 'PF11812.1']

# 2.1
def count_unique_proteins(x):
    return len(set([item[:7] for item in x]))

# 2.2
def count_proteins(x):
    names = (item[:7] for item in x)
    counts = {}
    for pfname in names: 
        counts[pfname] = counts.get(pfname, 0) + 1
    return counts

# Problem 3
def merge_protein_counts(d1, d2):
    all_keys = set(d1.keys()) | set(d2.keys())
    d_merged = {k: (d1.get(k,0), d2.get(k,0)) for k in all_keys}
    return d_merged
        
       
#3.1
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
          'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 
          'October': 10, 'November': 11, 'December': 12}
dates_list = ["February 6, 1992", "February 18, 1992", "February 27, 1992", 
              "September 6, 1994", "December 1, 1993"]
def dates_to_iso8601(x):
    iso_dates = []
    splitlist = [s.split() for s in x]
    for month, day, year in splitlist: 
        month = str(months[month])
        day = str(day[:-1])
        year = str(year)
        iso_date = "-".join([year, month, day])
        iso_dates.append(iso_date)
    return iso_dates    

def sort_dates(l):
    newlist = []
    for item in l:
        month, day, year = item.split()
        month = int(months[month])
        day = int(day[:-1])
        year = int(year)
        newlist.append((year, month, day))
    return sorted(newlist)

