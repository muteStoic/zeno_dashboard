import openai
import streamlit as st

openai.api_key = "your_openai_api_key"

# File uploader in Streamlit to get the image from the user
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file:
    # Read the image data
    image_bytes = uploaded_file.read()
    
    # Create the message payload
    message_payload = {
        "thread_id": st.session_state.threadid,
        "role": "user",
        "content": [
            {"type": "text", "text": "Analyze this image and tell me if there's any text."},
            {
                "type": "image",
                "image": {
                    "bytes": image_bytes,
                    "mime_type": uploaded_file.type
                }
            }
        ]
    }

    # Send the message
    message = openai.Client().beta.threads.messages.create(**message_payload)
    
    st.write("Response from OpenAI:", message)
