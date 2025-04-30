import sqlite3

Path = r"C:\Users\ronal\OneDrive\Imagens\Programação\Python\Automação Necessidade\Banco.db"

def DataBS(paramentros,valor1:str,valor2:str) -> None:
    Connection = sqlite3.connect(Path)
    Cursor = Connection.cursor()

    if(paramentros == "create"):
        Cursor.execute("CREATE TABLE IF NOT EXISTS Apis_DB(id INTEGER PRIMARY key AUTOINCREMENT,url BLOB,apis_urls BLOB)")

    elif(paramentros == "insert"):
        try:
             Cursor.execute(f'INSERT INTO Apis_DB (id,url,apis_urls) values (?,?,?)',(None,valor1,valor2))
             Cursor.execute(""" DELETE FROM Apis_DB WHERE id IN (
                        SELECT a.id 
                        FROM Apis_DB AS a, Apis_DB AS b 
                        WHERE a.url = b.url AND a.id < b.id
                        ); """)
             Connection.commit()
        except EnvironmentError as e:
            print(e)
    elif (paramentros == "remove"):
        Cursor.execute(f"DELETE FROM Apis_DB WHERE id=={valor1}")
        Connection.commit()
    elif(paramentros == "drop"):
        Cursor.execute("DROP TABLE Apis_DB")
    elif(paramentros == "select"):
        res = Cursor.execute(f"SELECT {valor1} FROM Apis_DB")
        return (res.fetchall())
    elif(paramentros == "selectESC"):
        res = Cursor.execute(f"SELECT {valor1} FROM Apis_DB where id == {valor2}")
        return (res.fetchall())
    Connection.close()


# for i in range(len(str(DataBS("selectESC","apis_urls",22)).split(","))):
#     print(DataBS("selectESC","apis_urls",22)[i])