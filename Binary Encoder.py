import bitarray




def scramble(number:str):
    length = len(number)
    chunks = []
    new_number = ''
    if length >= 10:
        i = 10
        while length%i != 0 and i > 0:
            i -= 1

        if i == 1:
            chunks = list(number)
        else:
            n = int(length/i)
            for j in range(n):
                if j == 0:
                    chunks.append(number[j:i])
                else:
                    chunks.append(number[j*(i):j*(i)+i])
    else:
        i = 0
        if length%2 != 0:
            length += 1
            i = -1
        n = int(length/2)
        chunks.append(number[:n])
        chunks.append(number[n:])

    new_number = str(i)+','
    
    for chunk in chunks[::-1]:
        new_number = new_number+chunk

    return new_number

def unscramble(number:str):
    i,scrambled_number = number.split(',')
    i = int(i)
    length = len(scrambled_number)
    new_number = ''
    chunks = []
    if i == -1 or i == 0:
        n = int((length/2))
        chunks.append(scrambled_number[:n])
        chunks.append(scrambled_number[n:])
    
    elif i == '1':
        chunks = list(scrambled_number)

    else:
        for j in range(int(length/i)):
            if j == 0:
                chunks.append(scrambled_number[j:i])
            else:
                chunks.append(scrambled_number[j*(i):j*(i)+i])
    
    for chunk in chunks[::-1]:
        new_number = new_number+chunk

    return new_number

def encrypt(string):

    ba = bitarray.bitarray()
    ba.frombytes(string.encode('utf-8'))
    bit = ba.to01()
    encrypted = str(int(bit,2))
    encrypted = scramble(encrypted)
    return encrypted

def decrypt(number):
    try:
        number = int(unscramble(number))
        bit_str = bin(number)[2:]
        while len(bit_str) % 8 != 0:
            bit_str = '0' + bit_str
        
        ba_2 = bitarray.bitarray(bit_str)
        decrypted_bytes = ba_2.tobytes()
        decrypted_str = decrypted_bytes.decode('utf-8')
        return decrypted_str
    except:
        return '[ERROR!]'

input_str = input('Enter a string: ')
encrypted_value = encrypt(input_str)
print(f'Encrypted: {encrypted_value}')

decrypted_str = decrypt(encrypted_value)
print(f'Decrypted: {decrypted_str}')
