from flask import Blueprint, request, jsonify
import re
from werkzeug.security import generate_password_hash, check_password_hash

from .constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_201_CREATED
from .constants.regex import email_regex
from .database import User
from .database import db

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth/")



@auth.post("/register")
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if len(username) < 3:
        return {"message": "username too short", "statusCode": HTTP_400_BAD_REQUEST}, HTTP_400_BAD_REQUEST
    if len(password) < 6:
        return {"message": "password too short", "statusCode":  HTTP_400_BAD_REQUEST}, HTTP_400_BAD_REQUEST
    if re.fullmatch(email_regex, email) is None:
        return {"message": "invalid email address", "statusCode": HTTP_400_BAD_REQUEST}, HTTP_400_BAD_REQUEST

    if User.query.filter_by(username=username).first() is not None:
        return {"message": "username is taken", "statusCode": HTTP_403_FORBIDDEN}, HTTP_403_FORBIDDEN
    if User.query.filter_by(email=email).first() is not None:
        return {"message": "email is taken", "statusCode": HTTP_403_FORBIDDEN}, HTTP_403_FORBIDDEN

    pwd_hash = generate_password_hash(password)
    print("pwd_hash:", pwd_hash)

    user = User(username=username, email=email, password=pwd_hash)
    db.session.add(user)
    db.session.commit()

    newUser = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }
    return jsonify({"message": "User created", "statusCode": HTTP_201_CREATED, "user":newUser }), HTTP_201_CREATED


@auth.get("/")
def getUser():
    return {"name": "Paul Silanka", "stack": "Fullstack Engineer"}
