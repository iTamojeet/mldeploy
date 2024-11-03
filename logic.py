import numpy as np
import joblib

def preprocessDataAndPredict(tv, radio, newspaper):    #put all inputs in array
    test_data = [tv, radio, newspaper]
    print(test_data)    #convert value data into numpy array and type float
    test_data = np.array(test_data).astype(float)  
    #reshape array
    test_data = test_data.reshape(1,-1)
    print(test_data) 
    #open file
    file = open("preetha.pkl","rb") 
    #load trained model
    trained_model = joblib.load(file)
    #predict
    prediction = trained_model.predict(test_data)
    return prediction    