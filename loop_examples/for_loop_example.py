import random

rast_gele_sayi = random.randint(1, 100)
hak = 0
while hak < 5:
	hak += 1
	tahmin = int(input("Tahmininiz: "))
	if tahmin > rast_gele_sayi and hak < 5:
		print("Tahmininizi küçültün")
	elif tahmin < rast_gele_sayi and hak < 5:
		print("Tahmininizi büyütün")
	elif rast_gele_sayi == tahmin:
		print("Tebrikler")
		break
	else:
		print(rast_gele_sayi)
print("😛 Hak bitti !")
