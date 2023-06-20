import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_lottie import st_lottie
import json

st.set_page_config(
    page_title="Bizcard app",
    page_icon="📇",
)

st.title("BizcardX: Extracting Business Card Data with OCR")
st.sidebar.success("Select a page above")



# Card animation 
rain(emoji="🎈",
     font_size=54,
     falling_speed=5,
     animation_length="infinite",)

# Card GIF 
import base64

file_ = open("D:\Guvi\projects\project 3 try\Card gif1.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

# animation hello
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_coding = load_lottiefile("business card.json")

left_col , right_col  = st.columns(2)
    # animation hello  
with right_col:
     st_lottie(
     lottie_coding,
     speed=5,
     reverse=False,
     loop=True,
     quality="high",
     height = 350,
     width = 550,
     key = "coding",
     )
with left_col:
    # Card GIF 
    import base64

    file_ = open("D:\Guvi\projects\project 3 try\Card gif1.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
)



with st.expander("Project Video"):
    video = st.checkbox('show video')
    if video:
        img = open(r'C:\Users\shanm\Videos\Captures\project3_Bizcard_extraction_OCR1.mp4','rb')
        st.video(img,format='video/mp4')
