from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('drugs.json') as drug_data:
        rates = json.load(drug_data)
    if 'State' in request.args:
        selected_state = request.args["State"]
        return render_template('statsPage1.html', response_options = get_state_options(rates), percentAbuse = percentAbuse(rates, selected_state), response_state = selected_state)
    return render_template('statsPage1.html', response_options = get_state_options(rates))

def get_state_options(rates):
    states = []
    options = ""
    for c in rates:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def percentAbuse(rates, selected_state):
    percentAbuse = 0
    for c in rates:
        if c["State"] == selected_state:
            percentAbuse = c["Rates"]["Pain Relievers Abuse Past Year"]["18-25"]
    return str(percentAbuse)

if __name__=="__main__":
    app.run(debug=True)
