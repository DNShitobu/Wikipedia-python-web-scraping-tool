import wikipedia
import pyttsx3
speaker = pyttsx3.init()
user_input=input("Vihimi Wikipedia: ")
wiki=wikipedia.summary(user_input, "")
print (wiki)
speaker.say(wiki)
speaker.runAndWait()

