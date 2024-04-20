import os
import openai
import streamlit as st

st.title("ChatGPT by Streamlit")

# Retrieve the API key and model name from environment variables
api_key = os.environ.get("API_KEY")
openai.api_key = api_key

chatgpt_model = os.environ.get("AI_MODEL")


# Manage model name and message history in session state
if "chatgpt_model" not in st.session_state:
    st.session_state["chatgpt_model"] = chatgpt_model
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the saved messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Receive user input
if prompt := st.chat_input("Message ChatGPT..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate the assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        formatted_messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]

        # Generate a response using the ChatGPT model
        response = openai.chat.completions.create(
            model=st.session_state["chatgpt_model"],
            messages=formatted_messages,
            max_tokens=4096
        )

        # Retrieve and display the response text
        if response.choices:
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)

        # Add the response to the session state
        st.session_state.messages.append({"role": "assistant", "content": full_response})
