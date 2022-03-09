import hashlib

blockNumber = b"1"
nonce = 123_474_536_177      #2_241_619_641
data = b"S175910 ROBIN PERALA 032022"
prev = b"0000000000000000000000000000000000000000000000000000000000000000"
dataPrev = data + prev

input = blockNumber + str(nonce).encode() + dataPrev
hash = hashlib.sha256(input).hexdigest()

difficulty = 7  #notation is different because of the + "1"
zeros = "0" * difficulty + "1"

try:
    import time; start = time.time(); startNonce = nonce;
    while(hash > zeros):
        nonce += 1
        input = blockNumber + str(nonce).encode() + dataPrev
        hash = hashlib.sha256(input).hexdigest()

    
# try:
#   for n in range(nonce,nonce*2):
#     if (hash < zeroes): break
#     nonce += 1
#     input = blockNumber + str(nonce).encode() + data + prev
#     hash = hashlib.sha256(input).hexdigest()
finally:
    print()
    print(f"{nonce:_}")
    print(hash)
    print()
    total = (nonce-startNonce)/(time.time() - start)
    print(total)
    print()
    import winsound; winsound.Beep(400, 1500)



#1_647_315          Correct zeroes = 6      000000a02797159f685c67ffd91e1e9b62d8662ce86d3edc2c33b27c553f19fb
#988_484_189        Correct zeroes = 7      00000008ad4ba060e02cf384520242e807dfd6d51352e0a7bc44eb26d57dad37
#1_592_497_232      Correct zeroes = 8      00000000abb21c362a09486485bd3eb108b81b97cc0261727b2159aa46fd4b01
#123_474_536_177    Correct zeroes = 9      0000000006a9134f031d49bc30c9a9e920a9560191304ffdb9f8d032c98ef8ea


#While-loop
#4.19983444910086e-06
#5.641267536782546e-06
#6.593464250632194e-06
#Nonces per second
#220 027.26684935135
#214 465.8802881948
#212 830.90051925456
#Aalto
#777 384.6932506578
#800 737.6723608412
#796 521.3897081894
#Repl-it
#131 444.19433374115

#For-loop
#4.9446601547074465e-06
#4.494299505482679e-06
#4.734136845674251e-06





#Wrong - using update function
#725_532_937    Correct zeroes = 7
#2_280_070_841  Correct zeroes = 9      #00000000059e01237cac90500ed5ab6b7f31ac238c1a7464ede7aeee6ee8272c
