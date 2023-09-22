#%%
from sqlalchemy import create_engine, text

#%%

# Crea una connessione al tuo database
engine = create_engine('mysql+mysqlconnector://root:oirad1993@localhost/database4test')

# Definisci la query SQL come stringa
sql_query = """
CREATE VIEW VistaManipolazioneDati AS
SELECT
    ae.ID AS ApparecchiaturaID,
    CONCAT('Modello: ', ae.NomeModello, ' (ID: ', ae.ID, ')') AS DescrizioneModello,
    ae.NumeroSerie AS NumeroSerie,
    DATE_FORMAT(ae.DataProduzione, '%d/%m/%Y') AS DataProduzioneFormattata,
    UPPER(ae.Reparto) AS RepartoMaiuscolo,
    CONCAT('Fornitore: ', ae.Fornitore, ', Acquisto: ', DATE_FORMAT(ae.DataAcquisto, '%d/%m/%Y')) AS DettagliAcquisto,
    IFNULL(ae.Cliente, 'Nessun cliente') AS ClienteODefault,
    DATEDIFF(ae.GaranziaScadenza, NOW()) AS GiorniRimanentiGaranzia,
    UPPER(ae.StatoProduzione) AS StatoProduzioneMaiuscolo,
    CONCAT('Dimensioni: ', ae.Dimensioni, ', Peso: ', ae.Peso, ' kg') AS DescrizioneDimensioniPeso
FROM ApparecchiatureElettroniche ae;
"""

#%%

# Esegui la query SQL
with engine.connect() as connection:
    connection.execute(text(sql_query))

# Chiudi esplicitamente la connessione dopo aver eseguito la query
engine.dispose()

# %%

from sqlalchemy import create_engine, text

# Crea una connessione al tuo database
engine = create_engine('mysql+mysqlconnector://root:oirad1993@localhost/database4test')

# Definisci la query SQL per selezionare i dati dalla vista
sql_query = "SELECT * FROM VistaManipolazioneDati;"

# Esegui la query SQL e stampa i risultati
with engine.connect() as connection:
    result = connection.execute(text(sql_query))
    for row in result:
        print(row)
