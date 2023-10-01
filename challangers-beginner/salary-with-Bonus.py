nome_funcionario = str(input(""))
salario_funcionario = float(input(""))
vendas_do_funcionario = float(input(""))

comissao = vendas_do_funcionario * 0.15
total_receber = salario_funcionario + comissao

print(f"TOTAL = R$ {total_receber:.2f}")
