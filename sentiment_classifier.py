
'''

Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data 
(the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, 
which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. 
Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score 
(which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score 
(how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. 
ou will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, 
if you’re accessing this textbook from Coursera.

'''

projectTwitterData = open("project_twitter_data.csv", "r")
resultingData = open("resulting_data.csv","w")

def strip_punctuation(tweet):
    new_tweet = ""
    for i in punctuation_chars:
        if i in tweet:
            tweet = tweet.replace(i,"")
    return tweet

def get_pos(tweet):
    counter = 0
    lwr_case_tweet = strip_punctuation(tweet.lower()).split()
    for word in lwr_case_tweet:
        if word in positive_words:
            counter += 1
    return counter

def get_neg(tweet):
    counter = 0
    lwr_case_tweet = strip_punctuation(tweet.lower()).split()
    for word in lwr_case_tweet:
        if word in negative_words:
            counter += 1
    return counter

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
    

with open("project_twitter_data.csv") as proj_t:
    line = []
    for lin in proj_t:
        line.append(lin.strip()) 
        
def analyse_data(resultingData):
    resultingData.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingData.write("\n")
    
    dataLine = projectTwitterData.readlines()
    dataLine.pop(0)
    for line in dataLine:
        line = line.strip().split(',')
        resultingData.write("{}, {}, {}, {}, {}".format(line[1], line[2], get_pos(line[0]), get_neg(line[0]), (get_pos(line[0])-get_neg(line[0]))))
        resultingData.write("\n") 
                            
analyse_data(resultingData)
projectTwitterData.close()
resultingData.close()