from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField,IntegerField
from wtforms.validators import NumberRange,InputRequired




class PostForm(FlaskForm):
    picture = FileField('Insert picture', validators=[InputRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    colors=IntegerField('Enter no. of colors',
    	validators=[InputRequired(),NumberRange(min=2,max=64, message='Value must be between 2 and 64')])
    submit = SubmitField('Submit')
