**Como o Código Funciona**

    import os e import shutil: Importamos as duas bibliotecas necessárias. os é usado para interagir com o sistema operacional (caminhos, diretórios) e shutil para operações de alto nível como mover arquivos.

    organizar_arquivos(caminho_da_pasta): A função principal que recebe o caminho da pasta a ser organizada.

    os.listdir(caminho_da_pasta): Esta função lista todos os arquivos e diretórios dentro do caminho fornecido.

    os.path.join(...): É uma forma segura de construir caminhos, pois ele lida automaticamente com barras (/ ou \) do sistema operacional.

    os.path.splitext(nome_arquivo): Divide o nome de um arquivo em duas partes: o nome base e a extensão. Por exemplo, exemplo.txt se torna ('exemplo', '.txt').

    extensao[1:].lower(): Pega a extensão, remove o ponto inicial (.) e a converte para minúsculas. Se um arquivo não tiver extensão, ele será movido para uma pasta chamada "Outros".

    os.makedirs(pasta_destino, exist_ok=True): Cria a pasta de destino (ex: PDFs, Jpgs). O argumento exist_ok=True garante que o script não gere um erro se a pasta já existir.

    shutil.move(...): Move o arquivo do caminho original para o caminho de destino.


**Como Usar o Script**

    Salve o código: Copie o código acima e salve-o em um arquivo com extensão .py (ex: organizador.py).

    Edite o caminho: No final do script, na linha pasta_a_organizar = ..., substitua o exemplo pelo caminho da pasta que você deseja organizar.

    Execute o script: Abra o terminal (no Windows, pode ser o PowerShell ou o Prompt de Comando) e navegue até a pasta onde você salvou o arquivo. Execute-o com o comando:
    Bash

    python organizador.py

O script irá então organizar todos os arquivos da pasta especificada, criando e movendo-os para as pastas correspondentes. 
