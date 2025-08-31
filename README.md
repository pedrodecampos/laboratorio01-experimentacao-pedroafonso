# LAB01 — Características de Repositórios Populares no GitHub

Trabalho da disciplina **Laboratório de Experimentação de Software** (PUC Minas).
Analisa 1.000 repositórios mais populares do GitHub para responder às RQs propostas.

##  Estrutura (proposta do pacote)
- `coletor_github.py` — coleta via **GitHub GraphQL API** com paginação (1000 repositórios).
- `github_repos.csv` — dados brutos coletados.
- `analise_repositorios_formatado.pdf` — relatório final com **RQ01–RQ07**, gráficos e tabela por linguagem.
- `imgs/` ou arquivos `.png` — gráficos: distribuição de linguagens (barra + pizza), idade, PRs mesclados, releases, dias desde última atualização, % issues fechadas.
- `README.md` — este arquivo.

---

##  Como executar
1. Crie um **token pessoal do GitHub** e cole em `GITHUB_TOKEN` no `main.py`.
2. Rode a coleta:
   ```bash
   python coletor_github.py
   ```
3. Verifique o arquivo gerado `github_repos.csv`.
4. Rode a análise (separada ou no próprio script) para gerar os gráficos e o PDF final.

---

##  Questões de Pesquisa (RQs)
- **RQ01** — Sistemas populares são maduros/antigos? *(idade desde criação)*  
- **RQ02** — Recebem muita contribuição externa? *(PRs mesclados)*  
- **RQ03** — Lançam releases com frequência? *(total de releases)*  
- **RQ04** — São atualizados com frequência? *(dias desde última atualização)*  
- **RQ05** — São escritos nas linguagens mais populares? *(linguagem primária)*  
- **RQ06** — Possuem alto percentual de issues fechadas? *(fechadas / total)*  
- **RQ07 (Bônus)** — Por linguagem: PRs, releases e atualização variam conforme a linguagem?

---

##  Metodologia (resumo)
- Consulta GraphQL paginada (100 → 1000 repositórios) com filtro por estrelas.
- Limpeza básica e derivação de métricas (idade, dias desde atualização, % issues fechadas).
- **Mediana** como estatística de referência para RQ01–RQ06 (robusta a outliers).
- **Contagem por categoria** para RQ05 (linguagens).
- **Agrupamento por linguagem** para RQ07 (medianas por linguagem, com corte mínimo de amostras).

---

##  Hipóteses iniciais (antes da análise)
- Projetos populares tendem a ser **mais antigos** (maior maturidade).
- Recebem **muitas contribuições externas** (alto nº de PRs).
- **Lançam releases** com certa regularidade.
- **São atualizados** com frequência.
- São escritos em **linguagens populares** (Python, Java, JS/TS, Go, etc.).
- Mantêm **alta taxa de issues fechadas** (boa manutenção).

---

##  Resultados (sumário de medianas)
- **Idade (RQ01):** ~**9 anos**  
- **PRs mesclados (RQ02):** ~**25.8k**  
- **Releases (RQ03):** ~**102**  
- **Dias desde última atualização (RQ04):** ~**1.221 dias (~3,3 anos)**  
- **% issues fechadas (RQ06):** ~**69%**  
- **Linguagens (RQ05 – Top 10):** C++, Go, TypeScript, Rust, Python, Ruby, Java, C, PHP, JavaScript

**RQ07 (por linguagem – exemplo de achados):**
- **Python**: mediana de releases relativamente alta e menor tempo desde última atualização frente a algumas linguagens.
- **C++/Rust**: altas medianas de PRs, porém com janelas de atualização um pouco maiores em relação a Python.
- **Go/TypeScript**: altos valores de PRs e releases, confirmando ecossistemas ativos.


---

##  Discussão final (comparando hipóteses × achados)
- **Maturidade**: confirmada — mediana de ~9 anos.
- **Contribuições externas**: confirmada — valores muito altos de PRs.
- **Releases**: confirmada — mediana > 100.
- **Atualizações**: **parcial** — a mediana de ~3,3 anos sugere muitos projetos estáveis (menos commits recentes), sem necessariamente indicar abandono.
- **Linguagens**: confirmada — predominam linguagens mainstream.
- **Issues fechadas**: confirmada — ~69% indica boa manutenção.
- **RQ07**: há diferenças entre linguagens; ecossistemas mais “rápidos” (ex.: Python/Go/TS) tendem a ter ciclos mais frequentes de release/atualização, enquanto outros mostram maior volume de PRs com cadência mais espaçada.

---

##  Itens avaliativos (checklist do enunciado)
- [x] **Lab01S01** — consulta GraphQL (100 repositórios), todos os campos necessários.  
- [x] **Lab01S02** — paginação (1000), CSV, primeira versão do relatório com hipóteses.  
- [x] **Lab01S03** — análise/visualização, relatório final (medianas, discussão), **RQ07 (bônus)**.  

---

##  Créditos
- Aluno: **Pedro Afonso de Campos Faria Maciel**  
- Curso: **Engenharia de Software** — **PUC Minas**  
- Disciplina: **Laboratório de Experimentação de Software**
