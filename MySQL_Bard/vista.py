#%%
import MySQLdb

#%%
# Imposta le credenziali di accesso al database
host = "127.0.0.1"
port = 3306
user = "root"
password = "oirad1993"
database = "database4test"

# Crea una connessione al database
conn = MySQLdb.connect(host=host, port=port, user=user, password=password, database=database)

#%%
# Crea la vista
cur = conn.cursor()
cur.execute("""
CREATE VIEW VistaManipolazione AS
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
""")

# Esegue la vista
cur.execute("SELECT * FROM VistaManipolazione")

#%%
# Stampa i risultati
for row in cur:
    print(row)

conn.close()