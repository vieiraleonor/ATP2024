# Análise Meteorológica

Este projeto é uma aplicação em Python que permite analisar dados meteorológicos diários, como temperaturas mínima e máxima, amplitude térmica, precipitação, entre outros. A aplicação oferece funcionalidades para calcular estatísticas meteorológicas e gerar gráficos de temperatura e precipitação com base em uma tabela de dados meteorológicos.

## Funcionalidades

A aplicação possui um menu com as seguintes opções:

1. **Temperatura média diária**: Calcula a temperatura média diária a partir das temperaturas mínima e máxima registradas.
2. **Guardar tabela em ficheiro**: Salva a tabela de dados meteorológicos em um arquivo de texto.
3. **Carregar a tabela**: Carrega uma tabela de dados meteorológicos a partir de um arquivo de texto.
4. **Temperatura mínima mais baixa**: Exibe a menor temperatura mínima registrada.
5. **Amplitude média térmica**: Calcula a amplitude térmica diária (diferença entre a temperatura máxima e mínima).
6. **Precipitação máxima**: Identifica o dia e o valor da maior precipitação registrada.
7. **Dias com precipitação superior a um valor `p`**: Exibe os dias onde a precipitação foi maior que um valor fornecido (`p`).
8. **Maior número consecutivo de dias com precipitação abaixo de `p`**: Calcula o maior período consecutivo de dias com precipitação abaixo de um valor fornecido (`p`).
9. **Gráficos de temperatura máxima, mínima e precipitação**: Gera gráficos de linha para temperaturas e um gráfico de barras para precipitação.

0. **Sair**: Encerra a aplicação.

## Como Usar

1. **Configuração Inicial**: Execute o código fornecido para iniciar o programa e exibir o menu.
2. **Selecionar Opções**: No menu, escolha a opção desejada digitando o número correspondente.
3. **Parâmetros para Precipitação (`p`)**: Para as opções 7 e 8, o usuário deverá fornecer um valor de precipitação (`p`).
4. **Visualizar Gráficos**: A opção 9 exibe gráficos de temperatura mínima e máxima ao longo do tempo e de precipitação diária.

## Funções

### Funções Principais

- **mostrar_menu**: Exibe o menu de opções.
- **medias(tabMeteo)**: Calcula a média diária da temperatura.
- **guardatabMeteo(t, fnome)**: Salva a tabela meteorológica em um arquivo de texto.
- **carregatabMeteo(fnome)**: Carrega a tabela meteorológica a partir de um arquivo de texto.
- **minMin(tabMeteo)**: Encontra a temperatura mínima mais baixa.
- **amplTerm(tabMeteo)**: Calcula a amplitude térmica diária.
- **maxChuva(tabMeteo)**: Identifica o dia e o valor da precipitação máxima.
- **diasChuvosos(tabMeteo, p)**: Lista os dias com precipitação superior ao valor `p`.
- **maxPeriodoCalor(tabMeteo, p)**: Calcula o maior número consecutivo de dias com precipitação abaixo do valor `p`.
- **grafTabMeteo(t)**: Gera gráficos de temperatura mínima e máxima e de precipitação.

### Exemplo de Dados

A estrutura da tabela meteorológica (exemplo `tabMeteo1`) é:

```python
tabMeteo1 = [
    ((2022, 1, 20), 2, 16, 0),
    ((2022, 1, 21), 1, 13, 0.2),
    ((2022, 1, 22), 7, 17, 0.01)]
```

- **Formato**: `((ano, mês, dia), temperatura mínima, temperatura máxima, precipitação)`
