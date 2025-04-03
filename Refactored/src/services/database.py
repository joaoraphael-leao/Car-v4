import psycopg2

class Database:
    _instance = None

    def __new__(cls, name, user, password, host, port):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._name = name
            cls._instance._user = user
            cls._instance._host = host
            cls._instance._port = port
            cls._instance._password = password
            cls._instance._connection = None  # Conexão com o banco
            cls._instance._cursor = None      # Cursor para execução de queries
        return cls._instance

    def connect(self):
        """Estabelece conexão com o banco de dados"""
        if self._connection is None or self._connection.closed:
            try:
                self._connection = psycopg2.connect(
                    dbname=self._name,
                    user=self._user,
                    password=self._password,
                    host=self._host,
                    port=self._port
                )
                print("Conexão com o PostgreSQL estabelecida com sucesso.")
            except (Exception, psycopg2.Error) as error:
                print(f"Erro ao conectar ao PostgreSQL: {error}")
                raise
        return self._connection
    
    def get_cursor(self):
        """Retorna um cursor para execução de queries"""
        if self._connection is None or self._connection.closed:
            self.connect()  # Garante que a conexão esteja aberta
        if self._cursor is None or self._cursor.closed:
            self._cursor = self._connection.cursor()
        return self._cursor
    
    def execute_query(self, query, params=None):
        """Executa uma query no banco de dados"""
        cursor = self.get_cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Verificar se a query retorna resultados
            if cursor.description:
                return cursor.fetchall()
            return None
        except (Exception, psycopg2.Error) as error:
            self._connection.rollback()
            print(f"Erro ao executar query: {error}")
            raise
    
    def commit(self):
        """Confirma as alterações no banco de dados"""
        if self._connection:
            self._connection.commit()
    
    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self._cursor:
            self._cursor.close()
            self._cursor = None
        if self._connection:
            self._connection.close()
            self._connection = None
            print("Conexão com o PostgreSQL fechada.")
