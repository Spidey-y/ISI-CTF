from Crypto.Cipher import DES

flag = b"ISICTF{fake_flag}"
flag = flag.ljust( len(flag) + (8 - (len(flag) % 8)), b'\x00')
key = b"key"
iv = b"13371337"
des = DES.new(key, DES.MODE_OFB, iv)
ct = des.encrypt(flag)
f = open('output', 'wb')
f.write(ct)
