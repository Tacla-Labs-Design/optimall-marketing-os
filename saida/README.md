# saida/ — o que você montou

É aqui que o Claude grava o material pronto:

| O que | Onde |
|---|---|
| E-mail montado (`/newsletter-optimall`) | `saida/<slug>/index.html` |
| Apresentação montada (`/apresentacao-optimall`) | `saida/<slug>/index.html` + `assets/` + `<slug>.pdf` |
| Post ou carrossel (`/post-optimall`) | `saida/<slug>/index.html` + `png/` + `legenda.txt` |
| Prompt de foto de marca (`/foto-optimall`) | `saida/fotos/NNN-slug.md` |

**O que você monta fica só no seu computador.** Nada daqui é enviado para lugar nenhum
automaticamente — não tem risco de sobrescrever o trabalho de outra pessoa nem de mexer
no padrão sem querer.

## O que fazer com o arquivo pronto

*(e-mail)*

1. Conferir no navegador (ver "Como usar" no [README](../README.md) da raiz).
2. Testar o disparo pela ferramenta de envio ou por Litmus / Email on Acid.
3. Subir as imagens no servidor e trocar os caminhos relativos pelas URLs finais.

*(apresentação)*

1. O PDF já sai ao lado do `index.html`, um slide por página.
2. Para mandar para alguém, mandar o PDF — ou a **pasta inteira** (o HTML sozinho perde as
   imagens).

*(post)*

1. Os PNGs saem em `png/`, na ordem do carrossel, prontos para subir.
2. A legenda de Instagram e LinkedIn, com o ALT de cada card, está em `legenda.txt`.

## Diferença para `examples/`

| Pasta | O que é |
|---|---|
| `saida/` | Seu trabalho — fica no seu computador |
| `examples/` | Acervo de referência do time, cuidado por quem mantém o padrão |

Os prompts de foto em `saida/fotos/` são o histórico do ensaio: guardando-os, dá para
repetir uma foto meses depois e reaproveitar a mesma seed.

Quando um material ficar bom o bastante para virar referência, mande para quem cuida do
padrão — a decisão de entrar em `examples/` é dele.
