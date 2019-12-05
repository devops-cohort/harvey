from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from application.models import Users
from application.__init__ import LoginManager
from flask_login import LoginManager, current_user

"""project imports"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from application.models import Tracks, Artists, Genres
import application.py
from application.__init__ import LoginManager
from flask_login import LoginManager, current_user


class PostForm(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    content = StringField('Content',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    submit = SubmitField('  Post Content  ')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    email = StringField('Email:        ',
    validators=[
        DataRequired(),
        Email()
        ]
        )
    password = PasswordField('Password:     ',
    validators=[
        DataRequired()
        ]
        )
    confirm_password = PasswordField('Confirm Password',
    validators=[
        DataRequired(),
        EqualTo('password')
        ]
        )
    submit = SubmitField('  Sign Up  ')

    def validate_email(self,email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')

class LoginForm(FlaskForm):
    email = StringField('Email',
    validators = [
        DataRequired(),
        Email()
        ]
        )

    password = PasswordField('Password',
    validators = [
        DataRequired()
    ]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
    )

    email = StringField('Email:        ',
    validators=[
        DataRequired(),
        Email()
        ]
        )

    submit = SubmitField('  Update  ')


    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email already in use, please try another")


"""  Project forms   """
class DirectoryForm(FlaskForm): #user enters directory path
    directory_path = StringField("Enter your directory: ",
    validators = [
        DataRequired(),
        Length(min=2, max = 150) 
    ]
    )
    submit = SubmitField ('Submit')

    def validate_directory_path(self,directory_path):
        #change me <-- add directory check code 
        path = True
        if path:
            ValidationError("Path exists")
        if path == False:
            pass
            #change me <-- add make a directory function

class GenreForm(FlaskForm): #allows user to enter genre name
    genre_name = StringField("Genre name: ",
    validators = [
        DataRequired(),
        Length(min=2, max = 20)
            ]
        )
    folder_path = StringField("Folder Path: ", default="harvey/music/"+str(genre_name.data))
    submit = SubmitField('Add Genre') #button to submit data
    
    def validate_genre_name(self,genre_name):
        in_use = Genres.query.filter_by(name=genre_name.data).first()
        if in_use:
            raise ValidationError("Genre Already exists")
    def validate_folder_path(self,folder_path):
        in_use =  application.py.file_interactions.folder_identify_lx("harvey/music" + str(genre_name))
        if in_use:
            raise ValidationError("Directory already exists")