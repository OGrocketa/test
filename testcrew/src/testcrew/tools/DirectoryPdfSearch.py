from crewai.tools import tool
from crewai_tools import PDFSearchTool
import os
#TODO: Instead of using tools convert into vector store by hand and then just retrieve using
# langchain embeddings  each time
# Instead of using tools 

@tool("DirectoryPdfSearch")
def directory_pdf_search(query: str) -> str:
    """
    Search through PDF files in a specified directory and return relevant content.
    
    Args:
    query (str): The search query to look for in the PDF files.
    
    Returns:
    str: A string containing relevant data found in each PDF file.
    """
    directory = "/Users/yaraslausedach/Code/test/testcrew/knowledge/"
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    
    results = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        pdf_tool = PDFSearchTool(pdf=pdf_path)
        result = pdf_tool.kickoff(query)
        if result:
            results.append(f"From {pdf_file}:\n{result}\n")
    
    return "\n".join(results) if results else "No relevant information found."
