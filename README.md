# 📚 Sistema de Cadastro e Classificação de Alunos

## 📝 Descrição do Projeto

Este projeto foi desenvolvido como parte das atividades da disciplina **Pilares do Python**, pertencente ao curso de **Aperfeiçoamento em Inteligência Artificial**.

O objetivo do trabalho foi aplicar conceitos fundamentais da linguagem Python por meio da criação de um sistema de cadastro e processamento de notas de alunos.

O programa permite que o usuário informe a quantidade de alunos que deseja cadastrar, registre o nome e a nota de cada estudante e, ao final, organize os alunos conforme seu desempenho acadêmico:

- ✅ Alunos aprovados
- 🔄 Alunos em recuperação
- ❌ Alunos reprovados

As informações são armazenadas utilizando **listas de dicionários**, contendo o número da chamada, nome do aluno e sua respectiva nota.

---

## 🎯 Objetivo do Trabalho

O exercício teve como objetivo desenvolver a prática dos principais fundamentos da programação em Python, incluindo:

- Entrada e processamento de dados;
- Estruturas de repetição;
- Estruturas condicionais;
- Manipulação de listas e dicionários;
- Criação de funções;
- Organização e classificação de informações.

---

## 🎓 Curso

**Curso:** Aperfeiçoamento em Inteligência Artificial  
**Disciplina:** Pilares do Python  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**

Bibliotecas utilizadas:

- Nenhuma biblioteca externa necessária.

---


# ⚙️ Funcionamento e Implementação do Sistema

## 📌 Visão Geral

O sistema desenvolvido realiza o cadastro de alunos, processamento das notas e classificação automática conforme o desempenho acadêmico.

O fluxo do programa é dividido em três etapas principais:

1. Cadastro dos alunos;
2. Processamento e classificação das notas;
3. Organização e exibição dos resultados.

---

# 📝 Cadastro dos Alunos

Inicialmente, o usuário informa a quantidade de alunos que deseja cadastrar.

Para cada aluno cadastrado, o sistema solicita:

- Nome do aluno;
- Nota final obtida.

Exemplo de entrada:

```text
Quantidade Alunos: 3

Nome Aluno 1: João
Nota 1: 75

Nome Aluno 2: Maria
Nota 2: 55

Nome Aluno 3: Pedro
Nota 3: 30
```

Após a coleta das informações, cada aluno é armazenado utilizando um **dicionário Python**, contendo:

```python
{
    "Numero": 1,
    "Aluno": "João",
    "Notas": 75
}
```

Estrutura utilizada:

| Campo | Descrição |
|---|---|
| `Numero` | Número de chamada do aluno |
| `Aluno` | Nome do estudante |
| `Notas` | Nota final obtida |

---

# 📊 Classificação dos Alunos

Após o cadastro, o programa analisa a nota de cada aluno e realiza sua classificação.

As regras utilizadas são:

| Nota | Situação |
|---|---|
| Nota ≥ 60 | ✅ Aprovado |
| 40 ≤ Nota < 60 | 🔄 Recuperação |
| Nota < 40 | ❌ Reprovado |

A classificação é realizada utilizando estruturas condicionais:

```python
if Notas >= 60:
    aprovado.append(aluno)

elif Notas >= 40:
    recuperacao.append(aluno)

else:
    reprovado.append(aluno)
```

Cada aluno é direcionado para uma lista específica:

```python
aprovado = []

recuperacao = []

reprovado = []
```

---

# 📂 Organização dos Dados

O programa utiliza uma estrutura composta por:

- **Listas:** responsáveis por armazenar grupos de alunos;
- **Dicionários:** responsáveis por armazenar os dados individuais de cada aluno.

Exemplo:

```python
aluno = {
    "Numero": Numero,
    "Aluno": Alunos,
    "Notas": Notas
}
```

Essa estrutura permite acessar e manipular as informações de maneira organizada.

---

# 🔎 Ordenação dos Resultados

Após a classificação dos alunos, o sistema realiza a ordenação dos dados utilizando uma função personalizada:

```python
def ordenar_por_nome(aluno):
    return aluno["Aluno"].lower()
```

A função é utilizada pelo método `sort()`:

```python
aprovado.sort(key=ordenar_por_nome)

recuperacao.sort(key=ordenar_por_nome)

reprovado.sort(key=ordenar_por_nome)
```

Com isso, os alunos são organizados alfabeticamente pelo nome.

---

# 🚀 Como Executar o Projeto

## Pré-requisitos

É necessário possuir o Python 3 instalado.

Para verificar a versão:

```bash
python --version
```

---

## Execução

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Acesse a pasta do projeto:

```bash
cd nome-do-repositorio
```

Execute o programa:

```bash
python alunos.py
```

---

# 📌 Exemplo de Resultado

Após o processamento, o sistema apresenta os alunos separados por categoria:

```text
---------- Aprovados ----------
Número: 1
Nome: João
Nota: 75


---------- Recuperação ----------
Número: 2
Nome: Maria
Nota: 55


---------- Reprovados ----------
Número: 3
Nome: Pedro
Nota: 30
```

---

# 🧠 Conceitos de Python Aplicados

## Estrutura de Repetição

Foi utilizado o comando `for` para realizar o cadastro de todos os alunos:

```python
for Numero in range(1, n + 1):
```

---

## Estruturas Condicionais

Utilizadas para definir a situação acadêmica:

```python
if Notas >= 60:

elif Notas >= 40:

else:
```

---

## Listas

Utilizadas para armazenar os diferentes grupos de alunos:

```python
alunos_notas = []

aprovado = []

recuperacao = []

reprovado = []
```

---

## Dicionários

Utilizados para representar cada aluno:

```python
{
    "Numero": Numero,
    "Aluno": Nome,
    "Notas": Nota
}
```

---

## Funções

Foi criada uma função auxiliar para organizar os alunos:

```python
def ordenar_por_nome(aluno):
    return aluno["Aluno"].lower()
```

---

# 🔮 Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas:

- Criar uma interface gráfica utilizando Tkinter;
- Salvar os dados em arquivos `.json` ou `.csv`;
- Criar um sistema de busca de alunos;
- Implementar cadastro de diferentes turmas;
- Gerar relatórios automáticos;
- Criar gráficos de desempenho utilizando bibliotecas como Matplotlib.

---

# 👨‍💻 Autor

Desenvolvido por **Pedro**

Projeto acadêmico desenvolvido durante o curso de:

**Aperfeiçoamento em Inteligência Artificial**

Disciplina:

**Pilares do Python**
