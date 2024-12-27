import os

import streamlit as st
from helpers import get_openai_response



# Streamlit page config
st.set_page_config(
    page_title="Sales Call Support Chatbot",
    page_icon="",
    layout="wide"
)

st.title("Chat with Call Mentor")



# Appending Initial message
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {
            "role": "assistant",
            "content": "How can I help you?"
         }
    ]

# Rendering existing messages
for message in st.session_state.chat_history:
    if 'df_content' in message:
        st.chat_message(message["role"]).dataframe(
            message["df_content"], hide_index=True)
    else:
        st.chat_message(message["role"]).write(message["content"])


# user input question placeholder
user_question = st.chat_input(placeholder="Ask me about your data!")


if user_question:
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_question
        }
    )
    st.chat_message("user").write(user_question)

    #Step 2

    with st.spinner("Looking for a appropriate solution..."):
        # Get the SQL Query corresponding to user question
        response_from_gpt = get_openai_response(st.session_state.chat_history)
        if response_from_gpt:

            # save the query result in session state
            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": response_from_gpt
                }
            )

            # display the query result
    
    st.chat_message("assistant").write(response_from_gpt)
    # st.chat_message("prompt").write(st.session_state.chat_history)
  