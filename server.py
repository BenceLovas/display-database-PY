from flask import Flask, redirect, request, url_for, render_template
import database_manager
import queries

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<route>')
def routes(route):
    if route == 'mentors':
        sql_str = queries.MENTORS
    elif route == 'all-school':
        sql_str = queries.ALL_SCHOOL
    elif route == 'mentors-by-country':
        sql_str = queries.MENTORS_BY_COUNTRY
    elif route == 'contacts':
        sql_str = queries.CONTACTS
    elif route == 'applicants':
        sql_str = queries.APPLICANTS
    elif route == 'applicants-and-mentors':
        sql_str = queries.APPLICANTS_AND_MENTORS

    data = database_manager.select_query(sql_str)
    table_header = list(data[0].keys())

    return render_template('table.html', data=data, table_header=table_header)

if __name__ == "__main__":
    app.run(debug=True)
