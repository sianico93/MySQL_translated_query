#%%
import pymysql

#%%
# Connetti al database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='oirad1993',
                             database='database4test')

# Crea un cursore
cursor = connection.cursor()

# Esegui la query
cursor.execute("""
SELECT
    po.ID AS ProdottoOrdinatoID,
    po.NumeroOrdine,
    po.NomeModello,
    po.Quantita,
    po.PrezzoUnitario AS PrezzoUnitarioProdotto,
    po.Valuta AS ValutaProdotto,
    po.DataAggiunta,
    po.DataConsegnaPrevista,
    po.StatoProdotto,
    po.NumeroRMA,
    po.Note AS NoteProdotto,
    ae.NomeModello AS NomeModelloApparecchiatura,
    ae.NumeroSerie,
    ae.DataProduzione,
    ae.Reparto,
    ae.Fornitore AS FornitoreApparecchiatura,
    ae.DataAcquisto,
    ae.Cliente,
    ae.RepartoAssistenza,
    ae.DataUltimaManutenzione,
    ae.GaranziaScadenza,
    ae.DescrizioneProblema,
    ae.ComponenteDifettoso,
    ae.TecnicoAssistenza,
    ae.Note AS NoteApparecchiatura,
    oc.NumeroOrdine AS NumeroOrdineCliente,
    oc.DataOrdine,
    oc.Cliente AS ClienteOrdine,
    oc.IndirizzoSpedizione,
    oc.CittaSpedizione,
    oc.CAPSpedizione,
    oc.ProvinciaSpedizione,
    oc.NazioneSpedizione,
    oc.MetodoPagamento,
    oc.StatoPagamento,
    oc.DataPagamento,
    oc.MetodoSpedizione,
    oc.DataSpedizione,
    oc.StatoSpedizione,
    oc.DataConsegna,
    oc.TotaleOrdine,
    oc.Valuta AS ValutaOrdine,
    oc.NumeroFattura,
    oc.CodicePromozionale,
    oc.Note AS NoteOrdine
FROM ProdottiOrdinati po
JOIN ApparecchiatureElettroniche ae ON po.NomeModello = ae.NomeModello
JOIN OrdiniClienti oc ON po.NumeroOrdine = oc.NumeroOrdine
WHERE po.DataAggiunta BETWEEN '2022-01-01' AND '2023-06-30'
    AND ae.DataProduzione <= '2023-06-30'
    AND oc.DataOrdine >= '2022-01-01';
""")

#%%
# Estrai i risultati
results = cursor.fetchall()

#%%
# Stampa i risultati
for row in results:
    print(row)

# Chiudi il cursore
cursor.close()

# Chiudi la connessione
connection.close()

# %%
