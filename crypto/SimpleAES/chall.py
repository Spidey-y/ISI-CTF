from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import flag


key = pad(open("/dev/urandom", "rb").read(2), 16)
iv = open("/dev/urandom", "rb").read(16)

cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(flag.encode(), 16))

print(f"iv = {iv.hex()}")
print(f"ct = {ct.hex()}")

# iv = 813c5def8998acecf96ae0fd8c0af844
# ct = 8ceeab5f2db4424386053833f2bd9144f6d52e23f1c2cb30ca4e6895b9a7f9e5
