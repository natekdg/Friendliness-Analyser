from tkinter import Tk, filedialog  # import tkinter
from textblob import TextBlob   #import textblob
# Function to open a filedialog and import the selected file path
def open_file_dialog():
    root = Tk()
    root.withdraw()

    # Open filepath and accept/open the file that the user selected
    filepath = filedialog.askopenfilename

    # Run an analysis on the .txt file that was selected
    if filepath:
        perform_sentiment_analysis(file_path)

# Funtion to perform an analysis on the .txt file that was selected  
def perform_sentiment_analysis(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity


