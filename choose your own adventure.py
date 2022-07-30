#Choose Your Own Adventure

answer = (input("Hi. This is a choose your own adventure story. Would you like to play? (yes/no) "))
if answer.lower() == "no":
    print(":/ ok bye")
if answer.lower() == "yes":

    print("""
You are sitting in your home after a rainstorm watching tv.
It is 8pm on July 30th. 
The sun is shining through the edges of the clouds and creating a spectacular sunset.
Do you go outside to take a picture of the sunset or do you stay inside and continue watching tv?""")

    answer = input("Go outside/stay inside? ")

if answer.lower() == "go outside":

    print("""
You head outside and stand in the fresh, post rain evening. 
The sunset is even more beautiful than you saw from inside. 
You spend three minutes taking pictures of the sky from different angles. 
A flock of geese pass by overhead and create dark imprints against the orange and pink clouds.  
You then head back inside. Before you start watching tv again you check your phone.
There is a missed call from 281-357-7761 and a voicemail. 
Do you check the voicemail or delete without listening?
""")
    answer = input("do you check the voicemail or delete without listening? (delete/check): ")
if answer.lower() == "delete":
    print("thanks for playing")
if answer.lower() == "check":
    print("""
You hear the following, in slight electronic distortion:
My name is Holly Sands. I’m on the International Space Station. I know that sounds crazy but it's true.
There’s been an accident. I don’t know what happened.  I’m trapped here and I’m alone.
I can’t make contact with NASA. I can’t reach anyone. 
if you are receiving this I need you to make contact with NASA.
Tell them Astronaut Holly Sands is in distress. 
My personal ID is MXCB170. That’s Mike… X-Ray… Charlie,…Bravo…170.  
""")

if answer.lower() == "stay inside":
    print("""
Your phone lights up with a call and you check it. 
It says spam likely and you toss it back on the couch.  
2 minutes later your phone tells you you have a voicemail.
""")

answer = input("do you check the voicemail or delete without listening? (delete/check): ")
if answer.lower() == "delete":
    print("thanks for playing")
if answer.lower() == "check":
    print("""
You hear the following, in slight electronic distortion:
My name is Holly Sands. I’m on the International Space Station. I know that sounds crazy but it's true.
There’s been an accident. I don’t know what happened.  I’m trapped here and I’m alone.
I can’t make contact with NASA. I can’t reach anyone. 
if you are receiving this I need you to make contact with NASA.
Tell them Astronaut Holly Sands is in distress. 
My personal ID is MXCB170. That’s Mike… X-Ray… Charlie,…Bravo…170.  
""")
