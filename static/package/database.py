import sqlite3
Path = r"C:\Users\ronal\OneDrive\Imagens\Programação\Python\Automação Necessidade\Banco.db"


def DataBS(escolha,databaseName,valor1="",valor2="",valor3="") -> None:
    Connection = sqlite3.connect(Path)
    Cursor = Connection.cursor()

    if(escolha == "create"):
        print("Create")
        Cursor.execute(f"CREATE TABLE IF NOT EXISTS {databaseName}(id INTEGER PRIMARY key AUTOINCREMENT,url BLOB,apis_urls BLOB)")

    elif(escolha == "insert"):
        try:
             Cursor.execute(f'INSERT INTO {databaseName} (id,url,apis_urls) values (?,?,?)',(None,valor1,valor2))
             Cursor.execute(""" DELETE FROM {databaseName} WHERE id IN (
                        SELECT a.id 
                        FROM {databaseName} AS a, {databaseName} AS b 
                        WHERE a.url = b.url AND a.id < b.id
                        ); """)
             Connection.commit()
        except EnvironmentError as e:
            print(e)
    elif (escolha == "remove"):
        Cursor.execute(f"DELETE FROM {databaseName} WHERE id=={valor1}")
        Connection.commit()
    elif(escolha == "drop"):
        Cursor.execute("DROP TABLE {databaseName}")
    elif(escolha == "select"):
        res = Cursor.execute(f"SELECT {valor1} FROM {databaseName}")
        return (res.fetchall())
    elif(escolha == "selectEspecificar"):
        res = Cursor.execute(f"SELECT {valor1} FROM {databaseName} where {valor2} == '{valor3}'")
        return (res.fetchall())
    Connection.close()

