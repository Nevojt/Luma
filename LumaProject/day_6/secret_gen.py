import secrets

pepper = secrets.token_hex(32)  # Генерує 64-символьний рядок (32 байти)
print(pepper)
