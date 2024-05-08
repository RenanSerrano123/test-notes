soma=0.0
z=int(input("Qual o número total de trabalhos? "))
for i in range(1,z+1,1):
  trabalho=float(input("Qual a nota do trabalho "+str(i)+"? "))
  soma=soma+trabalho
media1=(soma/z)*0.6
prova=float(input("Qual a nota da prova? "))
media2=prova*0.4
mediafinal=media1+media2
print("A nota do aluno foi de: ",mediafinal)
if mediafinal<5:
  print("O conceito desse aluno nessa matéria foi F")
elif 5<=mediafinal<6:
  print("O conceito desse aluno nessa matéria foi D")
elif 6<=mediafinal<7:
  print("O conceito desse aluno nessa matéria foi C")
elif 7<=mediafinal<8.5:
  print("O conceito desse aluno nessa matéria foi B")
elif 8.5<=mediafinal<=10:
  print("O conceito desse aluno nessa matéria foi A")