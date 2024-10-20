from . import forms
from . import db_conn

from apiclient import discovery
from httplib2 import Http
import json
import psycopg2

class Session:
    #TODO: adicionar configurações de teste
    def __init__(self):
                                                                            
        self.__form_conn = forms.FormService("credentials.json",    #Objeto que será usado para a comunicação com a api de forms da google, a documentação
                    "1YckdpZN_ETO8XUm_Z_IGOWglMvEl9T7J5AdP3zqgbB8") #não é muito clara, apenas chama da "recurso" e não deixa claro se lida com refresh tokens
    
        with open('db_credentials.json') as db_credentials_file:
            db_credentials = json.loads(db_credentials_file)
        self.__db_conn = db_auth.connect_to_db('POSGRADUACAO', 'localhost', '5432', db_credentials) #Objeto de conexão com o bd
    
    def add_responses_to_db(self):
        responses = self.__form_conn.get_all_user_responses()["respostas"]
        for response in responses:
            self.__db_conn.insert_response(response)
        return

    def get_all_user_responses(self):
        return self.__form_conn.get_all_user_responses()

    def get_form_metadata(self):
        return self.__form_conn.get_form_metadata()


    #TODO: implement
    def end():
        return
    