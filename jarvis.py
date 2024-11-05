from functions.offlineFunc.speechEngine import speechConfig
from functions.offlineFunc.speechJARVIS import speak
from functions.offlineFunc.greetJarvis import greet_user
from functions.offlineFunc.inputJARVIS import take_user_input
import speech_recognition as sr
from random import choice
from utilities.utils import opening_text
from pprint import pprint
###########################################################
USERNAME,BOTNAME,engine=speechConfig()

###########################################################
if __name__ == '__main__':
    greet_user(speak,USERNAME,BOTNAME,engine)
    while True:
        query = take_user_input(speak,sr,opening_text).lower()





#take_user_input(speak,sr,opening_text)