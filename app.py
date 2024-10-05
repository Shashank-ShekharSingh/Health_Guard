import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set Page Configuration

st.set_page_config(page_title="Health Guard",layout="wide")

#getting the working directory of the .py file

working_dir=os.path.dirname(os.path.abspath(__file__))

#Loading of models

diabetes_model=pickle.load(open('diabetes.pkl','rb')) # Diabetese model load

heart_model=pickle.load(open('heart.pkl','rb'))   # Heart model load

# sidebar for navigation
with st.sidebar:
             selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
       st.title('Welecom To The Diabetes Prediction Model')
       col1,col2,col3 = st.columns(3)
       #glucose = col1.slider('Label',minmum Value,Maximum Value,Default)
       glucose = col1.slider('Glucose Level',0,500,120)
       bp = col2.slider('Blood Pressure Level',0,200,100)
       skthic = col3.slider('Skin Thickness Value',0,100,20)
       insulin =col1.slider('Insulin Level',0,900,30)
       BMI=col2.slider('BMI Level',0.0,70.0,25.0)
       DPF=col3.slider('Diabetes Pedigree Function Level',0.0,2.5,0.5)
       age=col1.slider('Age',1,120,18)
       
       if st.button('Diabetes Test Result'):
             user_input=[glucose,bp,skthic,insulin,BMI,DPF,age]
             pred      =diabetes_model.predict([user_input])[0]
             diab_diagnosis = 'The person is Diabetic' if pred ==1 else 'The Person is not Diabetic'
             st.success(diab_diagnosis)

# for Heart Disease Prediction
if selected == 'Heart Disease Prediction':
     st.title('Welcome to Heart Disease Prediction Model')
     col1,col2,col3,col4 = st.columns(4)
     age=col1.slider('Age',1,120,18)
     sex=col2.radio('Gender',['Male','Female'])
     # sex=col2.slider('Gender',0,1,1)
     cp=col3.selectbox('Chest Pain Types',['Type1','Type2','Type3','type4'])
     testbps=col4.slider('Testbps',94,200,131)
     chol=col1.slider('Chol',126,564,246)
     fbs=col2.radio('Fasting Blood Sugar >120',['Yes','No'])
     # fbs=col2.slider('Fasting Blood Sugar >120',0,1,0)
     #restcg=col3.radio('Resting Electrocardiograph Results',['Normal','Abnormal'])
     #restcg=col3.slider('Resting Electrocardiograph Results',0,1,0)
     restcg=col3.radio('Resting Electrocardiograph Results',['Normal','Abnormal'])
     thalach=col4.slider('Thalach',71,202,150)
     exang=col1.radio('Exercise Induced Angina',['Yes', 'No'])
     # exang=col1.slider('Exercise Induced Angina',0,1,0)
     oldpeak=col2.slider('Old Peak',0.0,6.2,1.0)
     slop=col3.selectbox('Slop',['Upsloping','Flat','Downsloping'])
     # slop=col3.slider('Slop',0,2,0)
     ca=col4.slider('CA',0,4,1)
     #thal=col1.selectbox('Thalassemia',['Normal','Fixed Defect','Reversable Defect'])
     thal=col1.slider('Thalassemia',0,3,0)
     #Mapping Of cotegorical Data
     cp_mapping={'Type1':0,'Type2':1,'Type3':2,'Type4':3}
     slop_mapping={'Upsloping':0,'Flat':1,'Downsloping':2}
     # thal_mapping={'Normal':0,'Fixed Defect':1,'Reversable Defect':2}

     if st.button('Heart Test Result'):
            user_input=[age,1 if sex =='Male' else 0,cp_mapping[cp],testbps,chol,1 if fbs=='Yes' else 0 , 1 if restcg=='Normal' else 0 ,thalach,1 if exang=='Yes' else 0,oldpeak,slop_mapping[slop],ca,thal]
          #   user_input=[age, sex,cp,testbps,chol,fbs,restcg,thalach,exang,oldpeak,slop,ca,thal]
            pred=heart_model.predict([user_input])[0]
            result='The person is Heart Patient' if pred ==1 else 'The Person is not Heart Patient'
            st.success(result)

# For Parkinsons Prediction
if selected == 'Parkinsons Prediction':
     st.title('Parkinsons Prediction Comming Soon !!!')
     

       