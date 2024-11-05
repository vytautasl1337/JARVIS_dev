# Text to Speech Conversion
def speak(text,engine):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()