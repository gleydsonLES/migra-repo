import subprocess
import os

#Nome do Projeto
project_name = "Nome do projeto"

#Token
az_pat = "token do repo"

# Lista de nomes dos repositórios
repository_names = [
    "nome do repos",
]

# Loop para clonar os repositórios
for repo_name in repository_names:
    url = f"ssh://url do repo antigo/{project_name}/_git/{repo_name}"
    subprocess.call(["git", "clone", "--bare", url])

# Loop para entrar em cada diretório clonado e executar git push --mirror para os destinos de teste
for repo_name in repository_names:
    # Concatenar repo_name com ".git"
    repo_path = repo_name + ".git"
    # Entrar no diretório clonado
    os.chdir(repo_path)
    
    # Executar git push --mirror para os destinos de teste
    for repo_name in repository_names:
        url = f"url nova do repo/_git/{repo_name}"
        subprocess.call(["git", "push", "--mirror", url])
    
    # Voltar ao diretório anterior
    os.chdir("..")

print("Operação concluída: git push para os repositórios clonados foi executado com sucesso.")





