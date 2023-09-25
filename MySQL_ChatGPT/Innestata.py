#%%
from sqlalchemy import create_engine, MetaData, Table, select, and_, func

#%%

# Crea una connessione al tuo database
engine = create_engine('mysql+mysqlconnector://root:oirad1993@localhost/database4test')

#%%

# Definisci il metadata del database
metadata = MetaData()

# Definisci le tue tabelle
apparecchiature_elettroniche = Table('ApparecchiatureElettroniche', metadata, autoload_with=engine)
prodotti_ordinati = Table('ProdottiOrdinati', metadata, autoload_with=engine)
ordini_clienti = Table('OrdiniClienti', metadata, autoload_with=engine)

#%%

# Query SQL tradotta in Python
subquery_inner = select(apparecchiature_elettroniche.c.NomeModello).\
    where(and_(
        func.sha1(func.concat(apparecchiature_elettroniche.c.ManualeUtente, apparecchiature_elettroniche.c.NomeModello)) ==
        func.sha1(func.concat(apparecchiature_elettroniche.alias().c.ManualeUtente, apparecchiature_elettroniche.alias().c.NomeModello)),
        apparecchiature_elettroniche.alias().c.ManualeUtente != '',
        apparecchiature_elettroniche.alias().c.ID.in_(
            select(prodotti_ordinati.c.ID).\
                where(prodotti_ordinati.c.NumeroOrdine.in_(
                    select(ordini_clienti.c.NumeroOrdine).\
                        where(and_(
                            ordini_clienti.c.CittaSpedizione == 'Milano',
                            ordini_clienti.c.DataOrdine.between('2023-01-01', '2023-07-31')
                        ))
                ))
        )
    ))

#%%

query = select(apparecchiature_elettroniche.c.NomeModello).\
    where(apparecchiature_elettroniche.c.NomeModello.in_(subquery_inner))

#%%

# Esegui la query e ottieni i risultati
with engine.connect() as conn:
    result = conn.execute(query)
    for row in result:
        print(row[0])
