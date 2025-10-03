print("Kalkulator Sederhana")
print("Pilih operator: +   -   *   /")

angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == '+':
	hasil = angka1 + angka2
elif operator == '-':
	hasil = angka1 - angka2
elif operator == '*':
	hasil = angka1 * angka2
elif operator == '/':
	if angka2 != 0:
		hasil = angka1 / angka2
	else:
		hasil = "Error: Pembagi tidak boleh nol!"
else:
	hasil = "Operator tidak valid!"

print(f"Hasil: {hasil}")