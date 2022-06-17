import requests

url = 'http://localhost:8081/users'
myobj = {
    "ime": "Ena",
    "prezime": "Sotirovic",
    "username": "esotirovic15",
    "smer": "RAF",
    "predmeti": [
        {
            "ime": "RISO",
            "espb": 6
        },
        {
            "ime": "MTZPP",
            "espb": 6
        }
    ]
}

x = requests.post(url, json = myobj)

print(x.text)
