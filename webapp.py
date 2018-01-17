from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('static/drugs.json') as drug_data:
        Rates = json.load(drug_data)
    if 'State' in request.args:
        selected_state = request.args["State"]
        return render_template('home.html', response_options = get_state_options(Rates), marijuanaUse = marijuanaUse(Rates, selected_state), response_state = selected_state)
    return render_template('home.html', response_options = get_state_options(Rates))

@app.route("/marijuanausage")
def render_marijuana_usage():
    with open('static/drugs.json') as drug_data:
        data = json.load(drug_data)
    if 'State' in request.args:
        return render_template('marijuanausage.html', response_options = get_state_options(dict), response_state = request.args['State'], marijuana_use = marijuanaUse(dict, request.args['State']))
    return render_template('marijuanausage.html', response_options = get_state_options(data))

def get_state_options(dict):
    states = []
    options = ""
    for c in dict:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def marijuanaUse(dict, selected_state):
    marijuanaUse = 0
    for c in dict:
        if c["State"] == selected_state:
            marijuanaUse = c["Marijuana"]["18-25"]
    return str(marijuanaUse)

if __name__=="__main__":
    app.run(debug=False, port=54321)
