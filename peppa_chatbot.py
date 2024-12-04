import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import random
import time
from pygame import mixer

class PeppaPigChatbot:
    def __init__(self):
        # Initialize pygame mixer for sound
        pygame.mixer.init()
        mixer.init(44100, -16, 2, 2048)
        
        # Load Peppa's responses from a dictionary
        self.responses = {
            "hello": ["*snort* Hello! I'm Peppa Pig! *giggles*", "Hi there! *snort* Want to jump in muddy puddles?"],
            "how are you": ["*snort* I'm very happy today! Want to play?", "*giggles* I'm having a wonderful day with my family!"],
            "muddy puddles": ["*splash splash* I love jumping in muddy puddles! *giggles*", "Muddy puddles are my favorite! *snort* Splash!"],
            "family": ["*happy snort* I live with Mummy Pig, Daddy Pig, and my little brother George! He loves his dinosaur!", "George goes 'Dine-Saw! Rawwwr!' *giggles*"],
            "play": ["*excited snort* Let's play together!", "*giggles* We could play with my teddy bear!", "Let's go outside and play!"],
            "friend": ["*happy snort* Suzy Sheep is my best friend! Baa!", "*giggles* I love playing with my friends!"],
            "food": ["*snort* I love spaghetti!", "*giggles* Daddy Pig makes the best pancakes!"],
            "default": ["*snort* That sounds fun!", "*giggles* Oh! How exciting!", "*happy snort* Let's tell Mummy Pig about it!"]
        }
        
        # Peppa's sound effects
        self.sound_effects = [
            "*snort snort*",
            "*giggles*",
            "*happy snort*",
            "*splash*"
        ]
    
    def add_sound_effect(self):
        """Add a random Peppa sound effect to the speech"""
        return random.choice(self.sound_effects) + " "
    
    def get_peppa_response(self, user_input):
        """Generate a Peppa Pig style response using simple pattern matching"""
        user_input = user_input.lower()
        
        # Check for keywords in user input
        for key in self.responses.keys():
            if key in user_input:
                return random.choice(self.responses[key])
        
        # If no keyword matches, return a default response
        return random.choice(self.responses["default"])
    
    def text_to_speech(self, text):
        """Convert text to Peppa Pig-like speech"""
        # Add sound effects randomly
        if not any(effect in text for effect in self.sound_effects):
            text = self.add_sound_effect() + text
        
        # Create a temporary file for the audio
        tts = gTTS(text=text, lang='en', tld='co.uk')  # British English
        audio_file = "peppa_response.mp3"
        tts.save(audio_file)
        
        # Play the audio at a higher speed to simulate Peppa's voice
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Remove the temporary audio file
        os.remove(audio_file)
        
        # Add a small delay for sound effects
        time.sleep(0.5)
    
    def peppa_sound(self):
        """Play a random Peppa Pig sound effect"""
        sound = random.choice(self.sound_effects)
        self.text_to_speech(sound)
    
    def listen(self):
        """Listen to user input via microphone"""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Peppa is listening... Say something!")
            audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Speech Recognition
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            
            # Generate Peppa's response
            peppa_response = self.get_peppa_response(user_input)
            print(f"Peppa says: {peppa_response}")
            
            # Convert response to speech
            self.text_to_speech(peppa_response)
            
        except sr.UnknownValueError:
            print("Peppa couldn't understand what you said!")
            self.text_to_speech("I didn't hear you properly. Can you say that again?")
        except sr.RequestError:
            print("Sorry, speech recognition service is unavailable")
            self.text_to_speech("Oops! Something went wrong.")
    
    def run(self):
        """Main interaction loop"""
        print("Welcome to Peppa Pig Chatbot!")
        self.text_to_speech("Hello! I'm Peppa Pig. Let's chat and have fun!")
        
        while True:
            try:
                self.listen()
                
                # Optional: Add a way to exit
                user_input = input("Want to continue? (y/n): ").lower()
                if user_input != 'y':
                    self.text_to_speech("Bye bye! See you next time! *snort*")
                    break
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break

def main():
    peppa_bot = PeppaPigChatbot()
    peppa_bot.run()

if __name__ == "__main__":
    main()
