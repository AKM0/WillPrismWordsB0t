# WillPrismWordsB0t

A Reddit Bot that formats words into prisms

This bot uses both Python and Java. 

The bot logs into Reddit and fetches comments from certain subreddits where it is allowed. It then parses the comments
for commands that explicitly call the bot. If a comment with a command is found, the specified string to be formatted is
passed to the jar with a system command. The jar formats the string and saves it to a text file. The bot replys 
the contents of this text file to the comment. The bot does the same for personal messages with commands.

The bot runs several checks as it reads comments and messages. It makes sure that the string to be formatted is not too long. It 
removes any characters that cannot be passed through a system command. It also checks to make sure that the comment/message has
an author. Finally, after a comment/message is checked it is either replied to or ignored, and the id of the comment/message
is stored to a text file of completed comments/message ids so that the bot never parses it again. After parsing all comments
and messages, the bot sleeps for 3 seconds. This reduces the CPU load on the machine. 

The formatting is possible because of ideographic unicode characters. Ideographic characters, or fullwidth characters, have the 
same width. Using a combination of fullwdith characters and a fullwidth ideographic space, the jar is able to format strings 
into cubes. 

