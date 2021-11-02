#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import random
import urllib.parse as ups

class Randomizer:
    def __init__(self):
        self.df = pd.read_csv('new_train.csv').iloc[:,1:]
        self.prob = [1/len(self.df)]*len(self.df)
        self.preferred_cols = []
        self.recommended_recipe = set()
        self.inc = 0
        self.dec = 0
        self.input_element = []

    def add_cart(self,inp):
        self.input_element.append(inp)
        self.preferred_cols = []
        self.recommended_recipe = set()
        for ingri in self.df.columns[1:]:
            if inp in ingri:
                self.preferred_cols.append(ingri)
                for index_no in self.df[self.df[ingri] == 1].index:
                    self.recommended_recipe.add(index_no)

        self.inc = 0.5/len(self.recommended_recipe)
        self.dec = 0.5/(len(self.df) - len(self.recommended_recipe))
        for i in range(len(self.prob)):
            if i in self.recommended_recipe:
                self.prob[i] += self.inc
            else:
                self.prob[i] -= self.dec
        #print(max(self.prob),min(self.prob),sum(self.prob))

    def recommender(self):
        return 'https://www.google.com/search?q='+ups.quote_plus(random.choice(list(self.df[pd.Series(self.prob)==max(self.prob)].label.values)))

