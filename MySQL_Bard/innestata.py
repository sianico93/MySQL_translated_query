#%%
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean

#%%
Base = declarative_base()

class ApparecchiatureElettroniche(Base):
  __tablename__ = 'apparecchiature_elettroniche'

  id = Column(Integer, primary_key=True)
  nome_modello = Column(String(100))
  manuale_utente = Column(String(1000))

  @classmethod
  def query(cls):
    """Returns a query for all instances of this class."""
    return sqlalchemy.orm.query(cls)

class ProdottiOrdinati(Base):
  __tablename__ = 'prodotti_ordinati'

  id = Column(Integer, primary_key=True)
  numero_ordine = Column(Integer)
  id_prodotto = Column(Integer)

class OrdiniClienti(Base):
  __tablename__ = 'ordini_clienti'

  id = Column(Integer, primary_key=True)
  numero_ordine = Column(Integer)
  data_ordine = Column(Date)
  citta_spedizione = Column(String(100))

#%%
def get_model_names():
  """Gets the model names of all electronic devices that have a user manual and were ordered by customers in Milan between January 1, 2023 and July 31, 2023."""

  # Connect to the database.
  connection_string = 'mysql+mysqlconnector://root:oirad1993@localhost/database4test'
  engine = sqlalchemy.create_engine(connection_string)

  # Get all electronic devices that have a user manual.
  electronic_devices = ApparecchiatureElettroniche.query().filter(
    ApparecchiatureElettroniche.ManualeUtente.length > 0).all()

  # Get the model names of all electronic devices that were ordered by customers in Milan between January 1, 2023 and July 31, 2023.
  ordered_devices = ProdottiOrdinati.query().filter(
    ProdottiOrdinati.NumeroOrdine.in_(
      OrdiniClienti.query().filter(OrdiniClienti.CittaSpedizione == 'Milano').filter(
          OrdiniClienti.DataOrdine.between('2023-01-01', '2023-07-31')).pluck('NumeroOrdine')
  )).all()

  # Get the model names of all electronic devices that have a user manual and were ordered by customers in Milan between January 1, 2023 and July 31, 2023.
  model_names = [
      electronic_device.NomeModello
      for electronic_device in electronic_devices
      if electronic_device.NomeModello in [
          ordered_device.NomeModello
          for ordered_device in ordered_devices
      ]
  ]

  # Close the connection to the database.
  engine.dispose()

  return model_names

#%%
if __name__ == '__main__':
  model_names = get_model_names()
  print(model_names)

# %%
