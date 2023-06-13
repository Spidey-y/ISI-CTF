flag = "ISICTF{something_here}"
key = ["some key here"]
c = []
for i in range(0, len(flag)):
    c.append((ord(flag[i]) ^ key[i % len(key)]))
print(c)
# [90, 100, 90, 116, 71, 113, 104, 111, 35, 101, 76, 6, 96, 104, 39, 64, 32, 68, 35, 90, 32, 104, 32, 65, 32, 89, 76, 64, 34, 67, 123, 7, 102, 67, 76, 3, 76, 92, 32, 78, 110]
