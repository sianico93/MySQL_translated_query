#%%
import pandas as pd

#%%
def query(conn):
  """
  Questa funzione esegue la query SQL specificata.

  Args:
    conn: La connessione al database.

  Returns:
    Un oggetto Pandas DataFrame contenente i risultati della query.
  """

  # Esegue la query SQL.
  cursor = conn.cursor()
  cursor.execute("""
    SELECT
      ae.TipoProdotto,
      YEAR(ae.DataProduzione) AS AnnoProduzione,
      SUM(LENGTH(ae.ManualeUtente)) AS DimensioneTotaleManuali
    FROM
      ApparecchiatureElettroniche ae
    GROUP BY
      ae.TipoProdotto, YEAR(ae.DataProduzione);
  """)

  # Estrae i risultati della query da un DataFrame Pandas.
  df = pd.DataFrame(cursor.fetchall(), columns=["TipoProdotto", "AnnoProduzione", "DimensioneTotaleManuali"])

  # Chiude il cursore.
  cursor.close()

  return df

#%%

def connect_to_database():
  """
  Questa funzione crea una connessione al database.

  Returns:
    La connessione al database.
  """

  # Importa il modulo MySQLdb.
  import pymysql

  # Crea la connessione al database.
  conn = pymysql.connect(host="127.0.0.1", user="root", password="oirad1993", database="database4test", port=3306, connect_timeout=5)


  return conn

#%%

if __name__ == "__main__":
  # Crea una connessione al database.
  conn = connect_to_database()

  # Esegue la query e stampa i risultati.
  df = query(conn)
  print(df)

