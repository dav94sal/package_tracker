from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import InputRequired
from ..map.map import map

cities = map.keys()
# print(cities)

class ShippingForm(FlaskForm):
    recipient = StringField("Recipient", validators=[InputRequired()])
    origin = SelectField("Origin",
                         default="Select Origin",
                         choices=cities,
                         validators=[InputRequired()])
    destination = SelectField("Destination",
                              default="Select Destination",
                              choices=cities,
                              validators=[InputRequired()])
    express_shipping = BooleanField("Express Shipping")
    submit = SubmitField("Submit")
