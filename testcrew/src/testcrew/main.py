from testcrew.crew import Testcrew
import gradio as gr
import shutil, os



def run():
    """
    Run the crew.
    """
    crew = Testcrew().crew()
    print("Crew is ready to answer your questions.")
    while True:
        question = input(">")

        if question == "e":
            break

        print(crew.kickoff({"user_question":question}))

   