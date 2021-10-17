from flask import request, render_template
from app import app, db
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
    messages = Message.query.all()
    return render_template("message_list.html", message_list=messages)


@app.route("/messages/<int:pk>")
def read_message_by_id(pk):
    message=Message.query.filter_by(id=pk).first()
    return render_template("message_detail.html",message=message )


@app.get("/greeting/<name>")
def greet(name):
    return render_template("home.html", username=name)
