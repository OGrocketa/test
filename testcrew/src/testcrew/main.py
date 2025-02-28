from crew import Pdfresearchers

def run():
    """
    Run the crew.
    """
    user_input = input("Ask your question: ")
    Pdfresearchers().crew().kickoff({"user_question":user_input})

run()