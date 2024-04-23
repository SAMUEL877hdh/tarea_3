import string


def validar(valor):
	try:
        if len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

		if numero in '':
			raise ValueError("la contraseña no debe tener espacios en blanco")

		if not any(c.isupper() for c in contraseña):
            raise ValueError("La contraseña debe contener al menos un carácter en mayúscula.")
        
        if not any(c.isdigit() for c in contraseña):
            raise ValueError("La contraseña debe contener al menos un número.")
        
        if not any(c in string.punctuation for c in contraseña):
            raise ValueError("La contraseña debe contener al menos un carácter especial.")

def veri_contraseña():
    while True:
        try:
            contraseña_1 = input("Ingrese su contraseña: ")
            validar(contraseña1)
            
            contraseña2 = input("Confirme su contraseña: ")
            if contraseña1 != contraseña2:
                raise ValueError("Las contraseñas no coinciden. Inténtelo de nuevo.")
            
            break  
        
        except ValueError as e:
            print(e)

    print("Contraseña válida y confirmada.")

if __name__ == "__main__":
	veri_contraseña()