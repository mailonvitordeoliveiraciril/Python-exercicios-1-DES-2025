alunos = ["alice", "bruno", "carla",]

dias = ["segunda", "terça", "quarta", "quinta"]

reservar = [[ausente for _ in dias] for _ in alunos]
 print("preencha com 's' para presença e 'x' para ausencia")

for i, aluno in enumerate(alunos):
    print(f"/nALUNO: {aluno}")
    for j, dia in enumerate(dias):
        entrada = input( f" {dias}: ")
        if entrada.upper() == 's':
           reservas[i][j] = "presente"


print("/nTABELA DE RESERVAS:")
print(F"{'ALUNO':<10}") { ' '.join([f'' {dia:<10}' for dia in dias])}")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '.join([f'{reservar:<10}'for reserva in reservas[i]])}")