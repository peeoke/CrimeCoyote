from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "sk-proj-GVgGtjAGWPX2SrjxiWlFT3BlbkFJEV3RS1piAoKy9D8FYAK1"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods = ["POST"])
def api():

    message = request.json.get("message")
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    else:
        return 'Failed to generate response!'
    
if __name__=='__main__':
    app.run()

