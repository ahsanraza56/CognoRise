from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from tkinter import *

def clearAll():
    negativeField.delete(0, END) 
    neutralField.delete(0, END) 
    positiveField.delete(0, END) 
    overallField.delete(0, END) 
    textArea.delete(1.0, END)
    
def detect_sentiment():
    sentence = textArea.get("1.0", "end")
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 

    negativeField.insert(10, str(sentiment_dict['neg']*100) + "% Negative")
    neutralField.insert(10, str(sentiment_dict['neu']*100) + "% Neutral")
    positiveField.insert(10, str(sentiment_dict['pos']*100) + "% Positive")

    if sentiment_dict['compound'] >= 0.05:
        overallField.insert(10, "Positive")
    elif sentiment_dict['compound'] <= -0.05:
        overallField.insert(10, "Negative")
    else:
        overallField.insert(10, "Neutral")

if __name__ == "__main__":
    gui = Tk() 
    gui.config(background="light green") 
    gui.title("Sentiment Detector") 
    gui.geometry("250x400") 

    enterText = Label(gui, text="Enter Your Sentence", bg="light green")
    textArea = Text(gui, height=5, width=25, font="lucida 13")
    check = Button(gui, text="Check Sentiment", fg="Black", bg="Red", command=detect_sentiment)
    negative = Label(gui, text="sentence was rated as: ", bg="light green") 
    neutral = Label(gui, text="sentence was rated as: ", bg="light green") 
    positive = Label(gui, text="sentence was rated as: ", bg="light green")
    overall = Label(gui, text="Sentence Overall Rated As: ", bg="light green")
    negativeField = Entry(gui)
    neutralField = Entry(gui)
    positiveField = Entry(gui)
    overallField = Entry(gui) 
    clear = Button(gui, text="Clear", fg="Black", bg="Red", command=clearAll)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    enterText.grid(row=0, column=2)
    textArea.grid(row=1, column=2, padx=10, sticky=W)
    check.grid(row=2, column=2)
    negative.grid(row=3, column=2)
    neutral.grid(row=5, column=2)
    positive.grid(row=7, column=2)
    overall.grid(row=9, column=2)
    negativeField.grid(row=4, column=2)
    neutralField.grid(row=6, column=2)
    positiveField.grid(row=8, column=2)
    overallField.grid(row=10, column=2)
    clear.grid(row=11, column=2)
    Exit.grid(row=12, column=2)

    gui.mainloop()
