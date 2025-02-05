import streamlit as st
import openai
import base64
from openai import Client

# Initialize OpenAI API client
openai.api_key = "your_openai_api_key"
client = Client()

# Initialize session state for the thread ID if not already set
if "threadid" not in st.session_state:
    st.session_state.threadid = "your_thread_id_here"

st.title("OpenAI Image and Text Messaging App")

# Text input for your message
user_message = st.text_input("Enter your message:", "Analyze this image and tell me what's in it.")

# File uploader for the image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if st.button("Send Message"):
    thread = client.beta.threads.create()
    st.session_state.threadid = thread.id


    


    if not uploaded_file:
        st.error("Please upload an image.")
    else:
        # Read the image content and encode it to base64
        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")


        thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is the difference between these images?"
        },
        {
          "type": "image_url",
          "image_url": {"url": "https://example.com/image.png"}
        },
        {
          "type": "image_file",
          "image_file": {"file_id": uploaded_file.id}
        },
      ],
    }
  ]
)
        


'''
        response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user","content": [{"type": "text","text": "What is in this image?",},{"type": "image_url","image_url": {"url": f"data:image/jpg;base64,{image_base64}"},},],}],)
        st.write(response)

        # Construct the message payload
        message_payload = {
            "thread_id": st.session_state.threadid,
            "role": "user","content": [{"type": "text","text": "What is in this image?",},{"type": "image_url","image_url": {"url": f"data:image/jpg;base64,{image_base64}"},},]
        }

        #"type": "image_url","image_url": {"url": f"data:image/jpg;base64,{new_base64}"

        

        # Send the message
        try:
            message = client.beta.threads.messages.create(**message_payload)
            st.success("Message sent successfully!")
            st.json(message)  # Show the response
        except Exception as e:
            st.error(f"Error: {e}")
            '''
