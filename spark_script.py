### Script to generate realtime reasult using saprk streaming
#Action:: this script uses spark streaming application in order to generate the reasults of real time data.
# Inputs:Xgboost ml model, Data at port 9999
#output : Output will bw printed on the execution code window.
# to execute  : spark-submit spark_script.py
# Author : sumit chandak (chandaksumit29@gmail.com)
#date : 1/13/2018  


import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import pandas as pd
from sklearn.externals import joblib
import pickle

# Function to map the point to the right quadrant
def classify(line,model):
    line
    line='0.00,1.69235134,  1.99906184,  1.33748061,  2.14400046, -3.16'
    timestamp=(line.split(',')[0])
    a=line.split(',')[1:]
    reasult=model.predict([float(i) for i in a])

    ret=[timestamp,reasult]
    return  ret
    
    
if __name__ == "__main__":
    
    spc = SparkContext(appName="classifier")
    stc = StreamingContext(spc, 180)
    
    result=pd.DataFrame(columns=['timestamp','reasult'])
    model = pickle.load('xgboost_model.sav')
    
    lines = stc.socketTextStream("localhost", 9999)
	 ret=classify(lines,model)
	
	 ret.pprint()

    stc.start()
    stc.awaitTermination()
