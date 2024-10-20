from . import form_auth

from apiclient import discovery
from httplib2 import Http

class Response:
    
    def __init__(self, response_dict):
        return

class FormService:

    def __init__(self, credentials_file, form_id):
        self.__form_service = form_auth.authenticate(credentials_file) #Objeto que será usado para a comunicação com a api de forms da google, a documentação
                                                            #não é muito clara, apenas chama da "recurso" e não deixa claro se lida com refresh tokens
        self.__Form_ID = form_id #id para o form que será utilizado, por enquanto, é o mesmo sempre


    def summarise_result(self, result):
        #o json resultante da chamada da api traz uma lista com todas as respostas, cada uma contendo um campo "answers"
        json_response = dict()
        json_response['respostas'] = list()

        if result.get('responses') is None:
            return json_response
        
        print(result)

        for response in result['responses']:
            response_dict = dict()
            response_dict['id_resposta'] = response['responseId']
            response_dict['data'] = response['create_time']
            response_dict['numero_usp'] = response['answers']['4e03a758']['textAnswers']['answers'][0]['value']
            response_dict["prazo_exame_qualificacao"] = response['answers']['623f8b49']['textAnswers']['answers'][0]['value']
            response_dict["prazo_deposito_dissertacao"] = response['answers']['08aca08c']['textAnswers']['answers'][0]['value']
            response_dict["atividades_academicas"] = response['answers']['0e72728d']['textAnswers']['answers'][0]['value'] 
            response_dict["resumo_atividades"] = response['answers']['3b4fa32c']['textAnswers']['answers'][0]['value'] 
            response_dict["observacoes"] = response['answers']['3e10bae9']['textAnswers']['answers'][0]['value'] 
            response_dict["dificuldades"] = response['answers']['4b67a211']['textAnswers']['answers'][0]['value'] 
            json_response['Respostas'].append(response_dict)
        
        return json_response

    def get_all_user_responses(self):

        result = self.__form_service.forms().responses().list(formId=self.__Form_ID).execute() #essa função retorna um json (dicionário)
        json_response = self.summarise_result(result)

        return json_response

    def get_form_metadata(self):
        result = self.__form_service.forms().get(formId=self.__Form_ID).execute()
        
        return result
    
    