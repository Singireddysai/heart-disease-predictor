import time
import streamlit as st
import pandas as pd
import joblib


rfmodel=joblib.load("model.pkl")
st.set_page_config(layout="wide", page_icon='💝', page_title="Heart_disease_predictor")

res=None
st.markdown(
        """
    <style>
         .main {
            text-align: center;
         }
         h3{
            font-size: 25px;
            font-family: Serif;
         }   
         .st-emotion-cache-16txtl3 h1 {
         font: bold 29px Serif;
         text-align: center;
         margin-bottom: 15px

         }
         div[data-testid=stSidebarContent] {
         background-color: #111;
         border-right: 4px solid #222;
         padding: 8px!important

         }

         div.block-containers{
            padding-top: 0.5rem
         }

         .st-emotion-cache-z5fcl4{
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1.1rem;
            padding-right: 2.2rem;
            overflow-x: hidden;
         }

         .st-emotion-cache-16txtl3{
            padding: 2.7rem 0.6rem
         }

         .plot-container.plotly{
            border: 1px solid #333;
            border-radius: 6px;
         }

         div.st-emotion-cache-1r6slb0 span.st-emotion-cache-10trblm{
            font: bold 24px tahoma
         }
         div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }

        div[data-baseweb=select]>div{
            cursor: pointer;
            background-color: #111;
            border: 4px solid #333
        }
        div[data-baseweb=select]>div:hover{
            border: 4px solid #49cc71

        }

        div[data-baseweb=base-input]{
            background-color: #111;
            border: 4px solid #444;
            border-radius: 5px;
            padding: 5px
        }

        div[data-testid=stFormSubmitButton]> button{
            width: 40%;
            background-color: #111;
            border: 2px solid #49cc71;
            padding: 18px;
            border-radius: 30px;
            opacity: 0.8;
        }
        div[data-testid=stFormSubmitButton]  p{
            font-weight: bold;
            font-size : 27px
        }

        div[data-testid=stFormSubmitButton]> button:hover{
            opacity: 1;
            border: 2px solid #49cc71;
            color: #fff
            font-size: 40px
        }

    </style>
    """,
        unsafe_allow_html=True
)

st.title(":white[*Heart disease predictor 💝*]",anchor="center")
st.write("")
primary_col1,primary_col2=st.columns([4,2])
with primary_col1:
    with st.form("predictor"):
        col1,col2,col3=st.columns([4,4,2])
        with col1:
            Age=st.number_input("Enter your age",1,100,value=35)
            gender=st.selectbox("Gender",["Male","Female"])
            cholesterol=st.number_input("Cholesterol",1,600,value=160)
            fastingBS=st.selectbox("Fasting blood sugar",["Less than 120 mg/dl","Greater than 120 mg/dl"])
        with col2:
            RestingBP=st.number_input("RestingBP",1,200,value=120)
            Max_Heart_rate=st.number_input("MaxHR",1,200,value=190)
            Old_peak=st.number_input("Old peak",0.0,4.5,value=0.3)
            Chest_pain_type=st.selectbox("Chest pain type",['Typical Angina','Atypical Angina','Non-Anginal Pain','Asymptomatic'])
        with col3:
            Excercise_angina=st.radio("Excercise Angina",["Yes","No"])
            st_slope=st.radio("ST slope",['Up','Flat','Down'])
            ecg=st.radio("ECG",['Normal','SVG','LVH'])

        submit=st.form_submit_button("✅Submit")

    


Age=Age
RestingBP=RestingBP
Cholesterol=cholesterol
MaxHR=Max_Heart_rate
Oldpeak=Old_peak
Sex_F=1 if gender=='Female' else 0
Sex_M=1 if gender=='Male' else 0
ChestPainType_ASY=1 if Chest_pain_type=='Asymptomatic' else 0
ChestPainType_ATA=1 if Chest_pain_type=='Atypical Angina' else 0
ChestPainType_NAP=1 if Chest_pain_type=='Non-Anginal Pain' else 0
ChestPainType_TA=1 if Chest_pain_type=='Typical Angina' else 0
FastingBS_0=1 if fastingBS=="Less than 120 mg/dl" else 0
FastingBS_1=1 if fastingBS=="Greater than 120 mg/dl" else 0
RestingECG_LVH=1 if ecg=='LVH' else 0
RestingECG_Normal=1 if ecg=='Normal' else 0
RestingECG_ST=1 if ecg=='SVG' else 0
ExerciseAngina_N=1 if Excercise_angina=='No' else 0
ExerciseAngina_Y=1 if Excercise_angina=='Yes' else 0
ST_Slope_Down=1 if st_slope=='Down' else 0
ST_Slope_Flat=1 if st_slope=='Flat' else 0
ST_Slope_Up=1 if st_slope=='Up' else 0

input_data=[[Age, RestingBP, Cholesterol, MaxHR, Oldpeak, Sex_F, Sex_M,
       ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP,
       ChestPainType_TA, FastingBS_0, FastingBS_1, RestingECG_LVH,
       RestingECG_Normal, RestingECG_ST, ExerciseAngina_N,
       ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up]]

if submit==True:
    res=rfmodel.predict(input_data)
    
with primary_col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    with st.spinner(":green[*Working on it....*]"):
        time.sleep(1.5)
        if(res==None):
            st.image('cardiology.png',width=220)
            st.subheader(":white[*Submit for Results*]")
        elif(res==1):
            st.image("hearted.png",width=220)
            st.subheader("Expected Result")
            prob=(rfmodel.predict_proba(input_data)[0][0])*100
            prob=round(prob,2)
            st.subheader(f":red[*{prob}% Heart patient*]")
        else:
            st.image("heart.png",width=220)
            st.subheader("Expected Result")
            prob=(rfmodel.predict_proba(input_data)[0][1])*100
            prob=round(prob,2)
            st.subheader(f":green[*{prob}% Not a Heart Patient*]")
        
