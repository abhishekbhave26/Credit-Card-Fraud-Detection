# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:55:37 2019

@author: abhis
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn
import main as m
from sklearn.metrics import classification_report,accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

class Solution():
    
    def fit(self,fraud,classifiers,x,y):
        #fit the model
        n_outliers=len(fraud)
        for i,(clf_name,clf) in enumerate(classifiers.items()):
            if clf_name=="Local Outlier Factor":
                y_pred=clf.fit_predict(x)
                scores_pred=clf.negative_outlier_factor_
            else:
                clf.fit(x)
                scores_pred=clf.decision_function(x)
                y_pred=clf.predict(x)
                
            #rehape the prediction 0 for valid, 1 for fraud
            y_pred[y_pred==1]=0
            y_pred[y_pred==-1]=1
            
            n_errors=(y_pred!=y).sum()
            
            #classification matrix
            print("{} : {}".format(clf_name,n_errors))
            print(accuracy_score(y,y_pred))
            print(classification_report(y,y_pred))
            
    
    
    def main(self):
        #data=m.Solution.getData(Solution)
        outlier_fraction,fraud=m.Solution.NumberOfFraudCases(Solution,data)
        x,y=m.Solution.dataFromDF(Solution,data)
        state=1
        
        #define outlier dectection methods
        classifiers={"Isolation Forest":IsolationForest(max_samples=len(x)
        ,contamination=outlier_fraction,random_state=state),
        "Local Outlier Factor":LocalOutlierFactor(n_neighbors=20,contamination=outlier_fraction)}
        
        Solution.fit(Solution,fraud,classifiers,x,y)
        
          

if __name__=="__main__":
    s=Solution()
    s.main()
        
        
        