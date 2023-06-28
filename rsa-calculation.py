alice_p = 11
alice_q = 13
bob_p = 17
bob_q = 23
starting_e = 1

dict_messages = {'a': ['Hai', 'Lulus'], 'b': ['Hello', 'Alhamdulillah']}
messages_in_ascii = {'a': {'Hai': [72, 97, 105], 'Lulus': [76, 117, 108, 117, 115]}, 'b': {'Hello': [72, 101, 108, 108, 111], 'Alhamdulillah': [65, 108, 104, 97, 109, 100, 117, 108, 105, 108, 108, 97, 104]}}

def calculateMod(p, q):
    return p * q

def calculatePhi(p, q):
    return (p - 1) * (q - 1)

def calculatePrivateKey(p, q, e):
     # Calculate phi(n)
    phi = (p - 1) * (q - 1)

    # Calculate the modular inverse of e
    d = mod_inverse(e, phi)

    return d

def mod_inverse(a, m):
    # Extended Euclidean algorithm to find the modular inverse
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return gcd, y, x - (a // b) * y

    gcd, x, _ = extended_gcd(a, m)

    # Make sure the modular inverse is positive
    inverse = (x % m + m) % m

    return inverse

def calculatePublicKey(starting_e, phi):
    e = starting_e
    # Find a value for e that satisfies the conditions
    while True:
        if gcd(e, phi) == 1 and e > 1 and e < phi:
            break
        # print('gcd_num', gcd(e, phi), 'greater than 1', e > 1, 'greater than ', phi, e < phi)
        e += 1

    # print('final gcd number', e)
    return e

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def keyGeneration():
    global alice_mod
    global bob_mod
    global alice_pub
    global bob_pub
    global alice_pri
    global bob_pri

    for i in range(2):
        if i == 0:
            print('----------------Key Info For Alice-----------------')
            alice_mod = calculateMod(alice_p, alice_q)
            print('alice_n', alice_mod)
            alice_phi = calculatePhi(alice_p, alice_q)
            print('alice_phi', alice_phi)
            alice_pub = calculatePublicKey(starting_e, alice_phi)
            print('alice_pub', alice_pub)
            alice_pri = calculatePrivateKey(alice_p, alice_q, alice_pub)
            print('alice_pri', alice_pri)
        else:
            print('----------------Key Info For Bob-----------------')
            bob_mod = calculateMod(bob_p, bob_q)
            print('bob_n', bob_mod)
            bob_phi = calculatePhi(bob_p, bob_q)
            print('bob_phi', bob_phi)
            bob_pub = calculatePublicKey(starting_e, bob_phi)
            print('bob_pub', bob_pub)
            bob_pri = calculatePrivateKey(bob_p, bob_q, bob_pub)
            print('bob_pri', bob_pri)
            print('----------------End Key Info-----------------')

def main():
    keyGeneration()
    print('type 1 to convert dict_message to ASCII and ecnrypt it')
    print('type 2 to input manual ASCII')
    to = int(input('what to do? '))

    if to == 1 :
        stringToAscii()
    elif to == 2 :
        manualAscii()
    else:
        print('Error! select 1 or 2')

def stringToAscii():
    dict_ascii = {}
    for i in dict_messages:
        res = {}

        for j in dict_messages[i]:
            res[j] = [ord(num) for num in j]

        dict_ascii[i] = res

    print("The message list is : " + str(dict_messages))
    print("The ascii list is : " + str(dict_ascii))
    print('----------done--------- ')
    # return dict_ascii
    # main()
    encDec(dict_ascii)

def encDec(dict):
    for i in dict:
        for j in dict[i]:
            print(j)
            for k in dict[i][j]:
                if i == 'a':
                    aliceSendToBob(k)
                else:
                    bobSendToAlice(k)

def aliceSendToBob(message):
    enc_pow = message ** bob_pub
    enc_mod = enc_pow % bob_mod
    print('Alice`s cyphertext sends to Bob: ', enc_mod)
    bobReceiveFromAlice(enc_mod)

def bobReceiveFromAlice(enc_mod):
    dec_pow = enc_mod ** bob_pri
    dec_mod = dec_pow % bob_mod
    print('Bob received cyphertext from Alice: ', enc_mod)
    print('Bob decrypted the message from Alice: ', dec_mod)
    print('string is', chr(dec_mod))

def bobSendToAlice(message):
    enc_pow = message ** alice_pub
    enc_mod = enc_pow % alice_mod
    print('Bob`s cyphertext sends to Alice: ', enc_mod)
    aliceReceiveFromBob(enc_mod)

def aliceReceiveFromBob(enc_mod):
    dec_pow = enc_mod ** alice_pri
    dec_mod = dec_pow % alice_mod
    print('Alice received cyphertext from Bob: ', enc_mod)
    print('Alice decrypted the message from Bob: ', dec_mod)
    print('string is', chr(dec_mod))

def manualAscii():
    a = int(input('Enter message in ASCII number: '))
    print('string is', chr(int(a)))
    sender = input('Enter sender: ')
    if sender == 'a':
        aliceSendToBob(a)
    elif sender == 'b':
        bobSendToAlice(a)

main()
    




