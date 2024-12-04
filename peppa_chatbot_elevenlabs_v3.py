import speech_recognition as sr
import pygame
import os
import random
import time
import requests
from pygame import mixer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
if not ELEVEN_API_KEY:
    raise ValueError("ElevenLabs API key not found in environment variables")

class PeppaPigChatbot:
    def __init__(self):
        # Initialize pygame mixer for sound
        pygame.mixer.init()
        mixer.init(44100, -16, 2, 2048)
        
        # Load Peppa's responses without any sound effects
        self.responses = {
            "hello": ["Hello! I'm Peppa Pig!", "Hi there! Want to jump in muddy puddles?"],
            "how are you": ["I'm very happy today! Want to play?", "I'm having a wonderful day with my family!"],
            "muddy puddles": ["I love jumping in muddy puddles!", "Muddy puddles are my favorite!"],
            "family": ["I live with Mummy Pig, Daddy Pig, and my little brother George! He loves his dinosaur!", "George loves his dinosaur so much!"],
            "play": ["Let's play together!", "We could play with my teddy bear!", "Let's go outside and play!"],
            "friend": ["Suzy Sheep is my best friend!", "I love playing with my friends!"],
            "food": ["I love spaghetti!", "Daddy Pig makes the best pancakes!"],
            "default": ["That sounds fun!", "Oh! How exciting!", "Let's tell Mummy Pig about it!"]
        }
        
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
    
    def text_to_speech(self, text):
        """Convert text to Peppa Pig voice using ElevenLabs API"""
        try:
            print(f"Generating speech for text: {text}")
            
            # ElevenLabs API endpoint
            url = f"https://api.elevenlabs.io/v1/text-to-speech/bZQlzDd9reynpb9v4jds"
            
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": ELEVEN_API_KEY
            }
            
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }
            
            # Make API request
            response = requests.post(url, json=data, headers=headers)
            
            if response.status_code == 200:
                print("Successfully generated audio")
                
                # Save audio to temporary file
                temp_file = "temp_audio.mp3"
                with open(temp_file, "wb") as f:
                    f.write(response.content)
                print(f"Saved audio to {temp_file}")
                
                # Play audio using pygame
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                print("Playing audio...")
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                
                # Clean up temporary file
                os.remove(temp_file)
                print("Finished playing audio")
            else:
                print(f"Error: API request failed with status code {response.status_code}")
                print(f"Response: {response.text}")
            
        except Exception as e:
            print(f"Error generating speech: {e}")
            print(f"Error details: {str(e.__class__.__name__)}")
    
    def listen(self):
        """Listen for user input using microphone"""
        with sr.Microphone() as source:
            print("Peppa is listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                user_input = self.recognizer.recognize_google(audio)
                print(f"You said: {user_input}")
                return user_input
            except sr.WaitTimeoutError:
                print("No speech detected within timeout period")
                return ""
            except sr.UnknownValueError:
                print("Could not understand audio")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return ""
    
    def get_peppa_response(self, user_input):
        """Generate a Peppa Pig style response"""
        user_input = user_input.lower()
        
        # Check for matching keywords in responses
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        
        # If no keyword matches, return default response
        return random.choice(self.responses["default"])
    
    def run(self):
        """Run the chatbot"""
        print("Hello! I'm Peppa Pig!")
        self.text_to_speech("Hello! I'm Peppa Pig!")
        
        while True:
            user_input = self.listen()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Bye bye!")
                self.text_to_speech("Bye bye!")
                break
            
            if user_input:
                response = self.get_peppa_response(user_input)
                print(f"Peppa: {response}")
                self.text_to_speech(response)
            
            print("\nWant to continue? (y/n)")
            if input().lower() != 'y':
                print("Bye bye!")
                self.text_to_speech("Bye bye!")
                break

if __name__ == "__main__":
    try:
        chatbot = PeppaPigChatbot()
        chatbot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
