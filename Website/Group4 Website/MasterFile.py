from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html', page_header="Home Page")


@app.route('/Dashboard')
def Dashboard():
    return render_template('Dashboard.html', page_header="Dashboard")


# practice start
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template(
        '404.html',
        error_message=e,
        page_header="Page Not Found",
    ), 404


# Repository https://github.com/boshiuchen/Youbike

# practice end

if __name__ == "__main__":
    app.run(debug=True)
