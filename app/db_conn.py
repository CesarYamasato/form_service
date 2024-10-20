import psycopg2

class DbConnection:

    def __init__(self, db_name, address, port,credentials):
        try:
            self.__db_conn = psycopg2.connect(database = db_name, host = address, port = port, user = 'postgres', password = 'postgres')
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
    
    #TODO: implement
    def query_response(self, filter):

        return

    def insert_response(self, response_json):
        cursor = self.__db_conn.cursor()
        cursor.execute(
            """INSERT INTO RELATORIO_ALUNO (NUMERO_USP, ID_RELATORIO, DATA_ENVIO, PRAZO_EXAME_QUALIFICACAO, PRAZO_ENTREGA_DISSERTACAO, ATIVIDADES_ACADEMICAS, RESUMO_ATIVIDADES, OBSERVACOES, DIFICULDADE_ORIENTADOR) VALUES 
                (%s,%s,%s,%s,%s,%s,%s,%s, %s)""", (response_json["numero_usp"], response_json["id_resposta"], response_json['data'], response_json['prazo_exame_qualificacao'], response_json['prazo_deposito_dissertacao'],
                response_json['atividades_academicas'], response_json['resumo_atividade'], response_json['observacoes'], response_json['dificuldades']))

        return

    def end_conn(self):
        self.__db_conn.end()
        return
