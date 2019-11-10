from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request

from forms.dish_form import DishForm
app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:134951m@localhost/receipt_webservice'
app.debug = True
db = SQLAlchemy(app)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dishname = db.Column(db.String(80), unique = True)
    dishtype = db.Column ( db.String(120), unique = True)

    def __init__(self, dishname, dishtype):
        self.dishname = dishname
        self.dishtype = dishtype
    def __repr__(self):
        return '<Dish %r' % self.dishname
@app.route('/')
def index():
    myDish = Dish.query.all()
    return render_template('index.html', allDishes=myDish)

@app.route('/dish', methods = ['GET'])
def index_dish():
    myDish = Dish.query.all()
    return render_template('dish.html', allDishes=myDish)
    # dish = Dish(request.form['username'], request.form['email'])
    # db.session.add(dish)
    # db.session.commit()
    # return redirect(url_for('index'))

@app.route('/new_dish', methods=['GET', 'POST'])
def new_dish():
    form = DishForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('dish_form.html', form=form, form_name="New dish",
                                   action="new_dish")
        else:
            dish_obj = Dish(
                dishname=form.dishname.data,
                dishtype=form.dishtype.data
            )
            a = Dish.query.filter(Dish.dishname == form.dishname.data).all()
            if not a:
                # return render_template('dish_form.html', form=form, form_name="New dish",
                #                        action="new_dish")
                db.session.add(dish_obj)
                db.session.commit()
                return redirect(url_for('index_dish'))
            return redirect(url_for('index_dish'))

    return render_template('dish_form.html', form=form, form_name="New dish", action="new_dish")

@app.route('/edit_dish', methods=['GET', 'POST'])
def edit_dish():
    form = DishForm()
    if request.method == 'GET':
        dishname = request.args.get('name')
        dish = db.session.query(Dish).filter(
            Dish.dishname == dishname).one()
        print(dishname)
        print(dish)
        a = db.session.query(Dish).filter(Dish.dishname == dish.dishname).all()
        if not a:
            return render_template('dish_form.html', form=form, form_name="Edit dish",
                                   action="edit_dish")
        form.dishtype.data = dish.dishtype
        form.dishname.data = dish.dishname
        form.old_name.data = dish.dishname
        return render_template('dish_form.html', form=form, form_name="Edit dish", action="edit_dish")

    else:
        if not form.validate():
            return render_template('dish_form.html', form=form, form_name="Edit dish",
                                   action="edit_fish")
        else:
            dish = db.session.query(Dish).filter(Dish.dishname == form.old_name.data,).one()
            dish.dishname = form.dishname.data
            dish.dishtype = form.dishtype.data
            db.session.commit()
            return redirect(url_for('index_dish'))


@app.route('/delete_dish')
def delete_dish():
    dishname = request.args.get('name')
    print(dishname)
    # dish = Dish.query.filter(Dish.dishname == dishname).first()
    # # result = db.query(Dish).filter(
    # #     Dish.dishname == dishname).one()
    #
    # db.session.delete(dish)
    # db.session.commit()

    return redirect(url_for('index_dish'))
if __name__ == "__main__":
    app.run()

