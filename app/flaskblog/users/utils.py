import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def delete_picture(user_picture):
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', user_picture)
    if os.path.isfile(picture_path):
        if user_picture != 'default.jpg':
            os.remove(picture_path)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.create_token()
    msg = Message('Password Reset Request', sender='noreply@myflaskblog.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request please, ignore this email.
'''
    mail.send(msg)


def send_email_confirmation_token(user):
    token = user.create_token()
    msg = Message("Email confirmation", sender='noreply@myflaskblog.com', recipients=[user.email])
    msg.body = f'''Thank you for creating your account. Please confirm your email address by clicking here: 
{url_for('users.confirm_token', token=token, _external=True)}

If you did not make this request please, ignore this email.
'''
    mail.send(msg)
