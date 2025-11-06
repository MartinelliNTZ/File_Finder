"""
==============================================
🧾 Script: Localizador e Copiador de Arquivos
Autor: M. Martinelli
Versão: 1.4 (log detalhado, ignore case e proteção de pastas)
Identificador: lca25v14
==============================================

Descrição:
-----------
Localiza arquivos cujo nome contenha um termo informado (sem diferenciar maiúsculas/minúsculas),
gera logs detalhados e, opcionalmente, copia os arquivos encontrados.

Opções:
--------
[ENTER] → Copiar arquivos e gerar log.
[1] → Gerar apenas o log (sem copiar).
[ESC] → Cancelar execução.

Melhorias desta versão:
------------------------
- Busca "ignore case" (não diferencia letras maiúsculas/minúsculas).
- Log inclui: pasta original, nome completo, data e hora de modificação.
- Ignora automaticamente a pasta de log e a pasta de destino de cópias.
- Ignora o próprio script.
- Log formatado com cabeçalho e contagem final.

Saídas:
--------
- Log oculto: pasta oculta `log`.
- Log visível (`log.txt`): apenas se opção = 1.
- Pasta de destino: criada se houver cópia.

Compatibilidade:
----------------
Windows 10/11, Python 3.8+
"""

import os
import shutil
import msvcrt
import ctypes
import time
from datetime import datetime

code = "lca25v14"


def obter_opcao():
    """Exibe o menu e retorna a opção escolhida pelo usuário."""
    while True:
        print("\nPressione ENTER para copiar os arquivos e criar um log")
        print("Digite 1 para apenas criar o log (sem copiar)")
        print("Ou pressione ESC para cancelar\n")

        print("Escolha: ", end="", flush=True)
        tecla = msvcrt.getch()

        if tecla == b'\r':  # ENTER
            print("ENTER")
            return ""
        elif tecla == b'1':
            print("1")
            return "1"
        elif tecla == b'\x1b':  # ESC
            print("\n❌ Operação cancelada pelo usuário.")
            exit()
        else:
            print("\nOpção inválida! Tente novamente.\n")


def obter_pasta_raiz():
    """Retorna a pasta onde o script está localizado."""
    return os.path.dirname(os.path.realpath(__file__))


def criar_pasta(nome, pasta_raiz, opcao):
    """Cria a pasta de destino apenas se a opção envolver cópia."""
    if opcao == "":  # ENTER → cópia
        nova_pasta = os.path.join(pasta_raiz, nome)
        os.makedirs(nova_pasta, exist_ok=True)
        return nova_pasta
    else:
        return None


def criar_log_path(pasta_raiz):
    """Cria a pasta oculta `log` e retorna o caminho do log datado."""
    log_dir = os.path.join(pasta_raiz, "log")
    os.makedirs(log_dir, exist_ok=True)

    # Ocultar pasta no Windows
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ctypes.windll.kernel32.SetFileAttributesW(log_dir, FILE_ATTRIBUTE_HIDDEN)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{code}_LOG_{timestamp}.txt"
    return os.path.join(log_dir, log_filename)


def registrar_log_e_copiar(nome, pasta_raiz, nova_pasta, opcao):
    """
    Busca arquivos cujo nome contenha `nome` (ignore case),
    registra informações completas no log e copia arquivos (se aplicável).

    Proteções:
        - Não busca dentro da pasta `log` nem da `nova_pasta`.
        - Ignora o próprio script.
    """
    log_path = criar_log_path(pasta_raiz)
    log_dir = os.path.dirname(log_path)
    script_path = os.path.realpath(__file__)
    excluded_dirs = {os.path.realpath(log_dir)}
    if nova_pasta:
        excluded_dirs.add(os.path.realpath(nova_pasta))

    nome_lower = nome.lower()
    encontrados = 0

    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"========== LOCALIZADOR DE ARQUIVOS ==========\n")
        log.write(f"Termo buscado (ignore case): {nome}\n")
        log.write(f"Data e hora da busca: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        log.write(f"Pasta base: {pasta_raiz}\n")
        log.write("=" * 45 + "\n\n")

        # Busca recursiva com proteção de diretórios
        for dirpath, dirnames, filenames in os.walk(pasta_raiz, topdown=True):
            dir_real = os.path.realpath(dirpath)

            # Remover diretórios que não devem ser vasculhados
            dirnames[:] = [
                d for d in dirnames
                if os.path.realpath(os.path.join(dirpath, d)) not in excluded_dirs
            ]

            for filename in filenames:
                caminho_completo = os.path.realpath(os.path.join(dirpath, filename))

                # Pular o próprio script
                if caminho_completo == script_path:
                    continue

                # Verificar se nome contém o termo (ignore case)
                if nome_lower in filename.lower():
                    encontrados += 1
                    data_mod = datetime.fromtimestamp(os.path.getmtime(caminho_completo))
                    data_fmt = data_mod.strftime("%d/%m/%Y %H:%M:%S")

                    log.write(f"[{encontrados}] Arquivo encontrado:\n")
                    log.write(f"  • Nome: {filename}\n")
                    log.write(f"  • Pasta: {dirpath}\n")
                    log.write(f"  • Caminho completo: {caminho_completo}\n")
                    log.write(f"  • Modificado em: {data_fmt}\n")
                    log.write("-" * 45 + "\n")

                    # Copiar se for opção ENTER
                    if opcao == "":
                        copiar_arquivo(caminho_completo, nova_pasta, filename)

        log.write(f"\nTotal de arquivos encontrados: {encontrados}\n")
        log.write("========== FIM DO LOG ==========\n")

    # Cria log visível se for apenas log (1)
    log_visivel = None
    if opcao == "1":
        log_visivel = os.path.join(pasta_raiz, "log.txt")
        shutil.copy(log_path, log_visivel)

    return log_path, log_visivel, encontrados


def copiar_arquivo(origem, destino_pasta, nome_arquivo):
    """Copia o arquivo para a pasta de destino, evitando sobrescritas."""
    if not destino_pasta:
        return

    destino = os.path.join(destino_pasta, nome_arquivo)
    if not os.path.exists(destino):
        shutil.copy(origem, destino)
    else:
        base, ext = os.path.splitext(nome_arquivo)
        i = 1
        while os.path.exists(os.path.join(destino_pasta, f"{base}_{i}{ext}")):
            i += 1
        shutil.copy(origem, os.path.join(destino_pasta, f"{base}_{i}{ext}"))


def main():
    """Executa o fluxo principal do script."""
    print("----LOCALIZADOR DE ARQUIVOS-----")
    nome = input("Digite o nome (ou parte do nome) do arquivo a ser localizado: ")
    opcao = obter_opcao()
    pasta_raiz = obter_pasta_raiz()
    nova_pasta = criar_pasta(nome, pasta_raiz, opcao)
    log_path, log_visivel, encontrados = registrar_log_e_copiar(nome, pasta_raiz, nova_pasta, opcao)

    print("\n✅ Operação concluída.")
    print(f"🔍 Total de arquivos encontrados: {encontrados}")
    print(f"📄 Log oculto salvo em: {log_path}")
    if log_visivel:
        print(f"📄 Log visível salvo em: {log_visivel}")
    if nova_pasta:
        print(f"📁 Pasta de destino: {nova_pasta}")

    input("\nPressione ENTER para sair...")


if __name__ == "__main__":
    main()
