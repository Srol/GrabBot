from __future__ import unicode_literals
from flask import Flask, request, redirect
from rq import Queue
from worker import conn
from utils import grab_video

app = Flask(__name__)
q = Queue(connection=conn)

@app.route("/request", methods = ['POST'])
def grab():
	if request.method == "POST" and request.form.get('token') == "Insert outgoing webhook token here":
		breakthisDown = request.form.get('text').split()[2]
		url = breakthisDown[1:-1]
		channel = request.form.get('channel_name')
		userName = request.form.get('user_name')
		result = q.enqueue(grab_video, url, channel, userName)
		print breakthisDown
		print url
		print channel
		print userName
		return "Processing request."
	else:
		return "problem"
