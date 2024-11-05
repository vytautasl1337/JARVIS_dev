from datetime import datetime

def greet_user(speak,USERNAME,BOTNAME,engine):
    """Greets the user according to the time"""
    hour = datetime.now().hour
    print(hour)
    if (hour >= 4) and (hour < 12):
        speak(f"Good morning {USERNAME}",engine)
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}",engine)
    elif (hour >= 16) and (hour < 20):
        speak(f"Good evening {USERNAME}",engine)
    elif (24 > hour >= 20) or (0 >= hour > 3):
        speak(f"Good night {USERNAME}",engine)
    speak(f"How may I be of service?",engine)