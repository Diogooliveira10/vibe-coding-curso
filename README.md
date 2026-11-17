# Meus gastos

Aplicativo simples para registrar gastos pessoais e acompanhar quanto foi gasto
em cada categoria. Criado com Python e Streamlit.

## Funcionalidades

- Registrar um gasto com categoria, valor e data.
- Consultar a lista de gastos e o total acumulado.
- Visualizar os valores por categoria em um gráfico de barras.
- Salvar os dados em um arquivo CSV para recuperá-los ao recarregar o app.
- Apagar todos os gastos pelo botão **Limpar tudo**.

## Requisitos

- Python 3 instalado.
- GitHub Codespaces ou outro ambiente com terminal.

## Como executar no GitHub Codespaces

Abra um terminal na pasta do projeto e execute os comandos abaixo:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

O Streamlit exibirá um endereço para abrir o aplicativo. No Codespaces, clique
em **Open in Browser** quando a notificação aparecer.

Se já criou o ambiente virtual antes, não é necessário criá-lo novamente.
Quando abrir um terminal novo, ative-o com `source .venv/bin/activate`.

## Dados

Os gastos são salvos em `gastos.csv`, na mesma pasta de `app.py`. O arquivo é
criado quando o primeiro gasto é adicionado e atualizado a cada novo registro.
O botão **Limpar tudo** apaga os registros do app e deixa o CSV vazio.

O arquivo `gastos.csv` está no `.gitignore` para evitar que dados pessoais sejam
enviados ao GitHub por engano. Faça uma cópia do CSV em outro local se quiser
manter um backup fora do Codespace.

## Estrutura do projeto

```text
.
├── app.py
├── requirements.txt
└── README.md
```

`gastos.csv` é criado automaticamente depois que você adiciona o primeiro
gasto.
