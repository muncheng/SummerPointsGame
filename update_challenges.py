import sqlite3
import os

#RUN TO UPDATE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

conn = sqlite3.connect(DB_PATH)



conn.execute("DELETE FROM challenges")

conn.executemany(
    "INSERT INTO challenges (title, description, points) VALUES (?, ?, ?)",
    [
        ("Touch grass", "yes", 1),
        ("get 10+ hours of screen time", "great job", 1),
        ("ponder", "deep", 1),
        ("sleep 10+ hours", "first of all i promise im not freaky, second of all idk how im gonna verify ts so whatever", 1),
        ("Chud around", "by Amanda 2026", 2),
        ("Walk around aimlessly", "like the sad little chud you are", 2),
        ("Watch fifa and cry about it", "idk messi v ronaldo or sth i dont ball😭✌️✌️🫃🫃🫃🫃🫃🫃", 2),
        ("Acquire a water gun", "easy points", 2),
        ("Eat good food🫃", "self explanatory, must make admin jealous", 5),
        ("do chores", "parent propaganda", 5),
        ("sit on a train", "nice", 5),
        ("Go to McD", "big mac", 5),
        ("Eat ice cream", "big back", 5),
        ("Eat jelly", "big back", 5),
        ("take aesthetic summer photos","tea", 5),
        ("Catfish someone", "lol", 5),
        ("Hangout w friends🤑", "unless you're antisocial or sth", 5),
        ("Play sports", "sounds summer-y idk", 5),
        ("Do origami", "i ran out of ideas", 5),
        ("Work on your hobby", "NO SPORTS cuz its cheating, music/art/anything", 5),
        ("Go swimming with friends", "sounds fun idk", 10),
        ("Binge a tv series/movei", "rip", 10),
        ("Interact with an animal", "dog or cat or sth", 10),
        ("ponder about life and be filled with an uncanny sensation of existential dread as you come to the realisation that we are barreling towards an abyysal future with no recourse", "deep shi", 10),
        ("Celebrate a bday", "your own or others", 10),         
        ("Go to the beach", "i like eating sand", 10),
        ("Have a picnic", "so preppyy", 10),
        ("Eat bbq", "any type is fine", 10),
        ("Read a book and finish it", "good job", 10),
        ("Have a sleepover", "slay", 10),
        ("Go watch a movie in cinemas", "backroomsss",10),
        ("Walk 10,000+ steps in a day", "these sweats bru",10),
        ("Go karaoke with friends", "lmaooo", 10),
        ("Make a summer scrapbook", "can you tell i ran out of ideas", 10),
        ("attend and survive a family reunion", "good luck", 10),
        ("Dye your hairrrrrrr", "dye yo hair neon green pls", 15),
        ("Build a lego set", "anything", 15),
        ("hunt for a rainbow", "pride month is over gng", 15),
        ("Get your nails done", "how do u wipe your ahh", 15),
        ("Bake something", "give me some pls", 15),
        ("Decorate a cake", "give me some pls", 15),
        ("lock in and study", "Igs are NEXT YEAR PEOPLE", 15),
        ("Roll down a hill", "its just funny", 20),
        ("stand in the rain", "its just funny", 20),
        ("visit a museum", "dinocaur", 20),
        ("find a potato shaped rock", "slay", 20),
        ("Learn a new dance", "soda pop", 20),  
        ("Visit another country", "lowkey pay to win lmao", 25),
        ("cuti cuti malaysia", "for the broke homies", 25),
        ("Watch the sunrise", "wow so romantic", 25),
        ("Go camping", "should have put tw for the IA survivors", 25),
        ("go to a music festival/concert", "good job", 25),
        ("make a tinfoil hat and wear it", "good job", 25),
        ("Lose your dior blush", "consider the points as a financial compensation", 25),
        ("attend a live sport event", "rich", 30),
        ("beat a video game", "nice", 30),
        ("get a j*b", "🥀", 50),
        ("Learn blender/davinci resolve/affinity/PS", "mad respect", 50),
        ("get a bf or gf", "romcom ahh", 50),
        ("breakup🥀", "relationship might be over but atleast u get points", 50),
        ("experience a tragic death", "rip", 50),
        ("become a hello kitty pyjama girl/performative matcha drinking male/finance bro", "sacrifices were made", 50),
        ("learn to swim", "good job", 50),
        ("make a silly summer movie", "cuz why not", 50),
        ("get a neon orange mowhawk", "if yall caught the ref gj", 50),
        ("perform on stage(sing/dance/something idk)", "good job", 50),
        ("learn how to do makeup", "mad respect and also pls pls pls give me a disney coded baddie makeover🤑🤑🤑", 50),
        ("Build a big lego set", "millenium falcon sized", 67),
        ("make a song", "soty", 67),
        ("set off the fire alarm", "hopital", 67),
        ("Join the army", "dont die", 67),
        ("commit arson", "just to clarify im not endorsing violence, sue me", 100),
        ("photoshop yourself to weird places", "i need a good laugh", 100),
        ("gamble and lose your money", "womp womp", 100),
        ("set off a bomb", "good job", 100),
        ("Submit whatever", "If you impress me i'll give it to you lmao", 100),
        ("Become a crypto broker", "dont buy btc", 100),
        ("Fly a plane/rocket", "plane", 100),
        ("Replace zak brown at mcl","respect", 670),
        ("Become a femboy","so kawaii", 670),
        ("Start the french revolution", "yeah Im not approving none of these submissions", 670),
        ("flush yourself down the toilet", "lol", 670),
        ("get on a magazine front cover", "good luck", 670)
        
        
    ]
)

conn.commit()
conn.close()

print("Challenges updated!")