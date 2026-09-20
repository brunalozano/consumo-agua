# 💧 Sistema de Classificação de Consumo de Água 

Este projeto foi desenvolvido em **Python** com o objetivo de implementar um sistema que classifica o perfil de consumo dos imóveis e emite alertas educativos aos moradores.

O sistema faz a classificação de acordo com as seguintes regras:

- Se o tipo do imóvel for **comercial**, o sistema exibe: **"Tarifa comercial aplicada – consulte o plano corporativo."**
- Se o tipo do imóvel for **apartamento** e o consumo for menor que 10 m³, o sistema exibe: **"Consumo econômico – excelente controle de água!"**
- Se o tipo do imóvel for **apartamento** ou **casa** com o consumo de até 25 m³, o sistema exibe: **"Consumo moderado – dentro do padrão residencial."**
- Em qualquer outro caso, o sistema exibe: **"Consumo excessivo – adote medidas de economia e verifique vazamentos."**

## 🐍 Tecnologias utilizadas 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github)
![Água](https://img.shields.io/badge/Projeto-Consumo%20de%20Água-1E90FF)

## ⚙️ Como funciona 

O programa solicita ao usuário o **tipo do imóvel** e o **consumo mensal de água em m³**. Em seguida, utiliza as estruturas condicionais **if, elif e else** para analisar essas informações de acordo com as regras definidas. Após a classificação, o programa exibe uma mensagem educativa aos moradores, correspondente ao perfil de consumo identificado.

## ▶️ Como executar

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o arquivo `app.py`.
3. Clique no botão "Executar" localizado no canto superior direito do Visual Studio Code.
4. Digite o tipo do imóvel (comercial, apartamento ou casa) e o consumo mensal de água em m³ quando solicitado.
5. O programa classificará o perfil de consumo do imóvel e exibirá um alerta educativo. 