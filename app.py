import streamlit as st
import google.generativeai as genai

genai.configure(api_key="Api Key") #Use your own api key
gemini = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")

st.title("🤖Artificial Intelligence Python Code Reviewer🤖")
st.write("Enter your python code:")

code = st.text_area("Code", height=300)

if st.button('Code Review'):
  if code.strip():
    user_prompt = f"Review the above code and provide feedback and debugging tips. ${code}"

    try:
      response=gemini.generate_content(user_prompt)
      st.markdown(response.text)

    except Exception as e:
      st.error(f"An error occurred: {e}")

  else:
    st.warning("Please enter some code to review.")