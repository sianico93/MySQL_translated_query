from sqlalchemy import create_engine

# Connetti al database
engine = create_engine('mysql+mysqlconnector://root:oirad1993@localhost/database4test')

# Esegui la query
result = engine.execute(
    """
    SELECT ae.NomeModello
    FROM ApparecchiatureElettroniche ae
    WHERE ae.NomeModello IN (
        SELECT ae_inner.NomeModello
        FROM ApparecchiatureElettroniche ae_inner
        WHERE SHA1(CONCAT(ae_inner.ManualeUtente, ae_inner.NomeModello)) = SHA1(CONCAT(ae.ManualeUtente, ae.NomeModello))
          AND LENGTH(ae_inner.ManualeUtente) > 0
          AND ae_inner.ID IN (
              SELECT po.ID
              FROM ProdottiOrdinati po
              WHERE po.NumeroOrdine IN (
                  SELECT oc.NumeroOrdine
                  FROM OrdiniClienti oc
                  WHERE oc.CittaSpedizione = 'Milano'
                    AND oc.DataOrdine BETWEEN '2023-01-01' AND '2023-07-31'
              )
          )
    );
    """
)

# Stampa i risultati
for row in result:
    print(row['NomeModello'])