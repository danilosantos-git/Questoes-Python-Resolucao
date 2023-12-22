# 3. Como critérios para passar em um exame o aluno deve anotar [(> 7.5 matemática) e (>
# 6.5 português)] ou [(> 8 redação) e (>6 matemática) e (> 8 português)]. Peça as três
# notas do aluno e em apenas uma única expressão booleana avalie se o aluno passou
# ou falhou no teste.

nota_mat = float(input("Nota de Matemática: "))
nota_port = float(input("Nota de Português: "))
nota_redacao = float(input("Nota de Redação: "))

aprovado = ((nota_mat > 7.5) and (nota_port > 6.5)) or ((nota_redacao > 8) and (nota_mat > 6) and (nota_port > 8))

if aprovado:
    print("Aprovado!")
else:
    print("Reprovado!")
