from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

debug = DebugToolbarExtension(app)

@app.route('/')
def questions():

  prompts = story.prompts
  return render_template('questions.html', prompts=prompts)

@app.route('/story')
def story_reveal():
  story_text = story.generate(request.args)

  return render_template('story.html', text=story_text)
