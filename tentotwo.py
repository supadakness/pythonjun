print("Эта программа переводит десятичное число в двоичное.")

chislo = int(input("Введите число:"))

a = chislo

res = ''

while chislo > 0:
	ost = chislo % 2
	res += str(ost)
	chislo = chislo // 2
	
print("Число",a,"в двоичной системе равно:",res[::-1])
