from flask import abort, flash, redirect, render_template, url_for, request, current_app, make_response
from flask_login import login_required, current_user
import csv

from . import bench


@bench.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('home_bs4.html')
    elif request.method == 'POST':
        results = []

        user_csv = request.form.get('user_csv').split('\n')
        reader = csv.DictReader(user_csv)

        for row in reader:
            results.append(dict(row))

        fieldnames = [key for key in results[0].keys()]

        return render_template('home_bs4.html', results=results, fieldnames=fieldnames, len=len)


@bench.route('/bs3', methods=['GET', 'POST'])
def test_bs3():
    if request.method == 'GET':
        return render_template('home_bs3.html')
    elif request.method == 'POST':
        results = []

        user_csv = request.form.get('user_csv').split('\n')
        reader = csv.DictReader(user_csv)

        for row in reader:
            results.append(dict(row))

        fieldnames = [key for key in results[0].keys()]

        return render_template('home_bs3.html', results=results, fieldnames=fieldnames, len=len)
