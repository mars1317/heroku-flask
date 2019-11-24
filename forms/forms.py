from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms import validators


class DishForm(Form):
    dishname = StringField("Dish name: ", [
        validators.DataRequired("Please enter dish name."),
        validators.Length(3, 100, "Name should be from 3 to 100 symbols")])
    calories_amount = IntegerField("Group: ", [
        validators.DataRequired("Please enter calories amount")])
    calories_amount = IntegerField("Calories amount: ", [
        validators.DataRequired("Please enter calories amount")])
    old_name = HiddenField()

    submit = SubmitField("Save")
class ReceiptForm(Form):
    __tablename__ = 'receipt'
    dishname_fk = StringField("Dish name: ", [
        validators.DataRequired("Please enter dish name."),
        validators.Length(3, 255, "Name should be from 3 to 255 symbols")])
    receipt_content = StringField("Dish Receipt: ", [
        validators.DataRequired("Please enter dish Receipt."),
        validators.Length(3, 255, "Receipt should be from 3 to 255 symbols")])
    old_name = HiddenField()

    submit = SubmitField("Save")
class TypeForm(Form):
    typename = StringField("Type name: ", [
        validators.DataRequired("Please enter type name."),
        validators.Length(3, 255, "Name should be from 3 to 255 symbols")])
    old_name = HiddenField()
    submit = SubmitField("Save")

# class IngridientForm(Form):
#     dishname = StringField("Dish name: ", [
#         validators.DataRequired("Please enter dish name."),
#         validators.Length(3, 255, "Name should be from 3 to 255 symbols")])
#     ingridients = StringField("Ingridients: ", [
#         validators.DataRequired("Please enter dish ingridients."),
#         validators.Length(3, 255, "Ingridient should be from 3 to 255 symbols")])
#     old_name = HiddenField()
#
#     submit = SubmitField("Save")