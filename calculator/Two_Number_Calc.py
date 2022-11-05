sayi_1 = int(input("1.Sayiyi Giriniz: "))
sayi_2 = int(input("2.Sayiyi Giriniz: "))
toplama = "+"
cikarma = "-"
carpma = "*"
bolme = "/"
mod = "%"

print(f"""Yapmak istediğiniz islemin isaretini yaziniz ve Enter'a basiniz:
Toplama: {toplama}
Cikarma: {cikarma}
Carpma : {carpma}
Bolme  : {bolme}
Mod Alma:{mod}
""")

islem = str(input())

if islem == toplama:
	print(sayi_1 + sayi_2)
elif islem == cikarma:
	print(sayi_1 - sayi_2)
elif islem == carpma:
	print(sayi_1 * sayi_2)
elif islem == bolme:
	if sayi_2 != 0:
		print(sayi_1 / sayi_2)
	else:
		print("Sonsuz")
elif islem == mod:
	print(sayi_1 % sayi_2)
else:
	print("Yanlis karakter yazildi")
