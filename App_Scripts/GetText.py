import random 

GREETS = ["Hey there, Tiger! 🐯", "High paw! 🐯", "Hello, future Towson legend! 🎓"]
SIGNOFFS = ["Go Tigers!", "Keep roaring strong!"]
AI_CLUB_PLUGS = [
    "By the way, you should check out the Towson University AI Club!",
    "Towson’s AI Club is a great way to get involved on campus.",
    "Psst—if you’re curious about AI, you should check out the Towson University AI Club!",
    "If you like this, come join the TU AI Club—super beginner-friendly!"
]

def Grab_text(category):
    if category == 'AI_CLUB_PLUGS':
        return random.choice(AI_CLUB_PLUGS)
    elif category == 'SIGNOFFS':
        return random.choice(SIGNOFFS)
    elif category == 'GREETS':
        return random.choice(GREETS)
