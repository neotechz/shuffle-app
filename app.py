# PACKAGE IMPORTS & INITIALIZATION

from flask import Flask, render_template, redirect, jsonify, request, session
from flask_session import Session


from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.orm import sessionmaker, declarative_base


from datetime import datetime
import uuid, os


app = Flask(__name__, static_folder ="static")
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SESSION_TYPE'] = 'filesystem'


db_path = "local.db"
engine = create_engine(f"sqlite:///{db_path}")
Base = declarative_base()


# DATABASE CLASSES & RELATED METHODS

def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "user"
    id = Column("id", String, primary_key = True, default = generate_uuid)
    username = Column("username", String)
    name = Column("name", String)
    num_decks = Column("num_decks", Integer, default = 0)
    datetime_created = Column("datetime_created", Integer)
    datetime_updated = Column("datetime_updated", Integer)
    datetime_login = Column("datetime_login", Integer)
    hash = Column("hash", String, nullable = True)
    role = Column("role", String)

    def __init__(self, username, name, datetime_now, hash = None, role = "user"):
        self.username = username
        self.name = name
        self.hash = hash
        self.datetime_created = datetime_now
        self.datetime_updated = datetime_now
        self.datetime_login = datetime_now
        self.role = role


class Deck(Base):
    __tablename__ = "deck"
    id = Column("id", String, primary_key = True, default = generate_uuid)
    user_id = Column("user_id", String, ForeignKey('user.id'))
    name = Column("name", String, default = "New Deck")
    description = Column("description", String, default = "Write a short description.")
    visibility = Column("visibility", String, default = "Public")
    tags = Column("tags", String, nullable = True)
    num_cards = Column("num_cards", Integer, default = 1)
    datetime_created = Column("datetime_created", Integer)
    datetime_updated = Column("datetime_updated", Integer)

    def __init__(self, user_id, datetime_now):
        self.user_id = user_id
        self.datetime_created = datetime_now
        self.datetime_updated = datetime_now


class Card(Base):
    __tablename__ = "card"
    id = Column("id", String, primary_key = True, default = generate_uuid)
    deck_id = Column("deck_id", String, ForeignKey('deck.id'))
    front = Column("front", String, default = "Place a question here.")
    back = Column("back", String, default = "Place the answer here.")
    tag = Column("tag", String, nullable = True)
    ease_factor = Column("ease_factor", Integer, default = 2.5)
    interval = Column("interval", Integer, default = 1)
    user_score = Column("user_score", Integer, default = 4)

    def __init__(self, deck_id):
        self.deck_id = deck_id

# ROUTES & RELATED METHODS

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

static_folder="static"
@app.route("/setup")
def setup():
    guest = session_db.query(User).filter_by(role = "guest").first()
    session["id"] = guest.id
    session["setup_done"] = True
    session.permanent = True
    
    return redirect("/")


@app.route("/", methods = ["GET"])
def index():
    if not session.get("setup_done"):
        return redirect("/setup")

    decks = session_db.query(Deck).filter_by(user_id = session.get("id")).all()

    return render_template("index.html", decks = decks)


@app.route("/deck/new", methods = ["GET"])
def create_deck():
    deck = Deck(user_id = session.get("id"), datetime_now = get_datetime())
    session_db.add(deck)
    session_db.flush()

    card = Card(deck_id = deck.id)
    session_db.add(card)
    session_db.commit()

    return render_template("new_deck.html", deck = deck)


@app.route("/deck/<string:deck_id>", methods = ["POST"])
def show_deck(deck_id):
    cards = session_db.query(Card).filter_by(deck_id = deck_id).all()
    deck = {
        "id": request.form["deck_id"],
        "name": request.form["deck_name"]

    } 

    return render_template("deck.html", cards = cards, deck = deck)


@app.route("/action/update_input_tag", methods = ["POST"])
def update_input_tag():
    data = request.get_json()
    id = data.get("id")
    value = data.get("value")
    attr = data.get("attr")

    model = model_map[data.get("model")]
    element = session_db.query(model).filter_by(id = id).first()
    setattr(element, attr, value)
    session_db.commit()

    return jsonify({"success": True, "value": value})


# APP LAUNCH & RELATED METHODS

def load_cookie_signature():
    if not os.path.exists("cookie_signature.txt"):
        with open("cookie_signature.txt", "wb") as file:
            file.write(os.urandom(24))
    
    with open("cookie_signature.txt", "rb") as file:
        app.secret_key = file.read()
    
    Session(app)


def create_guest():
    guest = session_db.query(User).filter_by(role = "guest").first()
    
    if not guest:
        guest = User(username = "guest", name = "Guest", role = "guest", datetime_now = get_datetime())
        session_db.add(guest)
        session_db.commit()


if __name__ == "__main__":
    Base.metadata.create_all(bind = engine)
    model_map = {
        "User": User,
        "Deck": Deck,
        "Card": Card
    }

    Session_db = sessionmaker(bind = engine)
    session_db = Session_db()
    load_cookie_signature()
    create_guest()
    
    app.run()


