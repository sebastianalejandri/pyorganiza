import os
import shutil

def organizar_arquivos(caminho_da_pasta):
    """
    Organiza arquivos em uma pasta, movendo-os para subdiretórios
    criados com base na extensão de cada arquivo.
    """
    # Verifica se o caminho fornecido é um diretório válido
    if not os.path.isdir(caminho_da_pasta):
        print(f"Erro: O caminho '{caminho_da_pasta}' não é um diretório válido.")
        return

    # Itera sobre todos os itens (arquivos e pastas) no diretório
    for nome_arquivo in os.listdir(caminho_da_pasta):
        caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo)

        # Ignora se for um diretório para evitar mover pastas
        if os.path.isdir(caminho_completo):
            continue

        # Obtém o nome base e a extensão do arquivo
        nome_base, extensao = os.path.splitext(nome_arquivo)
        
        # A extensão vem com um ponto, então removemos ele e usamos 'Outros' se não houver
        extensao = extensao[1:].lower() if extensao else 'outros'
        
        # Cria o nome da pasta de destino com base na extensão
        pasta_destino = os.path.join(caminho_da_pasta, extensao.capitalize())

        # Cria a pasta de destino se ela ainda não existir
        try:
            os.makedirs(pasta_destino, exist_ok=True)
        except OSError as e:
            print(f"Erro ao criar a pasta '{pasta_destino}': {e}")
            continue

        # Move o arquivo para a pasta de destino
        caminho_destino_completo = os.path.join(pasta_destino, nome_arquivo)
        try:
            shutil.move(caminho_completo, caminho_destino_completo)
            print(f"Arquivo '{nome_arquivo}' movido para '{pasta_destino}'.")
        except shutil.Error as e:
            print(f"Erro ao mover o arquivo '{nome_arquivo}': {e}")

# Exemplo de uso: substitua o caminho abaixo pela pasta que você deseja organizar
if __name__ == "__main__":
    pasta_a_organizar = "C:\\Users\\Seu_Usuario\\Downloads"  # Exemplo de caminho no Windows
    # Se estiver no Linux/macOS, use: pasta_a_organizar = "/home/seu_usuario/Downloads"
    organizar_arquivos(pasta_a_organizar)
