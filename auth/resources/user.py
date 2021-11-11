from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = User(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserLogin.parser.parse_args()

        # if username exists and password given matches the one link to the username provided
        if User.find_by_username(data['username']) and data['password'] == User.find_by_username(data['username']).password:
            return {"message": "Login success"}, 200
        return {"message": "Login failed"}, 400


class UserLogout(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserLogin.parser.parse_args()

        # if username exists and password given matches the one link to the username provided
        if User.find_by_username(data['username']) and data['password'] == User.find_by_username(data['username']).password:
            return {"message": "Logout success"}, 200
        return {"message": "Logout failed"}, 400
