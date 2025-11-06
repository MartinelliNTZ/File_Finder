# 🧾 Manual de Uso — Script Localizador e Copiador de Arquivos
**Criado por:** M. Martinelli  
**Versão:** 1.4 (log detalhado, ignore case e proteção de pastas)  
**Identificador:** lca25v14  
**Data de criação:** 31/10/2025  
**Última alteração:** 31/10/2025  

---

## 📘 Objetivo do Script
O script **Localizador e Copiador de Arquivos** tem como objetivo **localizar arquivos** em uma pasta e suas subpastas, **cujos nomes contenham um termo informado pelo usuário**, de forma **não sensível a maiúsculas/minúsculas (ignore case)**.  

Ele pode **gerar logs detalhados** e, opcionalmente, **copiar automaticamente os arquivos encontrados** para uma nova pasta organizada.

---

## ⚙️ Funcionalidades Principais

### 🔍 Busca Inteligente
- Pesquisa **recursiva** em todas as subpastas do diretório onde o script está localizado.  
- **Ignora diferenças entre maiúsculas e minúsculas**.  
- **Ignora automaticamente:**
  - A pasta de log (`log`);
  - A pasta de destino de cópias;
  - O próprio script.

### 📑 Log Detalhado
- Cada execução gera um log oculto dentro da pasta `log`, com:
  - Nome completo do arquivo encontrado;
  - Caminho original;
  - Data e hora da última modificação;
  - Contagem total de arquivos localizados.
- Quando o usuário escolhe gerar apenas o log, uma cópia visível (`log.txt`) é criada na raiz do script.

### 📂 Cópia Automática
- Cria automaticamente uma nova pasta com o **termo buscado**.
- Copia todos os arquivos encontrados para essa pasta.
- Se já existir arquivo com o mesmo nome, o script cria versões numeradas (`_1`, `_2`, ...).

---

## 🧭 Opções de Execução

Durante a execução, o usuário pode escolher:

| Tecla / Opção | Ação |
|---------------|------|
| **[ENTER]** | Copiar arquivos e gerar log |
| **[1]** | Gerar apenas o log (sem copiar) |
| **[ESC]** | Cancelar a execução |

---

## 📂 Estrutura de Saída

| Tipo de Saída | Descrição |
|----------------|------------|
| **📁 Pasta de destino** | Criada automaticamente com o nome pesquisado (apenas se houver cópia). |
| **📁 Pasta de log (oculta)** | Criada automaticamente com logs datados. |
| **📄 Log visível (log.txt)** | Criado apenas quando a opção escolhida for `1`. |

## 📦 Pasta_do_Script
┣ 📁 log (oculta)
┃ ┣ lca25v14_LOG_20251031_142500.txt
┣ 📁 Fazenda
┃ ┣ mapa001.pdf
┃ ┗ imagem1.png
┗ 📄 script_localizador.py


---

## 🧩 Passo a Passo do Funcionamento Interno

1. **Exibe menu interativo** com as três opções principais.  
2. **Solicita o termo de busca** e inicia o processo.  
3. **Determina a pasta raiz** (onde o script está salvo).  
4. **Cria pasta de destino** (somente se houver cópia).  
5. **Cria pasta oculta de log** (`/log`) e define nome do log com data e hora.  
6. **Percorre todas as pastas** ignorando as protegidas (`log`, destino, próprio script).  
7. **Verifica se o nome do arquivo contém o termo informado** (ignore case).  
8. Para cada arquivo encontrado:
   - Registra no log suas informações detalhadas;
   - Copia o arquivo, se for o modo com cópia.
9. **Cria log visível** (`log.txt`) se a opção for apenas log.  
10. Exibe resumo final com total de arquivos, caminhos e status.

---

## 📊 Exemplo de Saída no Console

----LOCALIZADOR DE ARQUIVOS-----
Digite o nome (ou parte do nome) do arquivo a ser localizado: Fazenda

Pressione ENTER para copiar os arquivos e criar um log
Digite 1 para apenas criar o log (sem copiar)
Ou pressione ESC para cancelar

Escolha: ENTER

✅ Operação concluída.
🔍 Total de arquivos encontrados: 5
📄 Log oculto salvo em: C:\Projetos\log\lca25v14_LOG_20251031_142500.txt
📁 Pasta de destino: C:\Projetos\Fazenda


---

## 🧾 Saídas e Compatibilidade

| Item | Detalhe |
|------|----------|
| **Log oculto:** | Pasta `log`, arquivo datado e oculto |
| **Log visível:** | `log.txt` criado apenas se opção = 1 |
| **Pasta de destino:** | Criada automaticamente se houver cópia |
| **Compatibilidade:** | Windows 10 / 11 |
| **Requisitos:** | Python 3.8+ |

---

## 💡 Boas Práticas

- Execute sempre em uma pasta local (não em rede).  
- Evite nomes de busca muito genéricos (como “.jpg” ou “temp”).  
- Faça backups da pasta de destino se pretender rodar várias vezes.  
- Se quiser apenas saber **onde estão os arquivos**, use a opção `[1]` (gera apenas log).  
- O script é seguro: **não apaga nem altera arquivos originais**.

---

## ⚙️ Estrutura Técnica e Módulos Utilizados

| Módulo | Função |
|---------|--------|
| `os`, `shutil` | Navegação de diretórios e cópia de arquivos |
| `msvcrt` | Captura de teclas no console (ENTER, ESC, etc.) |
| `ctypes` | Define atributos de pasta oculta no Windows |
| `time`, `datetime` | Geração de logs datados |

---

## 📜 Log — Exemplo de Registro
========== LOCALIZADOR DE ARQUIVOS ==========
Termo buscado (ignore case): Fazenda
Data e hora da busca: 31/10/2025 14:25:00
Pasta base: C:\Projetos

[1] Arquivo encontrado:
• Nome: Fazenda_A_Mapa.pdf
• Pasta: C:\Projetos\Mapas
• Caminho completo: C:\Projetos\Mapas\Fazenda_A_Mapa.pdf
• Modificado em: 29/10/2025 10:40:12
[2] Arquivo encontrado:
• Nome: Fazenda_B_Imagem.png
• Pasta: C:\Projetos\Imagens
• Caminho completo: C:\Projetos\Imagens\Fazenda_B_Imagem.png
• Modificado em: 30/10/2025 09:15:40

Total de arquivos encontrados: 2
========== FIM DO LOG ==========

---

## 🧠 Resumo Técnico do Fluxo
1. Usuário informa termo → Script identifica a pasta raiz.  
2. Pasta `log` é criada e ocultada.  
3. Busca recursiva é realizada ignorando diretórios protegidos.  
4. Cada arquivo que contém o termo é logado e copiado (se aplicável).  
5. Logs são finalizados e exibidos no console.  

---

## 🪶 Licença
Este script pode ser **usado, adaptado e distribuído livremente**, desde que mantida a autoria original.  
Recomenda-se documentar modificações (data, autor, versão) para controle e rastreabilidade.

---








Exemplo de estrutura gerada:

