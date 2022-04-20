import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # speak("hello, good morning mister simardeep   singh  my name is amelia and i am virtual assistant of suyash ")
    # speak("suyash will soon be connecting with you , will you wait for a second") 
    # speak("ok ")
    # speak("suyash is connected with you")
    # speak("enjoy your calling experience, bye") 
    speak("Activated Amelia")
    speak("i'm virtual assistant of suyash") 
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    # speak("I am Amelia Sir. Please tell me how may I help you") 
    speak("hello suyash , i am ready to take commands now")
    speak("what can i do for you")      

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        speak("recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak("say that again please") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\jarvis music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Amelia\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to suyash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend suyash oberai i am not able to send this email please try later there is a network problem")    
       
        elif 'who is suyash' in query:
                speak("suyash is my best friend and he is my creator,i help him in his work and i am always ready to take command from him ,i hope to deliver as much best results for him ")
               
        elif 'name of my parents' in query:
                speak("that's a wonderful question, suyash's father name is manish oberai, and his mother's name is kiran oberai, amritlal oberai is the grandfather of suyash, also suyash have his little sister who's name is kritika oberai, this family is the best family i met till now and all members are very good and helpful") 

        elif 'my birthday' in query:
                speak("suyash your birthday is on twenty seventh april. i'll remind you the day before and i want party also, haha jokes aside") 

        elif 'ok thanks' in query:
                speak("anytime suyash, i always love to help you")
        elif 'i like ' in query:
                speak("one of your favourite question suyash, you like gaining knowledge,  , gaming is your favourite hobby and also you like learning about new technologies. ")
        
        elif 'your name' in query:
                speak("मेरा नाम राहुल है, मेरा निर्माता सुयश है और मैं उनके निर्देशों का पालन करता हूं, वह बहुत अच्छा और बुद्धिमान लड़का है. ")
        
        elif'say hi to' in query:
                speak("ok sir")
                speak("hi all insta grammers, i'm amelia suyash's most closest friend who remain's with him all the time, and i am really grateful to have him.  ")
                speak("what else can i do for you")

        elif'stop the program' in query:
                speak("ok suyash, i always love to help ")
                speak("closing")
