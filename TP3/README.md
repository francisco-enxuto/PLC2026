# TPC3: Analizador Léxico
## Francisco Ribeiro Enxuto dos Santos
## A112319

<img width=400 src="https://github.com/francisco-enxuto/PLC2026/blob/main/img/IMG_20260922_204007.jpg" alt="Foto minha">

## Resumo

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

``` linguagem_estranha
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

Tokens e outros:
* O caráter '#' marca o início de um comentário que se prolonga até ao fim da linha e deve ser ignorado;
* O caráter '?' marca o início de um identificador de uma variável que se prolonga até ao primeiro caráter não alfanumérico;
* O caráter '@' marca o início de um identificador de língua que terá mais 2 carateres;
* Qualquer sequência entre aspas é um valor do tipo string;
* As outras sequências de alfanuméricos são identificadores de conceitos;
* Os carateres '{}.' são delimitadores; 'LIMIT' é uma palavra reservada;
* '1000' é um valor numérico.

## Uso

O analisador léxico lê  do  **stdin** e escreve o resultado no **stdout**
```bash
python analex.py < input.txt
```

## Resultados
Exemplo de entrada input.txt:

```txt
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
```

Output:

```bash
('PR', 'select', 1, (0, 6))
('IDV', '?nome', 1, (7, 12))
('IDV', '?desc', 1, (13, 18))
('PR', 'where', 1, (19, 24))
('D', '{', 1, (25, 26))
('IDV', '?s', 2, (1, 3))
('IDC', 'a', 2, (4, 5))
('IDC', 'dbo', 2, (6, 9))
('IDC', 'MusicalArtist', 2, (10, 23))
('D', '.', 2, (23, 24))
('IDV', '?s', 3, (1, 3))
('IDC', 'foaf', 3, (4, 8))
('IDC', 'name', 3, (9, 13))
('STR', '"Chuck Berry"', 3, (14, 27))
('IDL', '@en', 3, (27, 30))
('D', '.', 3, (31, 32))
('IDV', '?w', 4, (1, 3))
('IDC', 'dbo', 4, (4, 7))
('IDC', 'artist', 4, (8, 14))
('IDV', '?s', 4, (15, 17))
('D', '.', 4, (17, 18))
('IDV', '?w', 5, (1, 3))
('IDC', 'foaf', 5, (4, 8))
('IDC', 'name', 5, (9, 13))
('IDV', '?nome', 5, (14, 19))
('D', '.', 5, (19, 20))
('IDV', '?w', 6, (1, 3))
('IDC', 'dbo', 6, (4, 7))
('IDC', 'abstract', 6, (8, 16))
('IDV', '?desc', 6, (17, 22))
('D', '}', 7, (0, 1))
('PR', 'LIMIT', 7, (2, 7))
('N', '1000', 7, (8, 12))
```

PR - Palavra Reservada
C - Comentário
IDV - Identificador de variável
IDL - Identificador de língua
STR - String
N - Valor numérico
IDC - Identificador de conceito
D - Delimitador
SKIP - Espaço ou tab

### Ficheiros

- [Analisador léxico (`analex.py`)](https://github.com/francisco-enxuto/PLC2026/blob/main/TP3/analex.py)
- [Ficheiro de entrada (`input.txt`)](https://github.com/francisco-enxuto/PLC2026/blob/main/TP3/input.txt)
- [Ficheiro de saída (`output.txt`)](https://github.com/francisco-enxuto/PLC2026/blob/main/TP3/output.txt)