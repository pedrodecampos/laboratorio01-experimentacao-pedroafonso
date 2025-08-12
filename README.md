# Laboratório 01 - Características de Repositórios Populares

Este projeto faz parte do **Laboratório 01** da disciplina de Medição e Experimentação em Engenharia de Software.  
O objetivo é coletar e analisar dados dos **1.000 repositórios mais populares do GitHub** para responder às questões de pesquisa RQ01 a RQ07.

---

## 📌 Objetivos
- Analisar idade, popularidade e atividade de repositórios open-source.
- Verificar frequência de contribuições externas (Pull Requests).
- Avaliar número de releases e frequência de atualizações.
- Identificar as linguagens mais comuns.
- Calcular percentual de issues fechadas.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **GitHub GraphQL API**
- **JQ** para processamento de JSON
- **Pandas** para análise de dados
- **Matplotlib** para visualização

---

## 📂 Estrutura do Repositório
```
.
├── coletor_github.py        # Script para coleta dos dados via GraphQL
├── github_repos.csv         # Base de dados coletada
├── relatorio_lab01_github_final.pdf  # Relatório final em PDF
├── top_linguaguem.png       # Gráfico das principais linguagens
└── README.md                # Este arquivo
```

---

## ⚙️ Como Executar a Coleta
1. Crie um **token de acesso pessoal** no GitHub (com permissão de leitura pública).
2. Exporte o token como variável de ambiente:
   ```bash
   export GITHUB_TOKEN="seu_token_aqui"
   ```
3. Execute o script:
   ```bash
   python3 coletor_github.py
   ```
4. Os resultados serão salvos no arquivo `github_repos.csv`.

---

## 📊 Resultados
- **Idade mediana:** 8.8 anos  
- **PRs mergeados (mediana):** 25.309  
- **Releases (mediana):** 104  
- **% Issues fechadas (mediana):** 68.4%  
- **Linguagens mais populares:** TypeScript, Go, C, PHP, Ruby, Python, JavaScript, Java, C++, Rust.

---

## 👨‍💻 Autor
**Pedro Afonso de Campos Faria Maciel**  
Pontifícia Universidade Católica de Minas Gerais (PUC Minas)  
Engenharia de Software — 7º Período
