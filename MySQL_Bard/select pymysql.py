#%%
import pymysql

#%%
# Crea una connessione al database
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='oirad1993', db='database4test')

# Crea un cursore per eseguire le query
cursor = conn.cursor()

# Esegui la query SQL
cursor.execute("SELECT * FROM ApparecchiatureElettroniche WHERE CAST(SUBSTRING_INDEX(RisoluzioneSchermo, 'x', -1) AS SIGNED) > 1080 ORDER BY DataProduzione DESC;")

# Estrai i risultati della query
results = cursor.fetchall()

# Chiudi la connessione al database
conn.close()
#%%
# Stampa i risultati della query
for result in results:
    print(result)
# %%
