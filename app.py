# PACKAGE IMPORTS & INITIALIZATION

from flask import Flask, render_template, redirect, jsonify, request, session
from flask_session import Session


from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.orm import sessionmaker, declarative_base


from datetime import datetime
import uuid, os


app = Flask(__name__)
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


@app.route("/setup")
def setup():
    guest = session_db.query(User).filter_by(role = "guest").first()
    session["id"] = guest.id
    session["setup_done"] = True
    session.permanent = True
    
    return redirect("/")


@app.route("/")
def index():
    if not session.get("setup_done"):
        return redirect("/setup")

    decks = [deck.name for deck in session_db.query(Deck).filter_by(user_id = session.get("id"))]
    return render_template("index.html", decks = decks)


@app.route("/new")
def create_deck():
    new_deck = Deck(user_id = session.get("id"), datetime_now = get_datetime())
    new_card = Card(deck_id = new_deck.id)

    session_db.add(new_deck)
    session_db.add(new_card)
    session_db.commit()

    return redirect("/")


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
    Session_db = sessionmaker(bind = engine)
    session_db = Session_db()
    load_cookie_signature()
    create_guest()
    
    app.run()


