from flask import Flask,render_template, request
from  cars_model import Car
import  peewee
app = Flask(__name__)


@app.route('/', methods=("GET","POST"))
def form():
    if request.method == "POST":
        make = request.form["make"]
        model =request.form["model"]
        color =request.form["color"]
        price =request.form["price"]
        Car.create(make=make, model=model, color=color, price=price)
    return render_template("form.html")


@app.route('/display')
def display():
    cars = Car.select()
    return render_template("details.html", cars=cars)


if __name__ == '__main__':
    try:
        Car.create_table()
    except peewee.OperationalError:
        print("Table Already Created")

    app.run()

# peewee
# pymysql

#DB === cars_db
#table == cars (id, make, model, color, price)








