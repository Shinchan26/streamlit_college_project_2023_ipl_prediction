import streamlit as st
import pickle
import pandas as pd


st.sidebar.image("image/iplimages.png")
st.sidebar.image("image/image5.png")
st.sidebar.image("image/image9.png")

st.sidebar.image("image/image112.jpg")
st.sidebar.image("image/image10.jpg")



st.sidebar.header("IPL Prediction")
st.sidebar.write("The IPL, a professional Twenty20 cricket league in India, attracts viewers due to its star power, entertainment value, fast-paced format, regional pride, international fanbase, competitive balance, festive atmosphere, and digital engagement. The presence of renowned players, engaging elements like cheerleaders and music, high-scoring matches, regional rivalries, global following, competitive nature, festive timing, and widespread coverage on television and digital platforms make the IPL a highly appealing tournament for viewers.")
st.sidebar.image("image/image4.jpg")
st.sidebar.image("image/image18.jpg")
st.sidebar.image("image/image17.jpg")
st.sidebar.image("image/image13.jpg")
st.sidebar.image("image/image15.jpg")
st.sidebar.image("image/image13.jpg")
st.sidebar.image("image/image15.jpg")
st.sidebar.image("image/image11.jpg")


teams = ['Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Chennai Super Kings',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Mumbai Indians']

cities = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('KHELO DIMAG SE')

col1, col2 = st.columns(2)

with col1:
    BattingTeam = st.selectbox('Select the batting team',sorted(teams))
with col2:
    BowlingTeam = st.selectbox('Select the bowling team',sorted(teams))

selected_City = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/(balls_left)

    input_df = pd.DataFrame({'BattingTeam':[BattingTeam],'BowlingTeam':[BowlingTeam],'City':[selected_City],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(BattingTeam + "- " + str(round(win*100)) + "%")
    st.header(BowlingTeam + "- " + str(round(loss*100)) + "%")

