import re
import sys


def md_to_xml(texto):
    xml = texto

    # Cabeçalhos
    cabecalhos = [
        r"^#\s+(.+)$",
        r"^##\s+(.+)$",
        r"^###\s+(.+)$",
        r"^####\s+(.+)$",
        r"^#####\s+(.+)$",
        r"^######\s+(.+)$"
    ]

    i = 1
    for r in cabecalhos:
        xml = (re.sub(r, f"<h{i}>\\1</h{i}>", xml, flags = re.M))
        i += 1

    # Bold
    xml = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", xml)

    # Itálico
    xml = re.sub(r"\*(.+?)\*", r"<i>\1</i>", xml)

    # Lista numerada
    xml = re.sub(r"^\d+\.\s+(.+)$", r"<li>\1</li>", xml, flags = re.M)
    xml = re.sub(r"^(<li>.+</li>(?:\n<li>.+</li>)*)", r"<ol>\n\1\n</ol>", xml, flags = re.M)

    # Imagem
    xml = re.sub(r"!\[(.+?)\]\((.+?)\)", "<img src=\"\\2\" alt=\"\\1\"/>", xml)

    # Link
    xml = re.sub(r"\[(.+?)\]\((.+?)\)", "<a href=\"\\2\">\\1</a>", xml)


    return xml
            
def main():
    xml = sys.stdin.read()
    print(md_to_xml(xml))

if __name__ == "__main__":
    main()


