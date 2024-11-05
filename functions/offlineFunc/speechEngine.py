import pyttsx3,os
from dotenv import load_dotenv
load_dotenv()
def speechConfig():
    USERNAME = os.getenv('USER')
    BOTNAME = os.getenv('BOTNAME')

    engine = pyttsx3.init('sapi5')

    # Set Rate
    engine.setProperty('rate', 180)

    # Set Volume
    engine.setProperty('volume', 5.0)

    # Set Voice (Female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    return USERNAME,BOTNAME,engine
