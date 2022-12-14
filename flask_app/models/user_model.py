from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'users_cr_schema'

# control D same line


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # create
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());'
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        print(f'Created: <User {user_id}>')
        return user_id

    # find all (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from users;'
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for result in results:
            users.append(User(result))
        print(f'Found all users:')
        pprint(users)
        return users

    # find one by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        print(f'Found: <User {data["id"]}>')
        return user

    # # update one by id
    # @classmethod
    # def find_by_id_and_update(cls, data):
    #     query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;'
    #     connectToMySQL(DATABASE).query_db(query, data)
    #     print(f'Updated: <User {data["id"]}>')
    #     return True

    # # delete one by id
    # @classmethod
    # def find_by_id_and_delete(cls, data):
    #     query = 'DELETE FROM users WHERE id = %(id)s;'
    #     connectToMySQL(DATABASE).query_db(query, data)
    #     print(f'Deleted: <User {data["id"]}>')
    #     return True