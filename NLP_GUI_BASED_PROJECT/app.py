from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # login gui
        self.dbo = Database()
        self.apio = API()
        self.root = Tk()     # to initialise the interface  on the screen   
        self.root.title("NLP APP")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg="#1A1A2E")
        self.login_gui()

        self.root.mainloop() # To hold the interface on the screen

    def login_gui(self):
        self.clear() 

        heading = Label(self.root,text="NLP APP",bg="#1A1A2E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("Montserrat",24,"bold"))

        label1 = Label(self.root,text="Enter Email",bg="#1A1A2E",fg="white")
        label1.pack(pady=(10,10))
        label1.configure(font=("Montserrat",11))

        self.email_input = Entry(self.root,width=45,)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter Password",bg="#1A1A2E",fg="white")
        label2.pack(pady=(10,10))
        label2.configure(font=("Montserrat",11))

        self.password_input = Entry(self.root,width=45,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text="Login",bg="#C0B9DD",width=16,height=2,command=self.perform_login )  
        login_btn.pack(pady=(10,10))
        login_btn.configure(font=("Montserrat",10))

        label3 = Label(self.root,text="Not a Member?",bg="#1A1A2E",fg="white")
        label3.pack(pady=(20,5))
        label3.configure(font=("Montserrat",10))

        redirect_btn = Button(self.root,text="Register Now",bg="#C0B9DD",command=self.register_gui)  
        redirect_btn.pack(pady=(5,5))
        redirect_btn.configure(font=("Montserrat",8))

    def register_gui(self):
        self.clear()
        
        heading = Label(self.root,text="NLP APP",bg="#1A1A2E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("Montserrat",24,"bold"))

        label0 = Label(self.root,text="Enter Name",bg="#1A1A2E",fg="white")
        label0.pack(pady=(10,10))
        label0.configure(font=("Montserrat",11))

        self.name_input = Entry(self.root,width=45,)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text="Enter Email",bg="#1A1A2E",fg="white")
        label1.pack(pady=(10,10))
        label1.configure(font=("Montserrat",11))

        self.email_input = Entry(self.root,width=45,)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter Password",bg="#1A1A2E",fg="white")
        label2.pack(pady=(10,10))
        label2.configure(font=("Montserrat",11))

        self.password_input = Entry(self.root,width=45,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn = Button(self.root,text="Register",bg="#C0B9DD",width=16,height=2,command=self.perform_registration)  
        register_btn.pack(pady=(10,10))
        register_btn.configure(font=("Montserrat",10))

        label3 = Label(self.root,text="Already a Member?",bg="#1A1A2E",fg="white")
        label3.pack(pady=(20,5))
        label3.configure(font=("Montserrat",10))

        redirect_btn = Button(self.root,text="Login Now",bg="#C0B9DD",command=self.login_gui)  
        redirect_btn.pack(pady=(5,5))
        redirect_btn.configure(font=("Montserrat",8))

    def perform_registration(self):
        # Fetch the data from the gui
        name = self.name_input.get() 
        email = self.email_input.get() 
        password = self.password_input.get() 

        response = self.dbo.add_data(name, email, password)

        if response:    
            messagebox.showinfo("Success","Registration Successful. You can login now")
        else:
            messagebox.showerror("Error","Email already exists")
             
    def perform_login(self):
        email = self.email_input.get() 
        password = self.password_input.get()
        
        response = self.dbo.search(email,password)
        if response == 1:
            messagebox.showinfo("Success","Login successfull")
            self.home_gui()
        else:
            messagebox.showerror("Error","Incorrect Email/Password")

    def home_gui(self):
        self.clear()

        heading = Label(self.root,text="NLP APP",bg="#1A1A2E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("Montserrat",24,"bold"))

        sentiment_btn = Button(self.root,text="Sentiment Analysis",bg="#C0B9DD",width=25,height=4,command=self.sentiment_gui)  
        sentiment_btn.pack(pady=(10,10))
        sentiment_btn.configure(font=("Montserrat",10))

        ner_btn = Button(self.root,text="Named Entity Recognition",bg="#C0B9DD",width=25,height=4,command=self.ner_gui)  
        ner_btn.pack(pady=(10,10))
        ner_btn.configure(font=("Montserrat",10))

        emotion_btn = Button(self.root,text="Emotion Prediction",bg="#C0B9DD",width=25,height=4,command=self.emotion_gui)  
        emotion_btn.pack(pady=(10,10))
        emotion_btn.configure(font=("Montserrat",10))

        Logout_btn = Button(self.root,text="Log Out",bg="#C0B9DD",command=self.login_gui)  
        Logout_btn.pack(pady=(5,5))
        Logout_btn.configure(font=("Montserrat",8))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root,text="NLP APP",bg="#1A1A2E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("Montserrat",24,"bold"))

        heading2 = Label(self.root,text="Sentiment Analysis",bg="#1A1A2E",fg="white")
        heading2.pack(pady=(10,20))
        heading2.configure(font=("Montserrat",16))
        
        label1 = Label(self.root,text="Enter the text",bg="#1A1A2E",fg="white")
        label1.pack(pady=(10,10))
        label1.configure(font=("Montserrat",11))

        self.sentiment_input = Entry(self.root,width=45)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

        sentiment_btn = Button(self.root,text="Analyze Sentiment",bg="#C0B9DD",command=self.do_sentiment_analysis)  
        sentiment_btn.pack(pady=(5,5))
        sentiment_btn.configure(font=("Montserrat",9))
        
        self.sentiment_result = Label(self.root,text="",bg="#1A1A2E",fg="white")
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=("Montserrat",14))
        
        goback_btn = Button(self.root,text="Go Back",bg="#C0B9DD",command=self.home_gui)  
        goback_btn.pack(pady=(5,5))
        goback_btn.configure(font=("Montserrat",8 ))


    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        
        if "error" in result:
            self.sentiment_result.config(text="⚠️ API Error: " + result["error"])
            messagebox.showerror("API Limit Reached", "You have reached the API request limit. Please wait or upgrade your plan.")
            return

        if 'scored_labels' in result:
            sentiment = result['scored_labels'][0]['label']
        elif 'label' in result:
            sentiment = result['label']
        else:
            sentiment = "Unknown"

        self.sentiment_result.config(text=f"Sentiment: {sentiment}")
    
    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP APP", bg="#1A1A2E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Montserrat", 24, "bold"))

        heading2 = Label(self.root, text="Named Entity Recognition", bg="#1A1A2E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("Montserrat", 16))

        label1 = Label(self.root, text="Enter the text", bg="#1A1A2E", fg="white")
        label1.pack(pady=(10, 10))
        label1.configure(font=("Montserrat", 11))

        self.ner_input = Entry(self.root, width=45)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text="Analyze Entities", bg="#C0B9DD", command=self.do_ner)
        ner_btn.pack(pady=(5, 5))
        ner_btn.configure(font=("Montserrat", 9))

        self.ner_result = Label(self.root, text="", bg="#1A1A2E", fg="white", wraplength=300, justify=LEFT)
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=("Montserrat", 10))

        goback_btn = Button(self.root, text="Go Back", bg="#C0B9DD", command=self.home_gui)
        goback_btn.pack(pady=(5, 5))
        goback_btn.configure(font=("Montserrat", 8))
    
    def do_ner(self):
    
        text = self.ner_input.get().strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter some text for NER.")
            return

        result = self.apio.ner(text)

        if "error" in result:
            messagebox.showerror("API Error", result["error"])
            return

        entities = result.get("entities", [])
        if not entities:
            display = "No entities found."
        else:
            display = "\n".join([
                f"{e['word']} ➜ {e['entity_group']} ({e['score']:.2f})"
                for e in entities
            ])

        self.ner_result.config(text=display)

    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP APP", bg="#1A1A2E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Montserrat", 24, "bold"))

        heading2 = Label(self.root, text="Emotion Prediction", bg="#1A1A2E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("Montserrat", 16))

        label1 = Label(self.root, text="Enter the text", bg="#1A1A2E", fg="white")
        label1.pack(pady=(10, 10))
        label1.configure(font=("Montserrat", 11))

        self.emotion_input = Entry(self.root, width=45)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(self.root, text="Predict Emotion", bg="#C0B9DD", command=self.do_emotion)
        emotion_btn.pack(pady=(5, 5))
        emotion_btn.configure(font=("Montserrat", 9))

        self.emotion_result = Label(self.root, text="", bg="#1A1A2E", fg="white", wraplength=300, justify=LEFT)
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=("Montserrat", 10))

        goback_btn = Button(self.root, text="Go Back", bg="#C0B9DD", command=self.home_gui)
        goback_btn.pack(pady=(5, 5))
        goback_btn.configure(font=("Montserrat", 8))

    def do_emotion(self):
        
        text = self.emotion_input.get().strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter some text for emotion prediction.")
            return

        result = self.apio.emotion(text)

        if "error" in result:
            messagebox.showerror("API Error", result["error"])
            return

        emotions = result.get("emotions", [])
        if not emotions:
            display = "No emotion detected."
        else:
            # Sort emotions by score (optional but cleaner)
            emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)
            display = "\n".join([
                f"{e['label'].capitalize()} ➜ {e['score']:.2f}"
                for e in emotions[:3]  # Top 3 emotions
            ])

        self.emotion_result.config(text=display)

    def clear(self):
        # Clear existing UI
            for i in self.root.pack_slaves():
                i.destroy()

nlp = NLPApp()
