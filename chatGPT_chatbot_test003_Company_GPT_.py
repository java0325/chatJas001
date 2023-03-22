import openai
import streamlit as st

# openai.api_key = "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"
# openai.api_key = "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"

st.title("ChatGPT와 대화하기")

messages = st.session_state.get("messages", [
    {"role": "system", "content": "You are a kind helpful assistant."},
])

for message in messages:
    st.write(f"{message['role'].capitalize()}: {message['content']}")

# user_input = st.text_input(f"User {len(messages) // 2}:") # 한줄입력
user_input = st.text_area(f"User {len(messages) // 2}:", height=50) # 여러줄 자동입력

if user_input:
    messages.append(
        {"role": "user", "content": user_input},
    )
    chat = openai.ChatCompletion.create(
        # model="gpt-4", messages=messages# gpt-4-32k-0314
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    message_str = "{:<100}".format(
        "============================================================================================================"
    )
    st.write(f"{message_str}|")

    st.session_state.messages = messages
    st.experimental_rerun()