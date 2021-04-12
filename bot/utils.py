from .models import session,Message,Group
from sqlalchemy.sql import exists

def is_group_register(username):
    group=session.query(Group).filter(Group.group==username)
    return session.query(group.exists()).scalar()