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
        ("Acquire a water gun", "easy points", 2),
        ("Eat good food🫃", "self explanatory, must make admin jealous", 5),
        ("Go to McD", "big mac", 5),
        ("take aesthetic summer photos","tea", 5),
        ("Catfish someone", "lol", 5),
        ("Hangout w friends🤑", "unless you're antisocial or sth", 5),
        ("Play sports", "sounds summer-y idk", 5),
        ("Work on your hobby", "NO SPORTS cuz its cheating, music/art/anything", 5),
        ("Go swimming with friends", "sounds fun idk", 10),
        ("Celebrate a bday", "your own or others", 10),         
        ("Go to the beach", "i like eating sand", 10),
        ("Have a picnic", "so preppyy", 10),
        ("Eat bbq", "any type is fine", 10),
        ("Have a sleepover", "slay", 10),
        ("Go karaoke with friends", "lmaooo", 10),
        ("Make a summer scrapbook", "can you tell i ran out of ideas", 10),
        ("attend and survive a family reunion", "good luck", 10),
        ("Dye your hairrrrrrr", "dye yo hair neon green pls", 15),
        ("Get your nails done", "how do u wipe your ahh", 15),
        ("Bake something", "give me some pls", 15),
        ("lock in and study", "Igs are NEXT YEAR PEOPLE", 15),
        ("Visit another country", "lowkey pay to win lmao", 25),
        ("cuti cuti malaysia", "for the broke homies", 25),
        ("Watch the sunrise", "wow so romantic", 25),
        ("Go camping", "should have put tw for the IA survivors", 25),
        ("go to a music festival/concert", "good job", 25),
        ("attend a live sport event", "rich", 30),
        ("get a j*b", "🥀", 50),
        ("Learn blender/davinci resolve/affinity/PS", "mad respect", 50),
        ("get a bf or gf", "romcom ahh", 50),
        ("breakup🥀", "relationship might be over but atleast u get points", 50),
        ("learn to swim", "good job", 50),
        ("get a neon orange mowhawk", "if yall caught the ref gj", 50),
        ("commit arson", "just to clarify im not endorsing violence, sue me", 100),
        ("Replace zak brown at mcl","respect", 670),
        ("Start the french revolution", "yeah Im not approving none of these submissions", 670),
        
        
    ]
)

conn.commit()
conn.close()

print("Challenges updated!")