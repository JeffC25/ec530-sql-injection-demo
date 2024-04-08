from flask_restful import Resource, reqparse
import sqlite3

class SearchResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('search', required=True, help='Search term is required')
        args = parser.parse_args()

        search_term = args['search']
        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        # Unsanitized query for demonstration purposes
        query = ("SELECT * FROM users WHERE name LIKE" + " '" + search_term + "';")
        print(query)
        c.execute(query)
        result = c.fetchone()
        print('')
        print(result)
        conn.close()

        # id,username,name,birthday,secret,occupation,email,address,favorite_color,sleep_hours_per_night,exercise_hours_per_week,savings_amount,total_tacos_eaten
        user = [{
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
        }]
        return user