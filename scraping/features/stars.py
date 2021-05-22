from github import Github

# Retorna a quantidade de estrelas de um repositório
# Paramatros:
#   authToken: Token de autorização
#   repoURL: URL do repositório /{owner}/{repo} Ex: "tensorflow/tensorflow"

def getNumberOfStars(authToken, repoURL):
    repo = Github(authToken).get_repo(repoURL)

    return repo.stargazers_count