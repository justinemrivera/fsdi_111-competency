from flask import request
import app import app
import db
from app.database import Message


@app.post("/messages")
def create_message():
    msg_data = request.json
    title = msg_data.get("title")
    body = msg_data.get("body")
    if not title or not body:
        return "<h1>Invalid syntax</h1>", 400
    message = Message(title=title, body=body)
    db.session.add(message)
    db.session.commit
    return "<h1>Created</h1>", 201


@app.get("/messages")
def read_all_messages():
    return Message.query.all()
    print(messages)


@app.route("/messages/<int:pk>")
def read_message_by_id(pk):
    return Message.query.filter_by(id=pk).first()
