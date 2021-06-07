from typing import List

import psycopg2

from entities.user import User
from daos.user_dao import UserDao

from exceptions.exceptions import ResourceNotFoundError

from utils.connection_util import connection

class UserDaoPostgres(UserDao):
    def add_user(self, user: User) -> User:
        sql = """insert into users (username, user_password, first_name, last_name, emp_or_mgr) values (%s, %s, %s, %s, %s) returning user_id"""
        cursor = connection.cursor()
        try:
            cursor.execute(sql, (user.username, user.password, user.first_name, user.last_name, user.emp_or_mgr))
            user_id = cursor.fetchone()[0]
            user.user_id = user_id
            return user
        except psycopg2.Error:
            raise ValueError("A user with that username already exists")
        finally:
            connection.commit()

    def get_single_user(self, user_id: int) -> User:
        sql = """select * from users where user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        record = cursor.fetchone()
        try:
            return User(*record)
        except TypeError:
            raise ResourceNotFoundError(f'Resource with given ID {user_id} not found')

    def get_all_users(self) -> List[User]:
        sql = """select * from users"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return [User(*record) for record in records]

    def update_user(self, user: User) -> User:
        self.get_single_user(user.user_id) #Check the account exists

        sql = """update users set username=%s, user_password=%s, first_name=%s, last_name=%s, emp_or_mgr=%s where user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (user.username, user.password, user.first_name, user.last_name, user.emp_or_mgr, user.user_id))
        connection.commit()
        return user

    def delete_user(self, user_id: int) -> bool:
        self.get_single_user(user_id) #Check the account exits

        sql = '''delete from users where user_id = %s'''
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        return True