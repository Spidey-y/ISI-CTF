from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import itertools
ct = bytes.fromhex('a40c6502436e3a21dd63c1553e4816967a75dfc0c7b90328f00af93f0094ed62')
iv = bytes.fromhex('1df49bc50bc2432bd336b4609f2104f7')
target_plaintext = b'ISICTF{'  # The plaintext you want to find
for key in itertools.product(range(256), repeat=2):
    key = bytes(key)
    cipher = AES.new(pad(key,16), AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)
    if pt.find(target_plaintext) != -1 :
        print(f"Found key: {key.hex()}")
        break
else:
    print("Key not found.")
ct = bytes.fromhex('a40c6502436e3a21dd63c1553e4816967a75dfc0c7b90328f00af93f0094ed62')
iv = bytes.fromhex('1df49bc50bc2432bd336b4609f2104f7')
cipher = AES.new(pad(key,16), AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
print(pt)