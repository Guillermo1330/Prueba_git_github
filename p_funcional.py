from functools import reduce

nombres = list(
    map(
        lambda x: x.strip(),
        input("Ingrese los nombres de los estudiantes: ").split(",")
    )
)

notas = list(
    map(
        lambda x: float(x),
        input("Ingrese las notas: ").split(",")
    )
)

estudiantes = list(zip(nombres, notas))

suma_notas = reduce(lambda acc, n: acc + n, notas)
promedio = suma_notas / len(notas)

aprobados = list(filter(lambda e: e[1] >= 7, estudiantes))
reprobados = list(filter(lambda e: e[1] < 7, estudiantes))
 
print("\nEstudiantes y notas:")
print(estudiantes)

print("\nCantidad de estudiantes:")
print(len(estudiantes))

print("\nPromedio del curso:")
print(promedio)

print("\nAprobados:")
print(aprobados)

print("\nReprobados:")
print(reprobados)