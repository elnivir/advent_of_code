import hashlib

door_id = 'ugkcyxxp'.encode('utf-8')
index = 0
kod = 8 * [None]

while(1):
    temp = hashlib.md5(door_id + str(index).encode('utf-8')).hexdigest()
    if (temp[:5] == '00000' and temp[5] in ['0', '1', '2', '3', '4', '5', '6', '7']):
        if kod[int(temp[5])] == None:
            kod[int(temp[5])] = temp[6]
    if None not in kod:
        break
    index += 1

print("".join(kod))
