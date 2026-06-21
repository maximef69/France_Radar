import requests
import time
from prometheus_client import start_http_server, Gauge


FLIGHTS_OVER_FRANCE = Gauge('flights_over_france_total', 'Nombre total d avions en vol au-dessus de la France')

def fetch_flights_over_france():
    url = "https://opensky-network.org/api/states/all?lamin=41.0&lomin=-5.0&lamax=51.0&lomax=9.0"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        flights = data.get('states')
        
        if flights is not None:
            flight_count = len(flights)
            print(f"[API] {flight_count} avions détectés. Mise à jour de la jauge.")
            

            FLIGHTS_OVER_FRANCE.set(flight_count)
        else:
            print("[API] Aucun avion.")
            FLIGHTS_OVER_FRANCE.set(0)
            
    except Exception as e:
        print(f"[ERREUR] {e}")

if __name__ == "__main__":
    print("Démarrage de l'Exporter sur http://localhost:8000")
    start_http_server(8000)
    
    while True:
        fetch_flights_over_france()
        time.sleep(15)