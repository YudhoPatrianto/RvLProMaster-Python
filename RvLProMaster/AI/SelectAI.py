# Load Library
from RvLProMaster.EnvironmentHandler.Environment import GeminiAPI_KEY, GITHUB_ENV
from duck_chat import DuckChat
from openai import OpenAI
import google.generativeai as gemini
import base64

# Ai
class AI:
    class Gemini:
        # Gemini Text Search
        async def Text(question: str) -> str:
            try:
                gemini.configure(api_key=GeminiAPI_KEY)
                gen_conf  = {
                    'temperature': 1,
                    'top_p': 0.95,
                    'top_k': 64,
                    'max_output_tokens': 8192
                }
                gemini_models = gemini.GenerativeModel(
                    model_name='gemini-1.5-pro',
                    generation_config=gen_conf
                )
                
                # Start Gemini Text
                start_gemini = gemini_models.start_chat(
                    history=[
                    ]
                )
                response_gemini = await start_gemini.send_message_async(question)
                return response_gemini.text
            except:
                pass
            
        # Gemini Images Search
        async def Images(question: str) -> str:
            try:                
                gemini.configure(api_key=GeminiAPI_KEY)
                def UploadToGemini(path, mime_type=None):
                    file = gemini.upload_file(path, mime_type=mime_type)
                    return file
                
                conf_gemini_images = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }
                
                model_gemini_images = gemini.GenerativeModel(
                    model_name='gemini-1.5-pro',
                    generation_config=conf_gemini_images,
                )
                
                files = [
                    UploadToGemini('image.jpg', mime_type='image/jpeg')
                ]
                
                start_gemini_image = model_gemini_images.start_chat(
                    history=[
                        {
                            'role': 'user',
                            'parts': [
                                files[0],
                            ],
                        },
                    ]
                )
                
                answer = await start_gemini_image.send_message_async(question)
                return answer.text
            except:
                pass
    
    async def DuckDuckGoAI(question: str) -> str:
        """Start DuckDuckGo AI

        Args:
        
            question (str): Ask Prompt
        """
        try:
            async with DuckChat() as client_duck_ai:
                DuckChatAnswer = await client_duck_ai.ask_question(question)
                return DuckChatAnswer
        except:
            pass
        
    # Azure OpenAI
    class AzureOpenAI:
        # Text
        def Text(question: str) -> str:
            """Azure OpenAI Text Prompt

            Args:
                question (str): Your Asking Text
            """
            try:
                client_openai = OpenAI(
                    base_url="https://models.inference.ai.azure.com",
                    api_key=GITHUB_ENV
                )
                response_openai = client_openai.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": question
                        }
                    ],
                    temperature=1.0,
                    top_p=1.0,
                    max_tokens=4096,
                    model="gpt-4o-mini"
                )
                return response_openai.choices[0].message.content
            except:
                pass
        # Images
        def Images(question:str) -> str:
            """Azure OpenAI Images Search

            Parameter:
                question (str): Your Asking Text
            """
            def convToUrl(image_file: str, image_format: str) -> str:
                img_data = ""
                try:
                    # Open Image As Binary
                    with open(image_file, 'rb') as read_img:
                        img_data = base64.b64encode (read_img.read()).decode("utf-8")
                except FileNotFoundError:
                    print(f'File {image_file} Not Found')
                return f"data:image/{image_format};base64,{img_data}"
            
            client_openai = OpenAI(
                base_url="https://models.inference.ai.azure.com",
                api_key=GITHUB_ENV
            )
            
            response_openai = client_openai.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": question
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": convToUrl("image.jpg", "jpg"),
                                    "detail": "high"
                                },
                            },
                        ],
                    },
                ],
                temperature=1.0,
                top_p=1.0,
                max_tokens=4096,
                model="gpt-4o-mini"
            )
            return response_openai.choices[0].message.content