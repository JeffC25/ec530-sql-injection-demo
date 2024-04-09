from flask_restful import Resource, reqparse
import sqlite3

class UserResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='User is required')
        args = parser.parse_args()

        with sqlite3.connect('example.db') as conn:
            username = args['username']
            c = conn.cursor()

            # Unsanitized query for demonstration purposes
            query = ("SELECT * FROM users WHERE username='" + username + "';")
            print(query)
            c.execute(query)
            result = c.fetchone()
        conn.close()

        # user not found
        if result is None:
            return {'error': 'User not found'}, 404

        user = {
            'id': result[0],
            'username': result[1],
            'name': result[2],
            'birthday': result[3],
            'secret': result[4],
            'occupation': result[5],
            'email': result[6],
            'address': result[7],
            'favorite_color': result[8],
            'sleep_hours_per_night': result[9],
            'exercise_hours_per_week': result[10],
            'savings_amount': result[11],
            'total_tacos_eaten': result[12]
        }
        return user