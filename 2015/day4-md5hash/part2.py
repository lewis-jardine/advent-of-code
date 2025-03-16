import hashlib

secret_key = 'ckczppom'

# Start at n, hash input with n, continue until output[0:6] == 000000
n = 0
while True:
    hash_input = secret_key + str(n)
    # Encode input into binary, hash then decode into hex
    hash_result = hashlib.md5(hash_input.encode()).hexdigest()
    if hash_result[0:6] == '000000':
        break
    n += 1

print(n, hash_result)