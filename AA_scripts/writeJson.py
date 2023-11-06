import json
import os
from load_data import load

file = r'ProyectoFinal/AA_scripts/data.json'

data = {}
data['info'] = []

def add(plat, user, pssw):
    data['info'].append({
        'Plataforma: ': plat,
        'Usuario: ' : user,
        'Contraseña: ' : pssw
    })

plat, user, pssw = load()
add(plat, user, pssw)

if os.path.isfile(file):
    with open(file, 'w'):
        json.dump(data, file, indent=4)

  