from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/project')
def project():
    return render_template('project.html')    

if (__name__) == "__main__":
    app.run(debug=True)