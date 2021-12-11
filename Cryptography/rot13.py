info = "synt{mur_VF_syn9_svtug1at}"
buff = ""
for i in info:
if i in "{}_1234567890":
buff += i
elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
buff += chr((ord(i)-13+26-ord('A'))%26+ord('A'))
else:
buff += chr((ord(i)-13+26-ord('a'))%26+ord('a'))
print buff