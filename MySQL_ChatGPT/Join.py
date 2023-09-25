#%%

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime

#%%

# Definisci il modello base
Base = declarative_base()

# Definisci le classi dei modelli per le tabelle
class ProdottiOrdinati(Base):
    __tablename__ = 'ProdottiOrdinati'

    ID = Column(Integer, primary_key=True)
    NumeroOrdine = Column(Integer)
    NomeModello = Column(String)
    Quantita = Column(Integer)
    PrezzoUnitario = Column(Float) #qui ho modificato il nome della colonna da PrezzoUnitarioProdotto a PrezzoUnitario
    Valuta = Column(String) #qui ho modificato il nome della colonna da ValutaProdotto a Valuta
    DataAggiunta = Column(DateTime)
    DataConsegnaPrevista = Column(DateTime)
    StatoProdotto = Column(String)
    NumeroRMA = Column(Integer)
    Note = Column(String) #qui ho modificato il nome della colonna da NoteProdotto a Note

class ApparecchiatureElettroniche(Base):
    __tablename__ = 'ApparecchiatureElettroniche'

    NomeModello = Column(String, primary_key=True)
    NumeroSerie = Column(String)
    DataProduzione = Column(DateTime)
    Reparto = Column(String)
    Fornitore = Column(String) #qui ho modificato il nome della colonna da FornitoreApparecchiatura a Fornitore
    DataAcquisto = Column(DateTime)
    Cliente = Column(String)
    RepartoAssistenza = Column(String)
    DataUltimaManutenzione = Column(DateTime)
    GaranziaScadenza = Column(DateTime)
    DescrizioneProblema = Column(String)
    ComponenteDifettoso = Column(String)
    TecnicoAssistenza = Column(String)
    Note = Column(String) #qui ho modificato il nome della colonna da NoteApparecchiatura a Note

class OrdiniClienti(Base):
    __tablename__ = 'OrdiniClienti'

    NumeroOrdine = Column(Integer, primary_key=True)
    DataOrdine = Column(DateTime)
    Cliente = Column(String) #qui ho modificato il nome della colonna da ClienteOrdine a Cliente
    IndirizzoSpedizione = Column(String)
    CittaSpedizione = Column(String)
    CAPSpedizione = Column(String)
    ProvinciaSpedizione = Column(String)
    NazioneSpedizione = Column(String)
    MetodoPagamento = Column(String)
    StatoPagamento = Column(String)
    DataPagamento = Column(DateTime)
    MetodoSpedizione = Column(String)
    DataSpedizione = Column(DateTime)
    StatoSpedizione = Column(String)
    DataConsegna = Column(DateTime)
    TotaleOrdine = Column(Float)
    Valuta = Column(String) #qui ho modificato il nome della colonna da ValutaOrdine a Valuta
    NumeroFattura = Column(Integer)
    CodicePromozionale = Column(String)
    Note = Column(String) #qui ho modificato il nome della colonna da NoteOrdine a Note

#%%

# Crea un motore di database SQLite (sostituisci con i tuoi dettagli di connessione)
# engine = create_engine('sqlite:///database.db')

# Crea un motore di database MySQL (sostituisci con i tuoi dettagli di connessione)
engine = create_engine('mysql+mysqlconnector://root:oirad1993@localhost/database4test')

# Crea le tabelle nel database
Base.metadata.create_all(engine)

#%%

# Crea una sessione
Session = sessionmaker(bind=engine)
session = Session()

# Esegui la query
result = session.query(
    ProdottiOrdinati.ID.label('ProdottoOrdinatoID'),
    ProdottiOrdinati.NumeroOrdine,
    ProdottiOrdinati.NomeModello,
    ProdottiOrdinati.Quantita,
    ProdottiOrdinati.PrezzoUnitario.label('PrezzoUnitarioProdotto'), #qui ho modificato il nome della colonna da PrezzoUnitarioProdotto a PrezzoUnitario
    ProdottiOrdinati.Valuta.label('ValutaProdotto'), #qui ho modificato il nome della colonna da ValutaProdotto a Valuta
    ProdottiOrdinati.DataAggiunta,
    ProdottiOrdinati.DataConsegnaPrevista,
    ProdottiOrdinati.StatoProdotto,
    ProdottiOrdinati.NumeroRMA,
    ProdottiOrdinati.Note.label('NoteProdotto'), #qui ho modificato il nome della colonna da NoteProdotto a Note
    ApparecchiatureElettroniche.NomeModello.label('NomeModelloApparecchiatura'),
    ApparecchiatureElettroniche.NumeroSerie,
    ApparecchiatureElettroniche.DataProduzione,
    ApparecchiatureElettroniche.Reparto,
    ApparecchiatureElettroniche.Fornitore.label('FornitoreApparecchiatura'), #qui ho modificato il nome della colonna da FornitoreApparecchiatura a Fornitore
    ApparecchiatureElettroniche.DataAcquisto,
    ApparecchiatureElettroniche.Cliente,
    ApparecchiatureElettroniche.RepartoAssistenza,
    ApparecchiatureElettroniche.DataUltimaManutenzione,
    ApparecchiatureElettroniche.GaranziaScadenza,
    ApparecchiatureElettroniche.DescrizioneProblema,
    ApparecchiatureElettroniche.ComponenteDifettoso,
    ApparecchiatureElettroniche.TecnicoAssistenza,
    ApparecchiatureElettroniche.Note.label('NoteApparecchiatura'), #qui ho modificato il nome della colonna da NoteApparecchiatura a Note
    OrdiniClienti.NumeroOrdine.label('NumeroOrdineCliente'),
    OrdiniClienti.DataOrdine,
    OrdiniClienti.Cliente.label('ClienteOrdine'), #qui ho modificato il nome della colonna da ClienteOrdine a Cliente
    OrdiniClienti.IndirizzoSpedizione,
    OrdiniClienti.CittaSpedizione,
    OrdiniClienti.CAPSpedizione,
    OrdiniClienti.ProvinciaSpedizione,
    OrdiniClienti.NazioneSpedizione,
    OrdiniClienti.MetodoPagamento,
    OrdiniClienti.StatoPagamento,
    OrdiniClienti.DataPagamento,
    OrdiniClienti.MetodoSpedizione,
    OrdiniClienti.DataSpedizione,
    OrdiniClienti.StatoSpedizione,
    OrdiniClienti.DataConsegna,
    OrdiniClienti.TotaleOrdine,
    OrdiniClienti.Valuta.label('ValutaOrdine'), #qui ho modificato il nome della colonna da ValutaOrdine a Valuta
    OrdiniClienti.NumeroFattura,
    OrdiniClienti.CodicePromozionale,
    OrdiniClienti.Note.label('NoteOrdine') #qui ho modificato il nome della colonna da NoteOrdine a Note
).join(
    ApparecchiatureElettroniche, ProdottiOrdinati.NomeModello == ApparecchiatureElettroniche.NomeModello
).join(
    OrdiniClienti, ProdottiOrdinati.NumeroOrdine == OrdiniClienti.NumeroOrdine
).filter(
    ProdottiOrdinati.DataAggiunta.between('2022-01-01', '2023-06-30'),
    ApparecchiatureElettroniche.DataProduzione <= '2023-06-30',
    OrdiniClienti.DataOrdine >= '2022-01-01'
)

#%%

# Esegui la query e ottieni i risultati
results = result.all()

#%%

# Stampare i risultati (sostituisci con l'output desiderato)
for row in results:
    print(row)

# %%
