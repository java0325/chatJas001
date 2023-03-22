# import streamlit as st

# import openai
# openai.api_key = "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"

# messages = [
#     {"role": "system", "content": "You are a kind helpful assistant."},
# ]

# while True:
#     message = input("User :  ")
#     if message:
#         messages.append(
#             {"role": "user", "content": message},
#         )
#         chat = openai.ChatCompletion.create(
#             # model="gpt-4", messages=messages# gpt-4-32k-0314
#             model="gpt-3.5-turbo", messages=messages 
#         )
    
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})
#      # 메시지 폭 조정
#     message_str = "{:<100}".format("============================================================================================================")
#     print(f"{message_str}|")

# 대화를 SEND버튼으로 보내어서 대화하기
# import openai
# import streamlit as st

# openai.api_key = "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"

# st.title("ChatGPT와 대화하기")

# messages = [
#     {"role": "system", "content": "You are a kind helpful assistant."},
# ]

# user_input = st.text_input("User :")
# if st.button("Send"):
#     if user_input:
#         messages.append(
#             {"role": "user", "content": user_input},
#         )
#         chat = openai.ChatCompletion.create(
#             # model="gpt-4", messages=messages# gpt-4-32k-0314
#             model="gpt-3.5-turbo", messages=messages
#         )

#         reply = chat.choices[0].message.content
#         st.write(f"ChatGPT: {reply}")
#         messages.append({"role": "assistant", "content": reply})

#         message_str = "{:<100}".format(
#             "============================================================================================================"
#         )
#         st.write(f"{message_str}|")

# 하단에 새로 대화창은 안생김
# import openai
# import streamlit as st

# openai.api_key = "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"

# st.title("ChatGPT와 대화하기")

# messages = [
#     {"role": "system", "content": "You are a kind helpful assistant."},
# ]

# user_input = st.text_input("User :")

# if user_input:
#     messages.append(
#         {"role": "user", "content": user_input},
#     )
#     chat = openai.ChatCompletion.create(
#         # model="gpt-4", messages=messages# gpt-4-32k-0314
#         model="gpt-3.5-turbo", messages=messages
#     )

#     reply = chat.choices[0].message.content
#     st.write(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})

#     message_str = "{:<100}".format(
#         "============================================================================================================"
#     )
#     st.write(f"{message_str}|")

#     st.session_state.user_input = ''
#     st.experimental_rerun()
# else:
#     for message in messages:
#         st.write(f"{message['role'].capitalize()}: {message['content']}")

## 일단 1차버전...제대로 대화...
openai

import openai
import streamlit as st

# openai.api_key = "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"
openai.api_key = "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"

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