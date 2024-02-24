#!/bin/python3
"""User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User representation"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
