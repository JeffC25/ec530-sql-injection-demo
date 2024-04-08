from flask_restful import Resource, reqparse
import sqlite3

class SearchResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('search', required=True, help='Search term is required')
        args = parser.parse_args()

        search_term = "%" + args['search'] + "%"
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM products WHERE name LIKE '{search_term}'")
        results = c.fetchall()
        conn.close()

        products = [{'id': row[0], 'name': row[1], 'price': row[2]} for row in results]
        return products