import numpy as np
import streamlit as st
import pickle 
load_model = pickle.load(open('SAVED_DIABETICS.sav','rb'))

def d_pred(input_data):
    input_arr=np.asarray(input_data)
    input_re=input_arr.reshape(1,-1)
    pred = load_model.predict(input_re)
    print(pred)
    if pred[0]==0:
        return 'NO DIABETICS'
    else:
        return'IT SEEMS YOU HAVE DIABETICS'

def main():
    st.title(' Diabetics prediction')
    
    # getting input data from user
    Pregnancies= st.text_input('Enter the number of pregnancies')
    Glucose = st.text_input('Enter Glucose level')
    BloodPressure = st.text_input('Enter BP value')
    SkinThickness = st.text_input('Enter SkinThickness value')
    Insulin = st.text_input('Enter Insulin value')
    BMI = st.text_input('Enter BMI value')
    DiabetesPedigreeFunction = st.text_input('Enter DiabetesPedigreeFunction')
    Age = st.text_input('Enter your age')
    x = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    
    # code for prediction 
    diag= ''
    # creating button for prediction
    if st.button('Test Result'):
        if len(x) == 0:
            diag = "PLEASE DONT LEAVE IT EMPTY"
        else:    
            diag = d_pred(x)
    else:
        diag = "FILL UP THE ABOVE !!!"
    st.success(diag)




if __name__ == '__main__':
    main()



