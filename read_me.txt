About Project:
  #This project is used to predict real time classification of the given pair of data using ML and spark-streaming

Files:
  #Doc => contains detail overview about project, Evaluation parameters along with future cope of optimization
  #XGboost_model.py => python script to create the xgboost model using provided training data and save the model for future use
  #Spark_script.py => Script for live prediction of streaming data using spark streaming  and XGboost model.
  
To Execute:
  1  run the XGboost_model.py: this will generate a model and save it.
  2  run Spark_script : this will use the model and live data to generate the reasult.
