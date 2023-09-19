import streamlit as st
import numpy as np
import pickle


loadmodel = pickle.load(open('/Users/sowmi/Downloads/student_performance_prediction/trainedmodel.sav','rb'))

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://st3.depositphotos.com/2769299/19240/i/450/depositphotos_192407628-stock-photo-library-abstract-blurred-background.jpg");
             background-attachment: fixed;
             background-size: cover;
             }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


def grade_prediction(input_data):
    
    inputarray = np.asarray(input_data)

    #inputreshape = inputarray.reshape(1,-1)

    prediction = loadmodel.predict(inputarray)
    
    t = ((np.round(prediction)).astype(int))
    
    if (t==1):
        return 'Pass'
    if (t==0):
        return 'Fail'



def main():
    
    st.markdown(
    """
    <style>
    .title {

        top: 5%;
        left: 0;
        width: 100%;
        padding: 2px;
        font-size: 20px;
        font-weight: bold;
        z-index: 9999;
    }
    .block-container {
        padding-top: 3%;
        margin-top:1%;
        }
    p{
       color: white;
       }
    .css-1n543e5 edgvbvh10{
        color:black;
        }
    .css-1vbkxwb e16nr0p34{
        color: red;}
    </style>
    """,
    unsafe_allow_html=True
    )
    ttle = 'Student Performance Prediction'
    
    ttle = f'<div class = "title"><span style="color: #FFFFFF; font-size: 55px; font-weight: bold;">{ttle}</span></div>'
    
    
    st.markdown(ttle, unsafe_allow_html=True)
    
    #'school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',
       #'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',
       #'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       #'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       #'Walc', 'health', 'absences', 'passed'
    
    
    


    option = ['','GP','MS']
    school = st.selectbox('School', option, index = 0)
    option = ['','M','F']
    sex = st.selectbox('Gender', option, index = 0)
    age=st.text_input("Age")
    option = ['','U','R']
    address = st.selectbox('Address', option, help = '"U" - Urban or "R" - Rural', index = 0)
    option = ['','LE3','GT3']
    Famsize = st.selectbox('Family Size', option, index = 0, help = '"LE3" - less or equal to 3 or "GT3" - greater than 3')
    option = ['','T','A']
    Pstatus = st.selectbox("Parent's Status", option, index = 0, help = '"T" - Together or "A" - Apart')
    option = ['','0','1','2','3','4']
    Medu = st.selectbox("Mother's Education Level", option, index = 0, help = '0 - None, 1 - Primary Education, 2 - 5th to 9th Grade, 3 - Secondary Education or 4 - Higher Education')
    Fedu = st.selectbox("Father's Education Level", option, index = 0, help = '0 - None, 1 - Primary Education, 2 - 5th to 9th Grade, 3 - Secondary Education or 4 - Higher Education')
    option = ['','health','services','at_home','other']
    Mjob = st.selectbox("Mother's Job", option, index = 0, help = 'Teacher, Healthcare related, Civil Services (e.g. Administrative or Police), Stay at Home or Other')
    Fjob = st.selectbox("Father's Job", option, index = 0, help = 'Teacher, Healthcare related, Civil Services (e.g. Administrative or Police), Stay at Home or Other')
    option = ['','home','reputation','course','other']
    reason = st.selectbox("Reason to choose this school", option, index = 0, help = 'Close to home, Reputation of the School, Course preference or Other')
    option = ['','mother','father','other']
    guardian = st.selectbox("Student's Guardian", option, index = 0)
    option = ['','1','2','3','4']
    traveltime = st.selectbox("Travel Time", option, index = 0, help = '1 - Less than 15 minutes, 2 - 15 to 30 minutes, 3 - 30 minutes to 1 hour, or 4 - More than 1 hour')
    studytime = st.selectbox("Study Time", option, index = 0, help = '1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours')
    option = ['','0','1','2','3']
    failures = st.selectbox("Number of past class Failures", option, index = 0, help = 'Failure count 0 - 2 or else 3')
    option = ['','yes','no']
    schoolsup = st.selectbox("Extra Educaitonal Support", option, index = 0)
    famsup = st.selectbox("Family Educational Support", option, index = 0)
    paid = st.selectbox("Paid", option, index = 0, help= 'Extra paid classes within the course subject')
    activities = st.selectbox("Extra Curricular Activities", option, index = 0)
    nursery = st.selectbox("Attended Nursery School", option, index = 0)
    higher = st.selectbox("Higher", option, index = 0)
    internet = st.selectbox("Internet access at home", option, index = 0)
    romantic = st.selectbox("Relationship Status", option, index = 0)
    option = ['','1','2','3','4','5']
    famrel = st.selectbox("Family Relationship", option, index = 0, help = 'From 1 - Very Bad to 5 - Excellent')
    freetime = st.selectbox("Free Timeafter School", option, index = 0, help = 'From 1 - Very Low to 5 - Very High')
    goout = st.selectbox("Go Out", option, index = 0, help = 'From 1 - Very Low to 5 - Very High')
    dalc = st.selectbox("Workday Alcohol Consumption", option, index = 0, help = 'From 1 - Very Low to 5 - Very High')
    walc = st.selectbox("Weekend Alcohol Consumption", option, index = 0, help = 'From 1 - Very Low to 5 - Very High')
    health = st.selectbox("Health Condition", option, index = 0, help = 'From 1 - Very Bad to 5 - Excellent')
    absences = st.text_input("Absenses", help = 'From 0 to 93')
    
    
    

  
    feature1_mapping = {"no": 0, "yes": 1}
    feature2_mapping = {'mother': 0, 'father': 1, 'other': 2}
    feature3_mapping = {'home': 0, 'reputation': 1, 'course': 2, 'other': 3}
    feature4_mapping = {'teacher': 0, 'health': 1, 'services': 2, 'at_home': 3, 'other': 4}
    feature5_mapping = {'T': 0, 'A': 1}
    feature6_mapping = {'LE3': 0, 'GT3': 1}
    feature7_mapping = {'U': 0, 'R': 1}
    feature8_mapping = {'M': 0, 'F': 1}
    feature9_mapping = {'GP': 0, 'MS': 1}
    
    
    
    
    
    school = feature9_mapping.get(school, school)
    sex = feature8_mapping.get(sex, sex)
    address = feature7_mapping.get(address, address)
    Famsize = feature6_mapping.get(Famsize, Famsize)
    Pstatus = feature5_mapping.get(Pstatus, Pstatus)
    Mjob = feature4_mapping.get(Mjob, Mjob)
    Fjob = feature4_mapping.get(Fjob, Fjob)
    reason = feature3_mapping.get(reason, reason)
    guardian = feature2_mapping.get(guardian, guardian)
    schoolsup = feature1_mapping.get(schoolsup, schoolsup)
    famsup = feature1_mapping.get(famsup, famsup)
    paid = feature1_mapping.get(paid, paid)
    activities = feature1_mapping.get(activities, activities)
    nursery = feature1_mapping.get(nursery, nursery)
    higher = feature1_mapping.get(higher, higher)
    internet = feature1_mapping.get(internet, internet)
    romantic = feature1_mapping.get(romantic, romantic)
    
    
    
    result = ''
    
    #'school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',
       #'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',
       #'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       #'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       #'Walc', 'health', 'absences'
    
    if st.button("Predict Performance"):
        
        result = grade_prediction([[int(school),int(sex), int(age), int(address), int(Famsize), int(Pstatus), int(Medu), int(Fedu), int(Mjob), int(Fjob), int(reason), int(guardian),int(traveltime), int(studytime), int(failures), int(schoolsup), int(famsup), int(paid), int(activities), int(nursery), int(higher), int(internet), int(romantic), int(famrel), int(freetime), int(goout), int(dalc), int(walc), int(health), int(absences)]])
        
    if(result == 'Pass' or result == 'Fail'):
        result = 'Predicted Result of the Student:  ' + result
        
        result = f'<span style="color: #ffffff; font-size: 40px; font-weight: bold;">{result}</span>'
        
    
        st.markdown(result, unsafe_allow_html=True)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
        
        
        
        
         
