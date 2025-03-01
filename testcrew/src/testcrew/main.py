from testcrew.crew import Testcrew

def run():
    """
    Run the crew.
    """
    print("\n=== CrewAI Chat Interface ===")
    crew_instance = Testcrew().crew()

    while True:
        user_input = input("\n> ")
        if user_input.lower() in ["exit", "quit", "e"]:
            print("Goodbye!")
            break

        if not user_input.strip():
            continue

        response = crew_instance.kickoff({"user_question":user_input})
        print(f"\n{response}")