from flask import Flask, url_for, render_template
import database_manager
import queries
import headers
import common

app = Flask(__name__)
ROUTES = ["mentors", "all_school", "mentors_by_country", "contacts", "applicants", "applicants_and_mentors"]


@app.route('/')
def index():
    title_list = common.title_from_route(ROUTES)

    return render_template('index.html', routes_titles=zip(ROUTES, title_list))


@app.route('/<route>')
def routes(route):
    table_header = getattr(headers, route)
    sql_str = getattr(queries, route)
    data = database_manager.select_query(sql_str)

    return render_template('table.html', data=data, table_header=table_header)

if __name__ == "__main__":
    app.run(debug=True)
