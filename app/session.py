from . import forms
from . import db_auth

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
        self.__db_conn = db_auth.connect_to_db('production', 'localhost', '5050', db_credentials) #Objeto de conexão com o bd
    
    #TODO: implement
    def add_responses_to_db():

        return

    #TODO: implement
    def end():
        return
    