from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class macroForm(FlaskForm):
  age = IntegerField('Age', validators=[DataRequired()])
  weight = IntegerField('Weight (lbs)', validators=[DataRequired()])
  height_ft = IntegerField('Feet', validators=[DataRequired()])
  height_in = IntegerField('Inches', validators=[DataRequired()])
  gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
  activity_level = SelectField('Activity Level', choices=[('sedentary', 'Sedentary (little or no exercise)'), ('light', 'Lightly Active (activity 1-3 days/week)'), ('moderate', 'Moderately Active (activity 3-5 days/week)'), ('very', 'Very Active (activity 6-7 days/week)'), ('extra', 'Extra Active (anything more)')])
  body_type = SelectField('Body Type', choices=[('ectomorph', 'Ectomorph'), ('mesomorph', 'Mesomorph'), ('endomorph', 'Endomorph')])