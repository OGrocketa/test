from testcrew.crew import Pdfresearchers

def run():
    """
    Run the crew.
    """
    user_input = input("Ask your question: ")
    if user_input == "e":
        exit()
    Pdfresearchers().crew().kickoff({"user_question":user_input})

# if __name__ == "__main__":
#     while True:
#         run()