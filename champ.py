#GEN-AI Upskilling Chatbot Challenge
#Team 5 - Gen-AI Champs
#May 2024

import streamlit as champ
import pandas as pd
from io import StringIO


#Variables to use in the backend to retrieve frontEnd UI data

selectedGrade = ""
selectedCourse = ""
userQuery = ""

def main():
#-----------------------------------------------------------------------------------------------------------------
    champ.set_page_config(
        layout="wide",
        )
    
    head = champ.header("")
     #st.session_state.get('chat_log', []) -- cache chat

    logo, title = head.columns([0.05,0.95])
    with logo:
        champ.title(":robot_face:", ":color-background[White]")
    with title:
        champ.title(":purple[BiD]")  

    #-----------------------------------------------------------------------------------------------------------------
    subject = [{
        "1": "Art & Humanities",
        "2": "Science",
        "3": "Computing",
        "4": "Economics",
        "5": "Reading & Language",
        "6": "Test Prep - LSAT",
        "7": "Test Prep - SAT",
        "8": "Test Prep - MCAT",
        "9": "Test Prep - PISA",
        "10": "Math", 
        "11": "Other"  
    }]

    grade = [{
        "1": "Pre-K - 8th Grade", 
        "2": "High School", 
        "3": "College", 
        "4": "Other"
    }]

    with champ.sidebar:
        def promptStarter():
            print(f"You are a seasoned {subject} instructor who teaches at the {grade} grade level. Your student needs your help understanding what they are studying or with research. Summarize your response.")
            pass

        subject = champ.selectbox("Subject", subject[0].values(), index=None, placeholder="Select a course")

        grade = champ.selectbox("Grade", grade[0].values(), index=None, placeholder="Select a grade", on_change=promptStarter)
        
        documents = champ.file_uploader(
            "Select Sources", 
            type=["pdf", 'ppt', 'docx'], 
            accept_multiple_files=True
        )
        if documents and documents[0] is not None:
            doc = StringIO(documents[0].read().decode("ISO-8859-1"))
            #champ.write(doc)

#-----------------------------------------------------------------------------------------------------------------
    with champ.container(border=False):
        mainContainer, rightContainer = champ.columns([0.7,0.3])
        with mainContainer:
            chatWindow = champ.container(border=True, height=None)
            userInputWindow = champ.container(border=False)
            with chatWindow:
                if grade and subject:
                    selectedGrade = grade
                    selectedGrade = subject
                    chat = champ.chat_message(f"You are a seasoned {subject} instructor who teaches at the {grade} level", avatar="🤖")
                    chat.write(f":gray-background[Hello.]")

            def Submit():
                userQuery = prompt
                with chatWindow:
                    if prompt:
                        user = champ.chat_message(f"user", avatar="🙂")
                        reply = champ.chat_message(f"ai", avatar="🤖")
                        if prompt: #while?
                            user.write(f":green-background[{prompt}]")
                        else:
                            user.write(prompt)
                            reply.write(f":gray-background[AI Reply]")
                    #input container - user enters their question/prompt here
            
            with userInputWindow:
                prompt=[]

                userInput = champ.text_area(
                    height=200,
                    label="userInput",
                    placeholder=f"Tell me how can I help you today?",
                )
            
                PrePrompts = [
                    {
                        "Art & Humanities": 
                            [
                                "Who was Shakespeare?", 
                                "What is personification?"
                            ],
                    
                        "Science" : 
                            [
                                "What is Osmosis?", 
                                "Is Pluto a planet?"
                            ]
                    }
                ]
                for pre in [PrePrompts[0]]:
                    list = [*dict.values([pre][0])]
                    userPrompt = champ.selectbox("Select a prompt: ", *[list], index=None, placeholder="Start Here?")

                if userInput:
                    prompt = userInput
                else:
                    prompt=userPrompt
            
            #generate button
            btn = champ.button("Generate", type="primary", use_container_width=True, on_click=Submit)

#-----------------------------------------------------------------------------------------------------------------
        with rightContainer:
            with champ.container(height=660):
                with champ.container(
                    border=False,
                    height=350
                    ):
                    champ.image(
                        image="https://ugokawaii.com/wp-content/uploads/2022/08/owl-teacher.gif", 
                        use_column_width=True,
                    )
#https://www.presentermedia.com/powerpoint-animation/scribbles-teaching-student-pid-22511
                champ.divider()
                    #static image of black board tools
                with champ.container(
                    border=False,
                    height=320
                ):
                    canvasArea = champ.image(
                        image='imgs/board.png',
                        use_column_width=True
                    )
                    
if __name__=='__main__':
    main()