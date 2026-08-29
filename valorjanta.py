valor_total=float(input("Qual o valor total da conta? : "))
porcentagem=float(input("Qual a porcentagem da taxa de serviço? : "))
desconto=float(input("Qual o desconto?: "))
valor_da_taxa=(porcentagem/100)*valor_total
total_final=valor_total+valor_da_taxa-desconto
valor_por_amigo=total_final/3
print("O valor da taxa é", valor_da_taxa, ", o total final é", total_final, "e cada pessoa deverá pagar", valor_por_amigo, "reais.")
