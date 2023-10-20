#%%
# import delle librerie per la connessione al database e per la generazione di dati casuali
import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta
import os

#%%
#configurazione del database
db_connection = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "oirad1993",
    "database": "database_test"
}

#%%
#inizializzazione del faker
fake = Faker()

#create a function to generate a random date
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

#create a function to generate a random manual
def generate_random_manual():
    sections = ['Introduzione', 'Installazione', 'Utilizzo', 'Risoluzione Problemi', 'Specifiche Tecniche']
    manual = ""

    for section in sections:
        manual += f"## {section}\n\n"
        paragraph_count = random.randint(2, 6)
        for _ in range(paragraph_count):
            manual += fake.paragraph() + "\n\n"

    return manual

#create a function to generate a fake data for table "ApparecchiatureElettroniche"
def generate_fake_data_AE():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 1, 1)

    apparecchiature = [] # Inizializza l'elenco delle apparecchiature

    try:
        connection = mysql.connector.connect(**db_connection)
        cursor = connection.cursor()

        for i in range (50):
            nome_modello = fake.word()
            numero_serie = f'SN{i:03}'
            data_produzione = generate_random_date(start_date, end_date)
            reparto = fake.word()
            fornitore = fake.company()
            data_acquisto = generate_random_date(data_produzione, end_date)
            cliente = fake.company()
            reparto_assistenza = fake.word()
            data_ultima_manutenzione = generate_random_date(data_acquisto, end_date)
            garanzia_scadenza = generate_random_date(data_ultima_manutenzione, end_date)
            descrizione_problema = fake.text()
            componente_difettoso = fake.word()
            tecnico_assistenza = fake.name()
            note = fake.text()
            tipo_prodotto = fake.word()
            peso = round(random.uniform(0.1, 5.0), 2)
            dimensioni = f"{random.randint(5, 30)}x{random.randint(5, 30)}x{random.randint(1, 10)}"
            consumo_energetico = round(random.uniform(1.0, 10.0), 2)
            materiale_scocca = fake.word()
            colore = fake.color_name()
            interfaccia = fake.word()
            risoluzione_schermo = fake.random_element(['1920x1080', '1280x720', '2560x1440'])
            sistema_operativo = fake.word()
            cpu = fake.word()
            ram = f"{random.randint(2, 64)} GB"
            memoria_interna = f"{random.randint(16, 512)} GB"
            fotocamera_principale = f"{random.randint(5, 64)} MP"
            fotocamera_frontale = f"{random.randint(2, 32)} MP"
            connettivita = fake.word()
            bluetooth_versione = fake.random_element(['4.0', '4.2', '5.0'])
            sensori = fake.text()
            certificazioni = fake.text()
            manuale_utente = generate_random_manual()
            data_ultimo_aggiornamento = generate_random_date(data_produzione, end_date)
            versione_software = fake.random_element(['1.0', '2.0', '3.0'])
            stato_produzione = fake.random_element(['In produzione', 'Fuori produzione'])
            quantita_magazzino = random.randint(10, 100)
            quantita_vendute = random.randint(0, quantita_magazzino)
            prezzo_unitario = round(random.uniform(100.0, 1000.0), 2)
            valuta = fake.random_element(['EUR', 'USD'])
            
            # Creare una tupla con tutti i dettagli
            apparecchiatura = (
                nome_modello, numero_serie, data_produzione, reparto, fornitore, data_acquisto, cliente,
                reparto_assistenza, data_ultima_manutenzione, garanzia_scadenza, descrizione_problema,
                componente_difettoso, tecnico_assistenza, note, tipo_prodotto, peso, dimensioni,
                consumo_energetico, materiale_scocca, colore, interfaccia, risoluzione_schermo,
                sistema_operativo, cpu, ram, memoria_interna, fotocamera_principale,
                fotocamera_frontale, connettivita, bluetooth_versione, sensori, certificazioni,
                manuale_utente, data_ultimo_aggiornamento, versione_software, stato_produzione,
                quantita_magazzino, quantita_vendute, prezzo_unitario, valuta
            )
            
            apparecchiature.append(apparecchiatura)  # Aggiungi la tupla all'elenco
            
            insert_query = """
                INSERT INTO apparechiatureelettroniche (
                    NomeModello, NumeroSerie, DataProduzione, Reparto, Fornitore, DataAcquisto, Cliente,
                    RepartoAssistenza, DataUltimaManutenzione, GaranziaScadenza, DescrizioneProblema,
                    ComponenteDifettoso, TecnicoAssistenza, Note, TipoProdotto, Peso, Dimensioni,
                    ConsumoEnergetico, MaterialeScocca, Colore, Interfaccia, RisoluzioneSchermo,
                    SistemaOperativo, CPU, RAM, MemoriaInterna, FotocameraPrincipale,
                    FotocameraFrontale, Connettivita, BluetoothVersione, Sensori, Certificazioni,
                    ManualeUtente, DataUltimoAggiornamento, VersioneSoftware, StatoProduzione,
                    QuantitaMagazzino, QuantitaVendute, PrezzoUnitario, Valuta
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                nome_modello, numero_serie, data_produzione, reparto, fornitore, data_acquisto, cliente,
                reparto_assistenza, data_ultima_manutenzione, garanzia_scadenza, descrizione_problema,
                componente_difettoso, tecnico_assistenza, note, tipo_prodotto, peso, dimensioni,
                consumo_energetico, materiale_scocca, colore, interfaccia, risoluzione_schermo,
                sistema_operativo, cpu, ram, memoria_interna, fotocamera_principale,
                fotocamera_frontale, connettivita, bluetooth_versione, sensori, certificazioni,
                manuale_utente, data_ultimo_aggiornamento, versione_software, stato_produzione,
                quantita_magazzino, quantita_vendute, prezzo_unitario, valuta
            )

            cursor.execute(insert_query, data)
        
        connection.commit()
        cursor.close()
        connection.close()

        print("Inserimento completato!")

    except mysql.connector.Error as error:
        print("Errore durante l'inserimento:", error)
    
    return apparecchiature

#create a function to generate a fake data for table "ComponentiElettronici"
def generate_fake_data_CE(apparecchiature):
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 1, 1)

    try:
        connection = mysql.connector.connect(**db_connection)
        cursor = connection.cursor()

        for i in range (50):
            nome_componente = fake.word()
            apparecchiatura_random = random.choice(apparecchiature)
            codice_prodotto = apparecchiatura_random[0]
            fornitore_componente = fake.company()
            data_acquisto_componente = generate_random_date(start_date, end_date)
            quantita_magazzino_componente = random.randint(10, 100)
            prezzo_unitario_componente = round(random.uniform(10.0, 100.0), 2)
            valuta_componente = fake.random_element(['EUR', 'USD'])
            specifiche_tecniche = fake.text()
            data_ultimo_aggiornamento_componente = generate_random_date(data_acquisto_componente, end_date)
            documentazione_tecnica = fake.text()
            scheda_tecnica = fake.text()
            note_componente = fake.text()
            numero_lotti_prodotti = random.randint(1, 10)
            data_primo_utilizzo = generate_random_date(start_date, end_date)
            data_ultimo_utilizzo = generate_random_date(data_primo_utilizzo, end_date)
            numero_utilizzi = random.randint(1, 100)
            numero_serie_componente = f'CSN{random.randint(1, 100):03}'
            numero_firmware = f'Firmware{random.randint(1, 10)}'
            codice_revisione = f'Rev{random.randint(1, 5)}'
            data_scadenza_garanzia = generate_random_date(data_ultimo_aggiornamento_componente, end_date)
            certificazioni = fake.text()
            responsabile_qa = fake.name()
            stato_componente = fake.random_element(['In produzione', 'Fuori produzione'])
            data_ritiro = generate_random_date(data_acquisto_componente, end_date)

            insert_query = """
                INSERT INTO componentielettronici (
                    Nome, CodiceProdotto, Fornitore, DataAcquisto, QuantitaMagazzino, PrezzoUnitario, Valuta,
                    SpecificheTecniche, DataUltimoAggiornamento, DocumentazioneTecnica, SchedaTecnica, Note,
                    NumeroLottiProdotti, DataPrimoUtilizzo, DataUltimoUtilizzo, NumeroUtilizzi, NumeroSerieComponente,
                    NumeroFirmware, CodiceRevisione, DataScadenzaGaranzia, Certificazioni, ResponsabileQA,
                    StatoComponente, DataRitiro
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                nome_componente, codice_prodotto, fornitore_componente, data_acquisto_componente,
                quantita_magazzino_componente, prezzo_unitario_componente, valuta_componente,
                specifiche_tecniche, data_ultimo_aggiornamento_componente, documentazione_tecnica,
                scheda_tecnica, note_componente, numero_lotti_prodotti, data_primo_utilizzo,
                data_ultimo_utilizzo, numero_utilizzi, numero_serie_componente, numero_firmware,
                codice_revisione, data_scadenza_garanzia, certificazioni, responsabile_qa,
                stato_componente, data_ritiro
            )
            cursor.execute(insert_query, data)

        connection.commit()
        cursor.close()
        connection.close()

        print("Inserimento componenti completato!")

    except mysql.connector.Error as error:
        print("Errore durante l'inserimento componenti:", error)

#create a function to generate a fake data for table "OrdiniClienti"
def generate_fake_data_OC():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 1, 1)

    try:
        connection = mysql.connector.connect(**db_connection)
        cursor = connection.cursor()

        for i in range (50):
            data_ordine = generate_random_date(start_date, end_date)
            cliente = fake.company()
            indirizzo_spedizione = fake.address()
            citta_spedizione = fake.city()
            cap_spedizione = fake.zipcode()
            provincia_spedizione = fake.state_abbr()
            nazione_spedizione = fake.country()
            metodo_pagamento = fake.random_element(['Carta di credito', 'PayPal', 'Bonifico bancario'])
            stato_pagamento = fake.random_element(['In attesa', 'Completato'])
            data_pagamento = generate_random_date(data_ordine, end_date)
            metodo_spedizione = fake.random_element(['Corriere espresso', 'Posta prioritaria'])
            data_spedizione = generate_random_date(data_pagamento, end_date)
            stato_spedizione = fake.random_element(['In preparazione', 'Spedito'])
            data_consegna = generate_random_date(data_spedizione, end_date)
            totale_ordine = round(random.uniform(100.0, 1000.0), 2)
            valuta_ordine = fake.random_element(['EUR', 'USD'])
            numero_fattura = f'INV{random.randint(1000, 9999)}'
            codice_promozionale = f'PROMO{random.randint(1, 10)}'
            note_ordine = fake.text()

            insert_query = """
                INSERT INTO ordiniclienti (
                    DataOrdine, Cliente, IndirizzoSpedizione, CittaSpedizione, CAPSpedizione, ProvinciaSpedizione,
                    NazioneSpedizione, MetodoPagamento, StatoPagamento, DataPagamento, MetodoSpedizione,
                    DataSpedizione, StatoSpedizione, DataConsegna, TotaleOrdine, Valuta, NumeroFattura,
                    CodicePromozionale, Note
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                data_ordine, cliente, indirizzo_spedizione, citta_spedizione, cap_spedizione, provincia_spedizione,
                nazione_spedizione, metodo_pagamento, stato_pagamento, data_pagamento, metodo_spedizione,
                data_spedizione, stato_spedizione, data_consegna, totale_ordine, valuta_ordine,
                numero_fattura, codice_promozionale, note_ordine
            )
            cursor.execute(insert_query, data)

        connection.commit()
        cursor.close()
        connection.close()

        print("Inserimento ordini completato!")

    except mysql.connector.Error as error:
        print("Errore durante l'inserimento ordini:", error)

#create a function to generate a fake data for table "ProdottiOrdinati"
def generate_fake_data_PO(apparecchiature):
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 1, 1)

    try:
        connection = mysql.connector.connect(**db_connection)
        cursor = connection.cursor()

        for i in range (50):
            numero_ordine = random.randint(1, 50)  # Cambiare in base al numero di ordini generati
            nome_modello = random.choice(apparecchiature)[0]
            quantita = random.randint(1, 5)
            prezzo_unitario = round(random.uniform(100.0, 1000.0), 2)
            valuta_prodotto = fake.random_element(['EUR', 'USD'])
            data_aggiunta = generate_random_date(start_date, end_date)
            data_consegna_prevista = generate_random_date(data_aggiunta, end_date)
            stato_prodotto = fake.random_element(['In attesa di spedizione', 'Spedito'])
            numero_rma = f'RMA{random.randint(1000, 9999)}'
            note_prodotto = fake.text()

            insert_query = """
                INSERT INTO prodottiordinati (
                    NumeroOrdine, NomeModello, Quantita, PrezzoUnitario, Valuta, DataAggiunta,
                    DataConsegnaPrevista, StatoProdotto, NumeroRMA, Note
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                numero_ordine, nome_modello, quantita, prezzo_unitario, valuta_prodotto, data_aggiunta,
                data_consegna_prevista, stato_prodotto, numero_rma, note_prodotto
            )
            cursor.execute(insert_query, data)

        connection.commit()
        cursor.close()
        connection.close()

        print("Inserimento prodotti ordinati completato!")

    except mysql.connector.Error as error:
        print("Errore durante l'inserimento prodotti ordinati:", error)

#%%
#create a main function to call all the functions
def main():
    apparecchiature = generate_fake_data_AE()
    generate_fake_data_CE(apparecchiature)
    generate_fake_data_OC()
    generate_fake_data_PO(apparecchiature)

#%%
#create a main function in python
if __name__ == "__main__":
    main()

