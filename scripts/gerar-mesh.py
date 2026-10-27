#!/usr/bin/env python3
"""Gera as imagens de gradient mesh do e-mail a partir das receitas oficiais.

Usa o Google Chrome da máquina em modo sem janela — nada para instalar. Só o maintainer roda:
as imagens geradas são assets oficiais, em brand/assets/grafismos/.

Uso:
  python3 scripts/gerar-mesh.py            grava mesh-email-topo.png e mesh-email-cta.png
  python3 scripts/gerar-mesh.py css        só imprime as receitas em CSS (deck, post, web)

As receitas estão em design-system/newsletter/tokens.md (§ Gradient mesh). Mudar uma cor ou um
ponto é mudar MESH aqui, o tokens.md e as imagens na mesma leva (CHANGELOG).

Por que imagem e não CSS no e-mail: Gmail e Outlook ignoram radial-gradient. O topo sai com
transparência que some para baixo, para o degradê terminar no fundo da página nos dois modos.

Saída 0 = ok. Saída 1 = o Chrome não gerou a imagem.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "brand", "assets", "grafismos")

CHROME_CANDIDATOS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]

# Receita: fundo + pontos (x %, y %, cor, alcance %). Só cores de brand/marca.json.
MESH = {
    # Topo do e-mail. Texto em tinta #18181B por cima: os tons fortes ficam à direita e
    # embaixo, atrás da imagem de abertura, nunca atrás do título.
    "claro": ("#F3E8FF", [
        (0, 0, "#FAF5FF", 40),
        (20, 35, "#E9D5FF", 45),
        (70, 0, "#D8B4FE", 50),
        (100, 30, "#BC7AFF", 45),
        (100, 75, "#AD5CFF", 45),
        (45, 80, "#E9D5FF", 45),
        (100, 95, "#9934FF", 55),
    ]),
    # Faixa de CTA. Texto sempre branco por cima: os lilases ficam no canto oposto ao texto.
    "roxo": ("#9934FF", [
        (0, 0, "#821FE5", 55),
        (0, 100, "#7500EB", 50),
        (45, 100, "#9934FF", 50),
        (100, 0, "#AD5CFF", 45),
        (100, 100, "#BC7AFF", 45),
    ]),
}

# (arquivo, receita, largura, altura, some a partir de % da altura ou None)
IMAGENS = [
    ("mesh-email-topo.png", "claro", 600, 400, 42),
    ("mesh-email-cta.png", "roxo", 600, 240, None),
]


def css(nome):
    fundo, pontos = MESH[nome]
    camadas = ",\n    ".join(f"radial-gradient(at {x}% {y}%, {c} 0px, transparent {a}%)"
                             for x, y, c, a in pontos)
    return f"background-color:{fundo};\n  background-image:\n    {camadas};"


def mascara(inicio):
    # Opaco até `inicio`, depois some numa curva suave (mais rápida no começo) até 100%.
    passos = [(0, 1), (0.25, 0.63), (0.5, 0.33), (0.75, 0.11), (1, 0)]
    paradas = ", ".join(f"rgba(0,0,0,{a}) {inicio + (100 - inicio) * t:.1f}%" for t, a in passos)
    return f"-webkit-mask-image:linear-gradient(to bottom, {paradas});"


def chrome():
    for c in CHROME_CANDIDATOS:
        if c and os.path.exists(c):
            return c
    raise SystemExit("✗ Não encontrei o Google Chrome nesta máquina. Ele é necessário para gerar o mesh.")


def gerar(arquivo, nome, w, h, some):
    estilo = css(nome).replace("\n", "") + (mascara(some) if some else "")
    html = (f"<html><body style='margin:0;background:transparent'>"
            f"<div style='width:{w}px;height:{h}px;{estilo}'></div></body></html>")
    saida = os.path.join(DESTINO, arquivo)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    try:
        subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--no-first-run", "--no-default-browser-check",
                        "--default-background-color=00000000", f"--window-size={w},{h}",
                        "--force-device-scale-factor=1", f"--screenshot={saida}",
                        "file://" + f.name], capture_output=True, timeout=60)
    finally:
        os.unlink(f.name)
    if not os.path.exists(saida):
        print(f"  ✗ {arquivo}: o Chrome não gerou a imagem")
        return False
    print(f"  ✓ {os.path.relpath(saida, RAIZ)} — {w}×{h}, {os.path.getsize(saida) // 1024} KB")
    return True


def main(argv):
    if argv[1:] == ["css"]:
        for nome in MESH:
            print(f".mesh-{nome} {{\n  {css(nome)}\n}}\n")
        return 0
    if argv[1:]:
        print(__doc__)
        return 2
    ok = all([gerar(*img) for img in IMAGENS])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
