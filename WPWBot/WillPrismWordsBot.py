#This python script fetches Reddit comments, parses them, and passes parsed strings to a jar file
#programmed by AKM 
#January 28, 2016 - February 6, 2016 

import praw #Python Reddit API Wrapper
import codecs #for converting from bytes to unicode
import subprocess #call jar
import time #sleeps

USER_AGENT = "This script, /u/WillPrismWordsB0T, takes strings and formats them into prisms" #information for Oauth2 
#used B0t instead of Bot because of filter
ID = ""
SECRET = ""
URL = ""
REFRESH_TOKEN = ""

FETCH_LIMIT = 100 #number of new comments to be fetched 
MAX_COMMENT_LENGTH = 16 #maximum characters in a comment for a command
MIN_COMMENT_LENGTH = 3 #minimum characters in a comment for a command
MAX_MESSAGE_LENGTH = 64 #maximum characters in a private message for a command
MIN_MESSAGE_LENGTH = 3 #minimum characters in a private message for a command

HELP_MESSAGE = "\n\n^^^[Operation](/commands)" #message to be appended to button of comment 
SUMMONS = ["/U/WILLPRISMWORDSBOT" , "/USER/WILLPRISMWORDSBOT", "/U/WPWB", "/USER/WPWB", "U/WILLPRISMWORDSBOT" , "USER/WILLPRISMWORDSBOT", "U/WPWB", "USER/WPWB"] 
#^ all possible methods of summoning bot
BAD_PHRASES  = ["~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",":",";","\"","'","<",">","?",",",".","/","\\"]
#^ characters to be removed from string 
SUBREDDITS = "botwatch"
#^ subreddits for bot to scan

def parse (body): #isolates string to be operated and removes detrimental characters that cannot be passed through command prompt ()
    body = body.split ("\"", 2) #isolates string
    if (len(body) > 1):    
        word = body[1]
        for index in range (len(BAD_PHRASES)): #removes bad characters
                word = word.replace (BAD_PHRASES[index], " ")
    elif (len (body) <= 1):
       word = ""
    
    print ("Parsed.")
    return word
        
def call_jar (args): #calls jar file and returns final product, operated string
    print ("Calling jar file")
    subprocess.call (["java.exe", "-jar", "WillPrismWordsBot.jar", args])
    output = codecs.open ("out.txt", "r", "utf-8")
    prism_string = output.read()
    output.close ()
    return prism_string.encode ("utf-8") #returns bytes 
        
      
def check_if_completed_comment (comment_id): #checks to see if comment has been operated on if yes, returns False, if no, returns True
    #print ("Checking comment if completed...")
    ids = open ("completed_comments.txt", "r")
    if comment_id in ids.read ():
        ids.close ()
        return False
    if not (comment_id in ids.read ()):
        ids.close ()
        return True

def add_to_completed_comments (comment_id): #adds ID of completed comment to save file
    ids = open ("completed_comments.txt", "a+")
    if comment_id not in ids.read ():
        ids.write (comment_id + "\n")
    ids.close ()
    print ("Comment ID stored.")
        
def check_comment_length (parsed_string): #ensures that parsed string in comment is not large or obnoxious
    print ("Checking comment length...")
    if (parsed_string is None):
        return False
    elif (len(parsed_string) > MAX_COMMENT_LENGTH) or (len (parsed_string) < MIN_COMMENT_LENGTH):
        return False
    elif (len(parsed_string) <= MAX_COMMENT_LENGTH) and (len (parsed_string) >= MIN_COMMENT_LENGTH):
        return True
    else:
        return False
        
def check_if_completed_message (message_id): #checks to see if message has been operated on if yes, returns False, if no, returns True
    #print ("Checking messages if completed...")
    ids = open ("completed_messages.txt", "r")
    if message_id in ids.read ():
        ids.close ()
        return False
    if not (message_id in ids.read ()):
        ids.close ()
        return True

def add_to_completed_messages (message_id): #adds ID of completed message to save file
    ids = open ("completed_messages.txt", "a+")
    if message_id not in ids.read ():
        ids.write (message_id + "\n")
    ids.close ()
    print ("Message ID stored.")
        
        
def check_message_length (parsed_string): #ensures that parsed string in private message is not large or obnoxious for message
    print ("Checking message length...")
    if (parsed_string is None):
        return False
    elif (len(parsed_string) > MAX_MESSAGE_LENGTH) or (len (parsed_string) < MIN_MESSAGE_LENGTH):
        return False
    elif (len(parsed_string) <= MAX_MESSAGE_LENGTH) and (len (parsed_string) >= MIN_MESSAGE_LENGTH):
        return True
    else:
        return False

def check_summons ():
    comments = subreddit.get_comments (Limit = FETCH_LIMIT) #grabs comments
    for comment in comments: #for every comment
        if check_if_completed_comment (comment.id.upper ()): #check if comment not already completed
            try: #try to catch error if comment author is deleted
                throw_error = comment.author.name
                if any (summon in comment.body.upper () for summon in SUMMONS): #check if summoned
                    parsed_string = parse (comment.body.upper ()) #assign parsed_string value to be passed to be operated
                    if (check_comment_length (parsed_string)): #if correct length
                        reply = call_jar (parsed_string) #creates reply string with bytes
                        print ("Replying...")
                        try:
                            comment.reply (reply) #reply to comment
                            add_to_completed_comments  (comment.id.upper ()) #add to completed file
                            SAME_COMMENT_NUMBER = 1
                            print ("Replied.\n")
                        except:
                            print ("Comment probably empty.")
                            add_to_completed_comments (comment.id.upper ())
                            print ("\n")
                    else:
                        add_to_completed_comments (comment.id.upper ()) #if failed adds to completed anyways
            except:
                add_to_completed_comments(comment.id.upper ()) #if author is deleted, then adds to completed anyways
                print ("No author for comment.")
                        
def check_messages (): 
    private_messages = reddit_instance.get_content("https://www.reddit.com/message/messages/", Limit = FETCH_LIMIT) #gets private messages
    for message in private_messages: #for every message
        if check_if_completed_message (message.id.upper ()): #check if message not already completed
            if any (summon in message.body.upper () for summon in SUMMONS): #check if commanded
                parsed_string = parse (message.body.upper ()) #assign parsed_string value to be passed to be operated
                if (check_message_length (parsed_string)): #if correct length
                    reply = call_jar (parsed_string)
                    try:
                        print ("Replying to Message...")
                        message.reply (reply) #reply to message
                        add_to_completed_messages (message.id.upper ()) #add to completed file
                        print ("Replied to Message.\n")
                    except:
                        print ("Message probably empty.")
                        add_to_completed_messages (message.id.upper ())
                        print ("\n")

                else:
                    add_to_completed_messages (message.id.upper ()) #if failed adds to completed anuways
                    

            
                        
print ("Logging in...") #creates reddit instance, logs in using Oauth, and grabs subreddits
reddit_instance = praw.Reddit (USER_AGENT)
reddit_instance.set_oauth_app_info (ID, SECRET, URL)
reddit_instance.refresh_access_information (REFRESH_TOKEN)
subreddit = reddit_instance.get_subreddit (SUBREDDITS)
print ("Logged in.")

print ("Beginning Loop...")

while True: #loops until manual termination
    try:
        time.sleep (3) #sleep to lower CPU usage
        check_summons () #used to check comments
        check_messages () #used to check messages
    except KeyboardInterrupt:
        print ("Program intentionally terminated.")
        exit ()

print ("Terminated.")
