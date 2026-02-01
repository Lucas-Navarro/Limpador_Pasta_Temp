import os 
import shutil

def limparPasta(caminho):
    # Se não existe este caminho no windows
    if not os.path.exists(caminho):
        print(f"Pasta não encontrada")
        return
    
    for item in os.listdir(caminho):
        # Entra no caminho certo
        caminhoTemp = os.path.join(caminho, item)

        try:
            # Se for pasta ou arquivo normal
            if os.path.isfile(caminhoTemp) or os.path.islink(caminhoTemp):
                os.remove(caminhoTemp)
            elif os.path.isdir(caminhoTemp):
                shutil.rmtree(caminhoTemp)
        except PermissionError:
            print(f"Arquivo em uso, ignorado {caminhoTemp}")
        except Exception as e:
            print(f"Erro ao excluir {caminhoTemp}: {e}")

# Limpa o temp normal
limparPasta("temp")


# Limpa o %TEMP%
temp_windows = os.environ.get("TEMP")
limparPasta(temp_windows)

print("Limpeza Concluída")
