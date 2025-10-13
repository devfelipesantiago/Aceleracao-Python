#!/bin/bash

### GIT FILTER-REPO ###

## NÃO EXECUTE ESSE SCRIPT DIRETAMENTE
## Esse script foi feito para uso do
## script 'trybe-publisher' fornecido 
## pela Trybe. 

[[ $# == 1 ]] && \
[[ $1 == "trybe-security-parameter" ]] && \
git filter-repo \
    --path .trybe \
    --path .github \
    --path .vscode \
    --path trybe.yml \
    --path trybe-filter-repo.sh \
    --path tests/test_estoque.py \
    --path tests/test_produto.py \
    --path tests/__init__.py \
    --path tests/livro/__init__.py \
    --path tests/livro/mocks.py \
    --path tests/livro/conftest.py \
    --path tests/__init__.py \
    --path tests/descricao_livro/__init__.py \
    --path tests/descricao_livro/mocks.py \
    --path tests/descricao_livro/conftest.py \
    --path README.md \
    --invert-paths --force --quiet
