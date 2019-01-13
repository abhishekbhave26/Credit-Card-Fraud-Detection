# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:17:33 2019

@author: abhis
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn


#print('Seaborn version is {}'.format(seaborn.__version__))
class Solution():
        
    def getData(self):
        data=pd.read_csv('creditcard.csv')
        return data
    
    
    def plotData(self,data):
        data.hist(figsize=(20,20))
        plt.show()
    
    
    def NumberOfFraudCases(self,data):
        fraud=data[data['Class']==1]
        valid=data[data['Class']==0]
        outlierFunction=len(fraud)/float(len(valid))
        #print(outlierFunction)
        
        #print('Fraud cases are : {}'.format(len(fraud)))
        #print('Valid cases are : {}'.format(len(valid)))
        return outlierFunction ,fraud       
    
    
    def correlationMatrix(self,data):
        corrmat=data.corr()
        fig=plt.figure(figsize=(12,9))
        sns.heatmap(corrmat,vmax=0.8,square=True)
        plt.show()
        
    
    def dataFromDF(self,data):
        columns=data.columns.tolist()
        
        columns=[c for c in columns if c not in ["Class"]]
        target="Class"
        x=data[columns]
        y=data[target]
        print(x.shape,y.shape)
        return x,y
        
    
    def main(self):
        data=getData()
        #plotData(data)
        #NumberOfFraudCases(data)
        #correlationMatrix(data)
        x,y=dataFromDF(data)
    
    
if __name__=="__main__":
    s=Solution()
    s.main()
    