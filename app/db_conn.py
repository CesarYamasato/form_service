import psycopg2

class DbConnection:

    def __init__(self, db_name, address, port,credentials):
            try:
                conn = psycopg2.connect(
                    dbname= db_name,
                    user = credentials["user"],
                    password = credentials["password"],
                    host= address,
                    port= port
                )
                self.__db_conn = conn
                self.__cursor = self.__db_conn.cursor()
            except Exception as e:
                print(f"Erro ao conectar ao banco de dados: {e}, {e.__class__}")
                self.__db_conn = None
                self.__cursor = None

            
    #TODO: implement
    def query_response(self, filter):

        return

    #TODO: EXCEPTION TRATMENT
    def insert_response(self, response_json):
        self.__cursor.execute(
            """INSERT INTO RELATORIO_ALUNO (NUMERO_USP, ID_RELATORIO, DATA_ENVIO, PRAZO_EXAME_QUALIFICACAO, PRAZO_ENTREGA_DISSERTACAO, ATIVIDADES_ACADEMICAS, RESUMO_ATIVIDADES, OBSERVACOES, DIFICULDADE_ORIENTADOR) VALUES 
                (%s,%s,%s,%s,%s,%s,%s,%s, %s);""", (response_json["numero_usp"], response_json["id_resposta"], response_json['data'], response_json['prazo_exame_qualificacao'], response_json['prazo_deposito_dissertacao'],
                response_json['atividades_academicas'], response_json['resumo_atividades'], response_json['observacoes'], response_json['dificuldades']))

        self.__db_conn.commit()

        return "Insertion Done"

    def end_conn(self):
        self.__db_conn.close()
        self.__cursor.close()
        return
