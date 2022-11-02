tek_kare_toplam = 0
cift_kup_tolam = 0
i = 1
sinir = int(input("Seri Sınırını Giriniz: "))

#while i < sinir: sınırın dahil olmadığı döngü
while i <= sinir:
	if i % 2 == 0:
		cift_kup_tolam += (i**3)
	else:
		tek_kare_toplam += (i**2)
	i += 1

print(f"Cift sayilarin kupleri toplami: {cift_kup_tolam}")
print(f"Tek sayilarin kareleri toplami: {tek_kare_toplam}")