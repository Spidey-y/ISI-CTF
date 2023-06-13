from Crypto.Util.number import getPrime
from binascii import hexlify
from ptrlib import chunks

flag = "ISICTF{something_here}"
n = getPrime(256)*getPrime(256)


def rsa_enc(pt: bytes):
    e = 5
    pt = int(hexlify(pt), 16)
    return pow(pt, e, n)


pt = chunks(flag, 8)
ct = [None] * len(pt)
for i in range(len(pt)):
    ct[i] = rsa_enc(pt[i].encode('utf-8'))
print(f'ct = {ct}')

# ct = [4117836643573275904579678054384663100243444116297375620485928377598483524534805007485195027257, 519096359531565498385561024120306279020702460431909434107846631631477423626600205970646936576, 19848933599184426407756901127734078236531252674451052530427195339919245432439243069222959358976, 15404679736082060792329382533937122081380923964487595261309036477597951297641198038164803200000, 2319284866670232824808971278960172754299149421524872461147721700727440859301501489791677133824, 294702470758438353293]
