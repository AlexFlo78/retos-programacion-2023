
leters = "abcdefghijklmnopqrstuvwxyz"
symb = "*/#$%&=¿?"
num = list(range(0, 10))
characters = list(leters)+ list(symb) + list(leters.upper()) + num

def password():
	import random as rd 
	num_carac = rd.randint(8, 16)
	final = ""
	for i in range(num_carac):
		final = final + f"{rd.choice(characters)}"

	return final


contraseña = password()
print(contraseña)
