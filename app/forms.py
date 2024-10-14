from . import form_auth

from apiclient import discovery
from httplib2 import Http


class FormService:

    def __init__(self, credentials_file, form_id):
        self.__form_service = authenticate(credentials_file) #Objeto que será usado para a comunicação com a api de forms da google, a documentação
                                                            #não é muito clara, apenas chama da "recurso" e não deixa claro se lida com refresh tokens
        self.__Form_ID = form_id #id para o form que será utilizado, por enquanto, é o mesmo sempre


    def summarise_result(self, result):
        #o json resultante da chamada da api traz uma lista com todas as respostas, cada uma contendo um campo "answers"
        json_response = dict()
        json_response['Respostas'] = list()

        if result.get('responses') is None:
            return json_response
        
        print(result)

        for response in result['responses']:
            response_dict = dict()
            print("Response: ", response)
            print("Response answers: ", response['answers'])
            #Questões de múltipla escolha são 
            response_dict['professor'] = response['answers']['48fface2']['textAnswers']['answers'][0]['value']
            response_dict['email'] = response['answers']['5abd8e58']['textAnswers']['answers'][0]['value']
            response_dict['nome'] = response['answers']['7ded28fb']['textAnswers']['answers'][0]['value']
            response_dict['numero_usp'] = response['answers']['7ed09868']['textAnswers']['answers'][0]['value']
            json_response['Respostas'].append(response_dict)
        
        return json_response

    def get_all_user_responses(self):

        result = self.__form_service.forms().responses().list(formId=self.__Form_ID).execute() #essa função retorna um json (dicionário)
        json_response = self.summarise_result(result)

        return json_response

    def get_form_metadata(self):
        result = self.__form_service.forms().get(formId=self.__Form_ID).execute()

        return result
    
    