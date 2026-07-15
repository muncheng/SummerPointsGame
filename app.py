from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import os
from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask import session, redirect
import uuid


app = Flask(__name__)
app.secret_key = "summer-secret-key"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ADMIN_PASSCODE = "062411"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



def database():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn




# create database

conn = database()


conn.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    username_lower TEXT UNIQUE,
    points INTEGER DEFAULT 0
)
""")


conn.execute("""
CREATE TABLE IF NOT EXISTS submissions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    username_lower TEXT,

    challenge TEXT,

    points INTEGER,

    photo TEXT,

    status TEXT

)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS challenges(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    points INTEGER
)
""")

existing = conn.execute(
    "SELECT * FROM challenges"
).fetchall()


#VERY IMPORTANT: NO COMMA AT THE END OF THE LIST!!!

if len(existing) == 0:

    conn.execute("""
    INSERT INTO challenges
    (title, description, points)
    VALUES
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
        ("Start the french revolution", "yeah Im not approving none of these submissions", 670)
    """)

conn.commit()




@app.route("/")
def home():

    return render_template("index.html")




@app.route("/app")
def main():

    return render_template("app.html")




@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        passcode = request.form.get("passcode")

        if passcode == ADMIN_PASSCODE:
            session["is_admin"] = True
            return redirect("/admin")

        return """
        <script>
        alert("Wrong passcode ❌");
        window.location="/admin_login";
        </script>
        """

    return render_template("admin_login.html")


@app.route("/admin_logout")
def admin_logout():

    session.pop("is_admin", None)

    return redirect("/")

@app.route("/admin")
def admin():

    if not session.get("is_admin"):
        return redirect("/admin_login")


    db = database()

    submissions = db.execute(
        """
        SELECT *
        FROM submissions
        WHERE status='pending'
        """
    ).fetchall()


    return render_template(
        "admin.html",
        submissions=submissions
    )


@app.route("/submit_name", methods=["POST"])
def submit_name():

    username = request.form["username"].strip()


    db = database()

    username_lower = username.lower()


    existing = db.execute(
        """
        SELECT *
        FROM users
        WHERE username_lower=?
        """,
        (username_lower,)
    ).fetchone()



    if existing is None:

        db.execute(
            """
            INSERT INTO users
            (username, username_lower, points)
            VALUES (?, ?, ?)
            """,
            (
            username,
            username_lower,
            0
            )
        )

        db.commit()


    session["username"] = username


    return redirect("/challenges")




@app.route("/upload", methods=["POST"])
def upload():

    username = request.form.get("username")
    challenge = request.form.get("challenge")
    points = request.form.get("points")


    # check if photo exists
    if "photo" not in request.files:
        return "just upload the photo"


    file = request.files["photo"]


    # check if user selected a file
    if file.filename == "":
        return "picture pls"



    filename = (
    str(uuid.uuid4()) +
    "_" +
    secure_filename(file.filename)
)


    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    file.save(path)



    db = database()


    db.execute(
        """
        INSERT INTO submissions
        VALUES(NULL,?,?,?,?,?)
        """,
        (
        username,
        challenge,
        points,
        filename,
        "pending"
        )
    )


    db.commit()


    return "submitted"



@app.route("/submissions")
def submissions():


    db=database()


    data=db.execute(
    "SELECT * FROM submissions"
    ).fetchall()


    return jsonify(
        [dict(x) for x in data]
    )








@app.route("/approve/<int:id>")
def approve(id):

    db = database()


    submission = db.execute(
        """
        SELECT *
        FROM submissions
        WHERE id=?
        """,
        (id,)
    ).fetchone()



    if submission is None:
        return "Submission not found"



    # mark submission approved
    db.execute(
        """
        UPDATE submissions
        SET status='approved'
        WHERE id=?
        """,
        (id,)
    )


    print("SUBMISSION USER:", submission["username"])
    print("LOWERCASE:", submission["username"].lower())

    test = db.execute(
        """
        SELECT *
        FROM users
        WHERE username_lower=?
        """,
        (submission["username"].lower(),)
    ).fetchone()


    print("FOUND USER:", test)

    # add points
    db.execute(
        """
        UPDATE users
        SET points = points + ?
        WHERE username_lower=?
        """,
        (
        int(submission["points"]),
        submission["username"].lower()
    ))


    db.commit()


    return redirect("/admin")






@app.route("/leaderboard")
def leaderboard():

    db = database()


    users = db.execute(
        """
        SELECT *
        FROM users
        WHERE points > 0
        ORDER BY points DESC
        """
    ).fetchall()


    return render_template(
        "leaderboard.html",
        users=users
    )



@app.route("/challenges")
def challenges():

    username = session.get("username")


    if not username:

        return """
        <script>
        alert("Gurl i literally told you to enter a name");
        window.location="/";
        </script>
        """


    db = database()

    challenges = db.execute(
        """
        SELECT *
        FROM challenges
        """
    ).fetchall()


    # look up this user's latest submission per challenge
    status_map = {}

    if username:

        subs = db.execute(
            """
            SELECT challenge, status, MAX(id) as id
            FROM submissions
            WHERE username_lower=?
            GROUP BY challenge
            """,
            (username.lower(),)
        ).fetchall()

        for s in subs:
            status_map[s["challenge"]] = {
                "status": s["status"],
                "id": s["id"]
            }


    def sort_key(c):
        info = status_map.get(c["title"])
        if info is None:
            return (0, 0)          # not submitted -> stays near the top
        return (1, info["id"])     # submitted -> pushed to bottom,
                                    # most recently submitted last


    challenges = sorted(challenges, key=sort_key)


    return render_template(
        "challenges.html",
        challenges=challenges,
        username=username,
        status_map=status_map
    )


@app.route("/submit_proof", methods=["POST"])
def submit_proof():

    username = request.form.get("username")
    challenge = request.form.get("challenge")
    points = request.form.get("points")


    # check if photo field exists
    if "photo" not in request.files:

        return """
        <script>
        alert("You didnt even upload a photo");
        window.history.back();
        </script>
        """


    file = request.files["photo"]


    # check if user actually selected a file
    if file.filename == "":

        return """
        <script>
        alert("You didnt even upload a photo man");
        window.history.back();
        </script>
        """



    filename = (
        str(uuid.uuid4()) +
        "_" +
        secure_filename(file.filename)
    )


    file.save(
        os.path.join(
            UPLOAD_FOLDER,
            filename
        )
    )


    db = database()


    db.execute(
        """
        INSERT INTO submissions
        (username, username_lower, challenge, points, photo, status)

        VALUES (?,?,?,?,?,?)
        """,
        (
        username,
        username.lower() if username else None,
        challenge,
        points,
        filename,
        "pending"
        )
    )


    db.commit()


    return """
    <script>
    alert("Photo submitted! Admin will approve sometime lol. Leaderboard will auto update when i approve dw ");
    window.location="/challenges";
    </script>
    """

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )
@app.route("/notifications/<username>")
def notifications(username):

    db=database()


    approved=db.execute(
    """
    SELECT *
    FROM submissions
    WHERE username=?
    AND status='approved'
    """,
    (username,)
    ).fetchall()


    return jsonify(
        [
        {
        "message":
        f"{x['challenge']} approved +{x['points']} points "
        }

        for x in approved
        ]
    )
@app.route("/reject/<int:id>")
def reject(id):

    db = database()

    db.execute(
        """
        UPDATE submissions
        SET status='rejected'
        WHERE id=?
        """,
        (id,)
    )

    db.commit()

    return redirect("/admin")


if __name__ == "__main__":

    conn.commit()

    app.run(debug=True)