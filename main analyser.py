from tkinter import Tk, filedialog          # import tkinter
from textblob import TextBlob           #import textblob


# use an Enter input to proceed with analyzing
input("Press Enter to open .txt finder...")

# function to open a filedialog and import the selected file path
def open_file_dialog():
    root = Tk()         # access tkinter library
    root.withdraw()         # hide/make the library invisible

    # open filepath and accept/open the file that the user selected
    file_path = filedialog.askopenfilename()

    # Run an analysis on the .txt file that was selected
    if file_path:
        perform_sentiment_analysis(file_path)           # perform an analysis on the txt file that was selected

# Funtion to perform an analysis on the .txt file that was selected  
def perform_sentiment_analysis(file_path):          # perform the analysis on the text file
    with open(file_path, "r") as file:          # store the file path
        text = file.read()          # read the text in the selected file
        blob = TextBlob(text)           # process the text data
        polarity = blob.sentiment.polarity          # run a polarity test on the selected .txt file
        subjectivity = blob.sentiment.subjectivity          # run a subjectivity test on the selected .txt file

# print results from analysis
        print ("Friendliness Analysis Results: ")           # print the "Analysis Result" to the screen
        print ("Polarity: ",polarity)           # print the "Polarity" results to the screen
        print ("Subjectivity: ",subjectivity)           # print the "Subjectivity" results to the screen

# open file dialog to select file (ignore)
open_file_dialog()