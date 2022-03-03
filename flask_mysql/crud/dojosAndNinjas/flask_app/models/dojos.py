from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

db = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']

        self.name = data['name']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        all_dojos = [] 
        for dojo in results:
            all_dojos.append(cls(dojo)) 
        return all_dojos
    

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos(name, created_at, updated_at)
        VALUES(%(name)s, NOW(), NOW());
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    

    @classmethod
    def show_one_dojo(cls, data):
        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas 
        ON dojos.id = ninjas.dojo_id 
        Where dojos.id = %(dojo_id)s; 
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])  
        for ninja_info in results:
            ninja_data = {
                "id" : ninja_info['ninjas.id'],
                "first_name" : ninja_info['first_name'],
                "last_name" : ninja_info['last_name'],
                "age" : ninja_info['age'],
                "created_at" : ninja_info['ninjas.created_at'],
                "updated_at" : ninja_info['ninjas.updated_at'],
                "dojo_id" : ninja_info['dojo_id']
            }
            dojo.ninjas.append(ninjas.Ninja(ninja_data))
        return dojo


    @classmethod
    def add_ninja(cls, data):
        query = """
        INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results