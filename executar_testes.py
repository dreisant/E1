import os
import glob
import subprocess
import sys

def main():
    pasta_base = os.path.dirname(os.path.abspath(__file__))
    pasta_testes = os.path.join(pasta_base, "tests")
    arquivos_in = sorted(glob.glob(os.path.join(pasta_testes, "*.in")))
    
    if not arquivos_in:
        print("Nenhum arquivo de teste (.in) encontrado.")
        return

    candidatos_executavel = [
        os.path.join(pasta_base, "e1"),
        os.path.join(pasta_base, "e1.exe"),
    ]
    
    executavel = None
    for cand in candidatos_executavel:
        if os.path.isfile(cand):
            executavel = cand
            break

    if not executavel:
        res = subprocess.run(["make", "compile"], cwd=pasta_base, shell=True)
        for cand in candidatos_executavel:
            if os.path.isfile(cand):
                executavel = cand
                break

    if not executavel:
        print("Erro: executavel 'e1' nao encontrado.")
        sys.exit(1)

    print("=" * 50)
    print(" Executando Bateria de Testes do E1")
    print("=" * 50)

    total = len(arquivos_in)
    passou = 0

    for arq_in in arquivos_in:
        nome_base = os.path.splitext(arq_in)[0]
        arq_ora = nome_base + ".ora"
        nome_teste = os.path.basename(arq_in)

        if not os.path.exists(arq_ora):
            print(f"[AVISO] {nome_teste}: arquivo de gabarito (.ora) nao encontrado!")
            continue

        with open(arq_in, "r", encoding="utf-8") as f:
            entrada = f.read()

        with open(arq_ora, "r", encoding="utf-8") as f:
            esperado = f.read().strip().replace("\r\n", "\n")

        processo = subprocess.run(
            [executavel],
            input=entrada,
            text=True,
            capture_output=True,
            cwd=pasta_base
        )

        obtido = processo.stdout.strip().replace("\r\n", "\n")

        if obtido == esperado:
            print(f"[OK] PASSOU: {nome_teste}")
            passou += 1
        else:
            print(f"[FALHA] {nome_teste}")
            print("--- Esperado ---")
            print(esperado)
            print("--- Obtido ---")
            print(obtido)
            if processo.stderr:
                print("--- Erro de Execucao (stderr) ---")
                print(processo.stderr)
            print("-" * 30)

    print("=" * 50)
    print(f"Resultado final: {passou}/{total} testes passaram.")
    print("=" * 50)

    if passou < total:
        sys.exit(1)

if __name__ == "__main__":
    main()
