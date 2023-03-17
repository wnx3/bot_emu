import urllib.request

# Lê a versão atual do arquivo version.txt
with open("version.txt", "r") as f:
    current_version = f.read().strip()

# Obtém o número da última versão do arquivo version.txt no repositório no GitHub
url = "https://raw.githubusercontent.com/wnx3/bot_emu/main/version.txt"
with urllib.request.urlopen(url) as response:
    latest_version = response.read().decode().strip()

# Compara as versões e atualiza o arquivo se houver uma nova versão disponível
if current_version != latest_version:
    url = "https://raw.githubusercontent.com/<SEU_USUARIO>/<NOME_DO_REPOSITORIO>/main/arquivo.py"
    with urllib.request.urlopen(url) as response:
        code = response.read().decode()

    with open("arquivo.py", "w") as f:
        f.write(code)

    # Atualiza o número da versão no arquivo version.txt
    with open("version.txt", "w") as f:
        f.write(latest_version)
