# Exercício 1 - Parte 2 (Flex e C)

**Equipe:**

**Membros:**
- Davi Carvalho, @dcxrvalho
- Davi Reis, @dreisant

---

## Descrição dos Arquivos

- `makefile`: Regras `compile` e `test`.
- `token.h`: Definição do enum dos tokens.
- `scanner.l`: Especificação léxica para o Flex.
- `main.c`: Função principal que chama `yylex()` e imprime os tokens.
- `executar_testes.py`: Script para executar os testes da pasta `tests/` contra os gabaritos (`.ora`).
- `tests/`: Casos de teste (`.in` e `.ora`).

---

## Como Compilar e Executar

### Via Makefile:
```bash
make compile
make test
```

### Execução manual:
```bash
./e1 < tests/cenario1.in
```

### Limpeza:
```bash
make clean
```
