import hashlib

door_id = 'ugkcyxxp'.encode('utf-8')
index = 0
kod = ""

while(1):
    temp = hashlib.md5(door_id + str(index).encode('utf-8)')).hexdigest()
    if (temp[:5] == '00000'):
        kod = kod + temp[5]
    index += 1
    if len(kod) == 8:
        break

print(kod)
