#!/usr/bin/env python3
"""Hash password"""
import bcrypt
from user import User
from db import DB
import uuid


def _hash_password(password: str) -> bytes:
    """ The returned bytes is a salted hash of the input
    password, hashed with bcrypt.hashpw
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def _generate_uuid() ->str:
    """ return a string representation of a new UUID"""
    random = str(uuid.uuid1())
    return random


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register_user method"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pas = _hash_password(password)
            user = self._db.add_user(email, pas)
            return user
        else:
            raise ValueError(f'User {email} already exist')

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        user = self._db.find_user_by(email=email)
        if user is not None:
            if bcrypt.checkpw(users['password'].encode('utf8')):
                return True
            else:
                return False
        else:
            return False

    def create_session(self, email: str) -> str:
        """Get session ID"""
        user = self._db.find_user_by(email=email)
        if user is not None:
            users['session_id'] = _generate_uuid()
            return (users['session_id'])