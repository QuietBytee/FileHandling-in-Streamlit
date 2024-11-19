import streamlit as st
import pandas as pd

st.subheader("Upoading the CSV file : ")
df=st.file_uploader("Upload your CSV file here : ",type=['csv','xlsx'])
if df is None:
    st.markdown("###### Loading the CSV file... ")
else:
    st.dataframe(pd.read_csv(r'C:\Users\dell\Desktop\dataScience\Streamlit\products.csv').head())

st.subheader("Dealing with images directly")
st.image(r'C:\Users\dell\Desktop\dataScience\Streamlit\To_close_streamlit.PNG')


st.subheader("Dealing with images by uploading")
img = st.file_uploader("Upload the Image file : ",type=['PNG','jpeg'])
if img is not None:
    st.image(img)

st.subheader('Working with video files...')
video = st.file_uploader("Upload the Video file : ",type=['mkv','mp4','wmv'])
if video is not None:
    st.video(video,start_time=0)

st.subheader('Working with audio files...')
audio = st.file_uploader("Upload the Audio file : ",type=['mkv','mp3','wav'])
if audio is not None:
    st.video(audio,start_time=0)
