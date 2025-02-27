#streamlit
import streamlit as st 

st.set_page_config(page_title= "growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflaction, challenges, and achievements! 🌟")

#quote section
st.header("Today's Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill')

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing")

#condition
if user_input:
    st.success(f"💪you're facing: {user_input}. keep pushing forword towords your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
 
else:
    st.info("Reflacting on past experience help you grow! Share your difficuities")

#acheivments
st.header("🏆 Celebrate Your Wins!")
acheivment = st.text_input("Share someting you've recently accomplished:")

if acheivment:
    st.success(f"💫 Amazing! You acieved: {acheivment}")
else:
    st.info("Big or small , every acheivement counts! Share one now! 😍")

# You would need to replace this with your actual watermark image
# For now, I'm leaving it empty as we don't have the actual watermark
watermark_base64 = ""
if watermark_base64:
    st.markdown(add_bg_from_base64(watermark_base64), unsafe_allow_html=True)

# Title
st.title("Growth Mindset Challenge with Streamlit | giaic quarter 3")

# User achievement message
st.markdown('<div class="achievement">i created the project sucessfully.</div>', unsafe_allow_html=True)

# Success message
st.markdown(
    '<div class="success-message">🎉 Amazing! You achieved: i created the project sucessfully.</div>',
    unsafe_allow_html=True
)

# Motivation button
st.markdown(
    '<button class="motivation-button">🔥 Need More Motivation?</button>',
    unsafe_allow_html=True
)

# Motivational message
st.markdown(
    '<div class="motivation-message">You\'re doing amazing! Every step counts. Keep growing and shining! 👊</div>',
    unsafe_allow_html=True
)


#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**⛔ Created by Taha Aleem**")
 
