#fuction input -> retoma string
name = input('Como te llamas? \n')
age=int(input('Cuantos años tienes? \n'))
future=int(input('Cuantos años mas? \n'))

print("Hola "+name)
print("En  "+ str(future) + "años tendras"+ str(age + future))

# Format String

text_complete = "Hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age + future))

print(f"Hola{name}, en {future} años tendras {age + future} años")