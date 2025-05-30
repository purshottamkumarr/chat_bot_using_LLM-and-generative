import os
import json

from PIL import Image

import google.generativeai as genai

# get the working directory

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

## loading the Api key

Google_Api_Key = config_data["Google_Api_Key"]

# configuring google.generative with Api Key

genai.configure(api_key=Google_Api_Key)

def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-pro")
    return gemini_pro_model

# get response from Gemini-Pro-Vision model - image/text to text
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-pro")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

# get response from embeddings model - text to embeddings
def embeddings_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(model=embedding_model,
                                    content=input_text,
                                    task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding_list

# get response from Gemini-Pro model - text to text
def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-pro")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result
