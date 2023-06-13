flag = "ISICTF{something_here}"
c = []
for i in range(0, len(flag)):
    c.append((ord(flag[i]) ^ 0x41) - 0x3)
print(c)
# [5, 15, 5, -1, 18, 4, 55, 22, 110, 16, 27, 109, 47, 27, 114, 51, 111, 47, 110, 41, 111, 57]
