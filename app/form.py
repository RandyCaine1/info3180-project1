from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileAllowed, FileRequired, FileField


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField(label='Gender', choices=[("None", "Select Gender"),("Female", "Female"), ("Male", "Male")])
    email = StringField('Email', validators=[InputRequired(), Email()])
    location = StringField('Location', validators=[InputRequired()])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only image files are accepted with extensions "jpg","png","jpeg".')])