
import sys
import re

def tokenize(input_string, id_linha):
    reconhecidos = []
    linha = id_linha
    mo = re.finditer(r'(?P<PR>[sS][eE][lL][eE][cC][tT]|[lL][iI][mM][iI][tT]|[wW][hH][eE][rR][eE])|(?P<C>#.*)|(?P<IDV>\?\w+)|(?P<IDL>@[a-zA-Z]{2})|(?P<STR>".*?")|(?P<N>\d+)|(?P<IDC>(?<= |:)(\w+))|(?P<D>\{|\}|\.)|(?P<SKIP>[ \t])', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['PR']:
            t = ("PR", dic['PR'], linha, m.span())

        elif dic['C']:
            t = ("C", dic['C'], linha, m.span())
    
        elif dic['IDV']:
            t = ("IDV", dic['IDV'], linha, m.span())
    
        elif dic['IDL']:
            t = ("IDL", dic['IDL'], linha, m.span())
    
        elif dic['STR']:
            t = ("STR", dic['STR'], linha, m.span())
    
        elif dic['N']:
            t = ("N", dic['N'], linha, m.span())
    
        elif dic['IDC']:
            t = ("IDC", dic['IDC'], linha, m.span())
    
        elif dic['D']:
            t = ("D", dic['D'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and not dic['C']and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for id_linha, linha in enumerate(sys.stdin):
    for tok in tokenize(linha, id_linha):
        print(tok)    

