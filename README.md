# Automação de Planilhas de Vendas de Veículos

Este projeto visa automatizar a geração de relatórios de vendas de veículos para a XYZ Corporation International, uma revendedora de automóveis de luxo com sede em São Paulo. O CEO da empresa deseja analisar as vendas por fabricante ao longo dos anos, incluindo um gráfico de barras e um resumo das vendas totais por fabricante.

## Funcionalidades

1. **Geração de Tabela Pivô:** O script em Python gera uma tabela pivô a partir de um arquivo Excel contendo os dados de vendas de veículos. A tabela pivô inclui as colunas Fabricante, Preço de Venda e Ano.

2. **Criação de Gráfico de Barras:** Com base na tabela pivô gerada, o script cria um gráfico de barras mostrando as vendas totais por fabricante ao longo dos anos.

3. **Adição de Fórmulas:** O script adiciona fórmulas à planilha para calcular o total de vendas por fabricante.

4. **Envio por E-mail:** Por fim, o script envia a planilha automatizada por e-mail para o CEO da empresa.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas necessárias: pandas, openpyxl, matplotlib

## Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto-automacao-planilhas.git
