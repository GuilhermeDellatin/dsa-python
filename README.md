# dsa-python

Estudos de estruturas de dados e algoritmos em Python 3.13.

## Estrutura

```
src/dsa_python/    # implementações reutilizáveis ("biblioteca")
  sorting/
  data_structures/
  graphs/
exercises/         # soluções de exercícios
  clrs/chapter_XX/
  leetcode/pNNNN_nome.py
tests/             # espelha src/ e exercises/
```

## Uso

```bash
uv sync                    # instala dependências
uv run pytest              # roda os testes
uv run ruff check .        # lint
uv run ruff format .       # formatação
```
