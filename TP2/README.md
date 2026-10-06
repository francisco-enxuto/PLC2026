# TPC2: Conversor de MarkDown para HTML
## Francisco Ribeiro Enxuto dos Santos
## A112319
<img width=400 src="https://github.com/francisco-enxuto/PLC2026/blob/main/img/IMG_20260922_204007.jpg" alt="Foto minha">

## Resumo:

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

### Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`

Out: `<h1>Exemplo</h1>`

### Bold: pedaços de texto entre "**":

In: `Este é um **exemplo** ...`

Out: `Este é um <b>exemplo</b> ...`

### Itálico: pedaços de texto entre "*":

In: `Este é um *exemplo* ...`

Out: `Este é um <i>exemplo</i> ...`

### Lista numerada:

In:
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

Out:
```
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

### Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`

Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

## Uso

O conversor lê Markdown do **stdin** e escreve o resultado no **stdout**, tal como o `cat`.

### Ficheiro de entrada e ficheiro de saída

```bash
python conversor.py < input.md > output.xml
```

- `< input.md` envia o conteúdo de `input.md` para o stdin do programa.
- `> output.xml` guarda o stdout no ficheiro `output.xml`.

### Apenas ver o resultado no terminal

```bash
python conversor.py < input.md
```

### Através de um pipe

```bash
cat input.md | python conversor.py > output.xml
```

### Escrever o texto manualmente

```bash
python conversor.py
```

O programa fica à espera de texto no teclado. Depois de escrever, termina a entrada com `Ctrl+D` e o resultado é impresso no terminal.


## Resultados

### Exemplo de entrada (`input.md`)

```markdown
###### Título muito pequeno
##### Título pequeno
#### Título normal
### Título maior
## Título grande
# Título mais maior grande
*aaaa*
1. batatas
2. cebolas
3. feijões
4. arroz
aaaaaaaaaaaaa
# batatas
1. batatas
2. cebolas
3. feijões
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum gajo](https://github.com/francisco-enxuto/PLC2026/blob/main/img/IMG_20260922_204007.jpg)
lindo
**um** e **dois**
teste som teste teste
**um** e **dois**
```

### Exemplo de saída (`output.xml`)

```xml
<h6>Título muito pequeno</h6>
<h5>Título pequeno</h5>
<h4>Título normal</h4>
<h3>Título maior</h3>
<h2>Título grande</h2>
<h1>Título mais maior grande</h1>
<i>aaaa</i>
<ol>
<li>batatas</li>
<li>cebolas</li>
<li>feijões</li>
<li>arroz</li>
</ol>
aaaaaaaaaaaaa
<h1>batatas</h1>
<ol>
<li>batatas</li>
<li>cebolas</li>
<li>feijões</li>
</ol>
Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
Como se vê na imagem seguinte: <img src="https://github.com/francisco-enxuto/PLC2026/blob/main/img/IMG_20260922_204007.jpg" alt="imagem dum gajo"/>
lindo
<b>um</b> e <b>dois</b>
teste som teste teste
<b>um</b> e <b>dois</b>
```

### Ficheiros

- [Conversor (`conversor.py`)](https://github.com/francisco-enxuto/PLC2026/blob/main/TP2/conversor.py)
- [Ficheiro de entrada (`input.md`)](https://github.com/francisco-enxuto/PLC2026/blob/main/TP2/input.md)
- [Ficheiro de saída (`output.xml`)](https://github.com/francisco-enxuto/PLC2026/blob/main/TP2/output.xml)

