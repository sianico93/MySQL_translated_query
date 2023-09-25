#%%
import mysql.connector

#%%
# Connessione al database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="oirad1993",
    database="database4test"
)

cursor = conn.cursor()

#%%
# Query SQL tradotta
query = """
SELECT *
FROM ApparecchiatureElettroniche
WHERE CAST(SUBSTRING_INDEX(RisoluzioneSchermo, 'x', -1) AS SIGNED) > 1080
ORDER BY DataProduzione DESC;
"""

#%%
# Esecuzione della query
cursor.execute(query)
results = cursor.fetchall()

#%%
# Stampa dei risultati
for row in results:
    print(row)

# Chiusura della connessione
conn.close()

# %%
