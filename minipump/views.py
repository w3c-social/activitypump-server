# Copyright (C) 2015 Christopher Allan Webber <cwebber@dustycloud.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from flask import render_template
from flask import request, make_response, redirect, url_for

from minipump import app
from minipump import db


@app.route("/")
@app.route("/hello/<name>/")
def index(name="friend"):
    return render_template("hello.html", name=name)


# Dumbest proof of concept possible:

@app.route("/submit-example/", methods=["GET", "POST"])
def submit_example():
    if request.method == "GET":
        return render_template("form.html")

    # otherwise, it's a POST
    new_user = {}
    def update_from_field(fieldname):
        if fieldname in request.form:
            new_user[fieldname] = request.form[fieldname]

    map(update_from_field, ['username', 'real_name'])
    db.USERS[request.form['username']] = new_user

    return redirect(url_for('show_db_stuff'))


@app.route("/show-db-stuff/")
def show_db_stuff():
    response = make_response(json.dumps(db.USERS))
    response.headers['Content-Type'] = 'application/json'
    return response
    
