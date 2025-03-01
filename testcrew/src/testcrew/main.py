from testcrew.crew import Testcrew
import gradio as gr
import shutil, os




def chat(user_message, history):
    response = crew_instance.kickoff({"user_question": user_message})
    return response

def process_file(uploaded_files):
    pdf_dir = "../../../knowledge"
    for uploaded_file in uploaded_files:
        file_name = os.path.basename(uploaded_file)
       
        dest_path = os.path.join(pdf_dir, file_name)
        
        shutil.copyfile(uploaded_file, dest_path)
    return "Files uploaded successfully you can start asking questions now"

crew_instance = Testcrew().crew()

with gr.Blocks() as demo:

    file_upload = gr.Interface(
        fn = process_file,
        inputs = gr.File(label="Upload PDFs", file_types=[".pdf"], file_count="multiple"),
        outputs = gr.Textbox(value="Submit PDF's to ask about them", label="Upload Status")
    )

    chat_interface = gr.ChatInterface(
        fn = chat,
        title = "PDF Chatbot",
        description = "Ask questions about your PDF",
        type = "messages",
        save_history = True
    )

def run():
    """
    Run the crew.
    """
    demo.launch()
   