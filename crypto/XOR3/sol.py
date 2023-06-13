from pwn import xor


tmp = bytes.fromhex(
    "4953491504467d2865765b7d2f614f640f0d7d0e5f67212b2d292f28786671746027191a54446a0c4b023e503a6c076a3e5e5012455016497866712230271f4b01476e4516502e006a394a363e54454a1c4a4b1c")
# p ^ k1 ^ k2          # The first 40 bytes of hash.txt denotes to the A
A = tmp[:28]
B = tmp[28:56]     # p ^ k1
# p ^ k2          # The last 40 bytes (not 41 since we stripped the trailing newline character)
C = tmp[56:]


BC = xor(B, C)  # [B ^ C] = [p ^ p ^ k1 ^ k2] = [0 ^ k1 ^ k2] = [k1 ^ k2]
# [A ^ B ^ C] = [A ^ k1 ^ k2] = [p ^ k1 ^ k2 ^ k1 ^ k2] = [p ^ 0 ^ 0] = p
p = xor(BC, A)

flag = p.decode()
print(flag)
