#%%
from sqlalchemy import create_engine, func, select, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql.expression import cast

#%%
# Definisci la connessione al database
DATABASE_URL = "mysql+mysqlconnector://root:oirad1993@localhost/database4test"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

#%%
# Definisci la classe per la tabella 'ApparecchiatureElettroniche'
Base = declarative_base()

class ApparecchiatureElettroniche(Base):
    __tablename__ = 'apparecchiatureelettroniche'

    id = Column(Integer, primary_key=True)
    TipoProdotto = Column(String)
    DataProduzione = Column(Date)
    ManualeUtente = Column(String)

#%%
# Costruisci la query
query = (
    select(
        ApparecchiatureElettroniche.TipoProdotto,
        func.YEAR(ApparecchiatureElettroniche.DataProduzione).label('AnnoProduzione'),
        func.SUM(func.LENGTH(ApparecchiatureElettroniche.ManualeUtente)).label('DimensioneTotaleManuali')
    )
    .group_by(ApparecchiatureElettroniche.TipoProdotto, func.YEAR(ApparecchiatureElettroniche.DataProduzione))
)

#%%
# Esegui la query
result = session.execute(query)

# Stampa i risultati
for row in result:
    print("TipoProdotto:", row.TipoProdotto)
    print("AnnoProduzione:", row.AnnoProduzione)
    print("DimensioneTotaleManuali:", row.DimensioneTotaleManuali)
    print("")

# Chiudi la sessione
session.close()

# %%
