# PACKAGE IMPORTS & INITIALIZATION

from flask import Flask, render_template, redirect

from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.orm import sessionmaker, declarative_base

import uuid

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

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
    hash = Column("hash", String)
    num_decks = Column("num_decks", Integer, default = 0)
    datetime_created = Column("datetime_created", Integer)
    datetime_updated = Column("datetime_updated", Integer)
    datetime_login = Column("datetime_login", Integer)

    def __init__(self, username, name, hash, datetime_now):
        self.username = username
        self.name = name
        self.hash = hash
        self.datetime_created = datetime_now
        self.datetime_updated = datetime_now
        self.datetime_login = datetime_now

class Deck(Base):
    __tablename__ = "deck"
    id = Column("id", String, primary_key = True, default = generate_uuid)
    user_id = Column("user_id", String, ForeignKey('user.id'))
    name = Column("name", String)
    description = Column("description", String)
    visibility = Column("visibility", String)
    tags = Column("tags", String)
    num_cards = Column("num_cards", Integer, default = 1)
    datetime_created = Column("datetime_created", Integer)
    datetime_updated = Column("datetime_updated", Integer)

    def __init__(self, user_id, name, description, visibility, tags, datetime_now):
        self.user_id = user_id
        self.name = name
        self.description = description
        self.visibility = visibility
        self.tags = tags
        self.datetime_created = datetime_now
        self.datetime_updated = datetime_now

class Card(Base):
    __tablename__ = "card"
    id = Column("id", String, primary_key = True, default = generate_uuid)
    deck_id = Column("deck_id", String, ForeignKey('deck.id'))
    front = Column("front", String)
    back = Column("back", String)

    def __init__(self, deck_id, front, back):
        self.deck_id = deck_id
        self.front = front
        self.back = back
        

# ROUTES

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def create_deck():
    # jsonify({})
    redirect("/")


# APP LAUNCH

if __name__ == "__main__":
    Base.metadata.create_all(bind = engine)
    app.run()

