from ppk2_api.ppk2_api import PPK2_API

geraete = PPK2_API.list_devices()
print(f"Gefundene PPK2 Geräte: {geraete}")