# project/main/views.py


from flask import render_template, Blueprint, redirect, url_for, jsonify,Flask, request, flash
from .forms import SearchForm
import json
import requests
import pprint

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return search_results(form.searchterm.data)

    return render_template('main/index.html', form=form)


@main_blueprint.route("/results")
def search_results(search_query):
    res = query_API(search_query)
    return render_template('main/results.html', results=res,
                           query=search_query)


def query_API(searchterm):
    apikey = "V9SVY84Z7USX"  # test value
    lmt = 8

    # load the user's anonymous ID from cookies or some other disk storage
    # anon_id = <from db/cookies>

    # ELSE - first time user, grab and store their the anonymous ID
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

    if r.status_code == 200:
        anon_id = json.loads(r.content)["anon_id"]
        # store in db/cookies for re-use later
    else:
        anon_id = ""

    # our test search
    search_term = "excited"

    # get random results using default locale of EN_US
    r = requests.get(
        "https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s&anon_id=%s" % (search_term, apikey, lmt, anon_id))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        return gifs
    else:
        gifs = None
