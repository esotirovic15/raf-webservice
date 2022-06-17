# raf-webservice

Nakon pokretanja servera Kubernetes klasteru potrebno je promeniti IP adresu u skripti /client/client.py da bi mogao poslati request.

ili

izvršiti sledeću naredbu u konzoli

curl -X POST -H "Content-type: application/json" --data "{\"ime\": \"Ena\",\"prezime\": \"Sotirovic\",\"username\": \"esotirovic15\",\"smer\": \"RAF\",\"predmeti\": [{\"ime\": \"RISO\",\"espb\": 6},{\"ime\": \"MTZPP\",\"espb\": 6}]}" http://localhost:8081/users

Umesto adrese **localhost** upisati IP adresu servisa
