from flask import Flask, redirect, request, url_for, render_template
import database_manager
import queries

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<route>')
def routes(route):
    sql_str = getattr(queries, route)
    data = database_manager.select_query(sql_str)
    table_header = list(data[0].keys())

    return render_template('table.html', data=data, table_header=table_header)

if __name__ == "__main__":
    app.run(debug=True)
