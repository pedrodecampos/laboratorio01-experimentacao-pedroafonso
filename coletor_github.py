import requests
import json
import csv
import os
from datetime import datetime, date
import statistics

# Substitua com seu token de acesso pessoal do GitHub
GITHUB_TOKEN = ""
API_URL = "https://api.github.com/graphql"

headers = {
    "Authorization": f"bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

def run_query(query, variables):
    """
    Função para executar a consulta GraphQL.
    """
    request = requests.post(API_URL, headers=headers, json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run with status code {request.status_code}. {request.text}")

def repo_age_in_days(created_at):
    """
    Calcula a idade do repositório em dias.
    """
    created_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ').date()
    today = date.today()
    return (today - created_date).days

def last_update_in_days(updated_at):
    """
    Calcula quantos dias se passaram desde a última atualização.
    """
    updated_date = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ').date()
    today = date.today()
    return (today - updated_date).days

def fetch_repositories():
    """
    Coleta os 1.000 repositórios usando paginação.
    """
    repositories = []
    end_cursor = None
    query = """
    query($cursor: String) {
        search(query: "stars:>1", type: REPOSITORY, first: 100, after: $cursor) {
            pageInfo {
                hasNextPage
                endCursor
            }
            nodes {
                ... on Repository {
                    name
                    nameWithOwner
                    createdAt
                    updatedAt
                    stargazerCount
                    primaryLanguage {
                        name
                    }
                    releases(first: 1) {
                        totalCount
                    }
                    pullRequests(states: MERGED) {
                        totalCount
                    }
                    issues(states: CLOSED) {
                        totalCount
                    }
                    openIssues: issues(states: OPEN) {
                        totalCount
                    }
                }
            }
        }
    }
    """
    while len(repositories) < 1000:
        variables = {"cursor": end_cursor}
        result = run_query(query, variables)
        
        data = result['data']['search']
        for repo in data['nodes']:
            if repo is not None and len(repositories) < 1000:
                repositories.append(repo)
        
        end_cursor = data['pageInfo']['endCursor']
        if not data['pageInfo']['hasNextPage']:
            break

    return repositories

def save_to_csv(data, filename="github_repos.csv"):
    """
    Salva os dados coletados em um arquivo CSV.
    """
    if not data:
        print("Nenhum dado para salvar.")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'name',
            'nameWithOwner',
            'createdAt',
            'updatedAt',
            'age_in_days',
            'last_updated_days_ago',
            'stargazerCount',
            'primaryLanguage',
            'releases_totalCount',
            'pullRequests_totalCount',
            'closed_issues_totalCount',
            'open_issues_totalCount',
            'total_issues',
            'closed_issues_percentage'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for repo in data:
            if repo is not None:
                total_issues = repo['issues']['totalCount'] + repo['openIssues']['totalCount']
                closed_issues_percentage = (repo['issues']['totalCount'] / total_issues) * 100 if total_issues > 0 else 0

                writer.writerow({
                    'name': repo['name'],
                    'nameWithOwner': repo['nameWithOwner'],
                    'createdAt': repo['createdAt'],
                    'updatedAt': repo['updatedAt'],
                    'age_in_days': repo_age_in_days(repo['createdAt']),
                    'last_updated_days_ago': last_update_in_days(repo['updatedAt']),
                    'stargazerCount': repo['stargazerCount'],
                    'primaryLanguage': repo['primaryLanguage']['name'] if repo['primaryLanguage'] else 'N/A',
                    'releases_totalCount': repo['releases']['totalCount'],
                    'pullRequests_totalCount': repo['pullRequests']['totalCount'],
                    'closed_issues_totalCount': repo['issues']['totalCount'],
                    'open_issues_totalCount': repo['openIssues']['totalCount'],
                    'total_issues': total_issues,
                    'closed_issues_percentage': closed_issues_percentage
                })
    print(f"Dados salvos com sucesso em '{filename}'")

def summarize_data(data):
    """
    Calcula as medianas para as RQs.
    """
    ages = [repo_age_in_days(r['createdAt']) for r in data]
    last_updates = [last_update_in_days(r['updatedAt']) for r in data]
    prs = [r['pullRequests']['totalCount'] for r in data]
    releases = [r['releases']['totalCount'] for r in data]
    closed_percentage = [
        (r['issues']['totalCount'] / (r['issues']['totalCount'] + r['openIssues']['totalCount'])) * 100
        if (r['issues']['totalCount'] + r['openIssues']['totalCount']) > 0 else 0
        for r in data
    ]
    langs = [r['primaryLanguage']['name'] if r['primaryLanguage'] else 'N/A' for r in data]

    print("\n=== Resultados (Medianas) ===")
    print(f"RQ01 - Idade (anos): {statistics.median(ages)/365:.1f}")
    print(f"RQ02 - PRs mesclados: {statistics.median(prs)}")
    print(f"RQ03 - Releases: {statistics.median(releases)}")
    print(f"RQ04 - Dias desde última atualização: {statistics.median(last_updates)}")
    print(f"RQ06 - % issues fechadas: {statistics.median(closed_percentage):.2f}%")

    print("\n=== RQ05 - Linguagens (contagem) ===")
    for lang, count in {l: langs.count(l) for l in set(langs)}.items():
        print(f"{lang}: {count}")

if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("ERRO: Por favor, substitua 'GITHUB_TOKEN' pelo seu token do GitHub.")
    else:
        print("Coletando dados dos 1.000 repositórios mais populares...")
        repositories_data = fetch_repositories()
        save_to_csv(repositories_data)
        summarize_data(repositories_data)
