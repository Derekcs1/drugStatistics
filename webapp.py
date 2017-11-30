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

def get_state_options(Rates):
    states = []
    options = ""
    for c in Rates:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def marijuanaUse(rates, selected_state):
    marijuanaUse = 0
    for c in counties:
        if c["State"] == selected_state:
            marijuanaUse = c["Marijuana"]["18-25"]
    return str(marijuanaUse)

if __name__=="__main__":
    app.run(debug=False, port=54321)
