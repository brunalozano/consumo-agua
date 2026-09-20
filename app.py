# Sistema de Classificação de Consumo de Água
# Entrada
imovel = input("Digite o tipo do imóvel: ")
consumo_mensal_agua = float(input("Digite o consumo mensal de água em m³: "))

print()

# Processamento e Saída - Classifica o perfil de consumo dos imóveis e exibe alertas educativos.
if imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif imovel == "apartamento" and consumo_mensal_agua < 10:
    print("Consumo econômico – excelente controle de água!")
elif (imovel == "apartamento" and consumo_mensal_agua <= 25) or (imovel == "casa" and consumo_mensal_agua <= 25):
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")