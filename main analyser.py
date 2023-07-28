from tkinter import Tk, filedialog  # import tkinter
from textblob import TextBlob   #import textblob

input("Press Enter to open .txt finder...")

# Function to open a filedialog and import the selected file path
def open_file_dialog():
    root = Tk()
    root.withdraw()

    # Open filepath and accept/open the file that the user selected
    file_path = filedialog.askopenfilename()

    # Run an analysis on the .txt file that was selected
    if file_path:
        perform_sentiment_analysis(file_path)

# Funtion to perform an analysis on the .txt file that was selected  
def perform_sentiment_analysis(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

# To print results from analysis
        print ("Friendliness Analysis Results: ")
        print ("Polarity: ",polarity)
        print ("Subjectivity: ",subjectivity)


open_file_dialog()