# Step 1:setup streamlit
import streamlit as st
import requests

BACKEND_URL= "http://localhost:8000/ask"

st.set_page_config(page_title="SelfGuide Therapist", layout="wide")
st.title("🧘SelfGuide Therapist")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

    # Step 3:show response from backend
for msg in st.session_state.chat_history:
   with st.chat_message(msg["role"]):
       st.write(msg["content"])

# Step 2:user is able to ask question 
#chat input
user_input = st.chat_input("Hi there! I'm here to listen and support you in any way I can. how are you feeling today?")
if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    #AI agent exists here
    # Try to talk to the backend
    try:
        response = requests.post(BACKEND_URL, json={"message": user_input})
        
        if response.status_code == 200:
            # Get the data from the backend
            data = response.json()
            
            # Check if the data is a dictionary or just a string
            if isinstance(data, dict):
                content = data.get("response", "No response key found in dictionary")
            else:
                content = str(data)
            
            # Save and display the text content
            st.session_state.chat_history.append({"role": "assistant", "content": content})
            with st.chat_message("assistant"):
                st.write(content)
        else:
            # This handles backend errors (like the 403 Forbidden error)
            st.error(f"Backend Error {response.status_code}: Please check your API keys.")

    except requests.exceptions.ConnectionError:
        # This catches the 'WinError 10061' specifically
        st.error("I can't reach the backend! Make sure you ran 'python main.py' in a separate terminal.")

