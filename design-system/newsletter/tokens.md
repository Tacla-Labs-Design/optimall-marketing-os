# Tokens — newsletter

> Os valores do e-mail do Optimall. A fonte de máquina é `cores` em
> [`brand/marca.json`](../../brand/marca.json); os componentes estão escritos com estes hex.
> Mudar um valor é mudar o `marca.json`, os componentes e este arquivo na mesma leva
> (`CHANGELOG.md`).

## Cor de marca

**`#9934FF`** (roxo Optimall).

Contraste sobre branco: **4,90:1** — passa para texto, por pouco. Isso governa três regras:

| Situação | Cor certa | Por quê |
|---|---|---|
| Texto **em cima** do roxo | `#FFFFFF` | 4,90:1. Texto escuro sobre o roxo é **proibido** |
| Texto/link de marca **sobre claro** | `#9025F4` (`accent-ink`) | 5,59:1 sobre branco (a página e o botão branco da faixa de CTA), 5,21:1 sobre a faixa do rodapé e 4,74:1 sobre a tag `#F3E8FF`, que é o piso real |
| Texto/link de marca no **dark mode** | `#D5BFFF` (`accent-on-dark`) | 10,55:1 sobre `#1A1A1A` |

O `#9934FF` entra como **fundo** — botão, tag, régua de destaque. Como texto, use sempre o
`#9025F4`: o roxo de marca passa sobre branco, mas fica a 4,56:1 sobre a faixa do rodapé `#FAF5FF`.

Os **ícones sociais do rodapé** são roxos (`brand/assets/icones/<rede>-marca.png`), só
Instagram e LinkedIn — as redes oficiais. Sobre a faixa lavanda do rodapé o roxo dá 4,56:1; sobre o
dark `#1A1A1A`, 3,56:1. O ícone é alvo de toque, não de leitura: quem sustenta o link é o
`alt` com o nome da rede e a área de toque.

## Fundos

| Token | Hex | Uso |
|---|---|---|
| `page` | `#FFFFFF` | Fundo da mensagem, fora do container |
| `canvas` | `#FFFFFF` | Fundo do container 600px — mesma cor da página |
| `surface` | `#FFFFFF` | Fundo do `13-card-conteudo` (com borda `hairline`) |
| `surface-alt` | `#F9F8FC` | Painel de imagem com print de tela (`11` variante B) |
| `accent-soft` | `#F3E8FF` | Painel de imagem (`11` A e C), tag/eyebrow, cards `05`, `06`, `08` B |
| `page-light` | `#FAF5FF` | Faixa do rodapé (`90` + `91`) |
| `hairline` | `#E3DDF1` | Divisores, borda da imagem de abertura e do `13` |

`page` e `canvas` são a mesma cor de propósito: o container não se destaca do fundo.
A peça é **página branca**, com o conteúdo solto nela; quem dá estrutura são o mesh do topo,
os títulos de seção grandes, os **painéis** de imagem e as linhas finas. As únicas faixas de
borda a borda são a do CTA (mesh roxo) e a do rodapé (lavanda).

## Gradient mesh

O fundo do topo (`01-header`) e da faixa de CTA (`89-faixa-cta-mesh`). É um degradê de vários
pontos radiais sobrepostos, **só com cores da paleta** (`brand/marca.json` → `cores` e
`paleta_extra`). A fonte é `scripts/gerar-mesh.py`; as imagens geradas ficam em
`brand/assets/grafismos/`.

| Mesh | Fundo | Pontos (posição → cor, alcance) | Texto por cima | Imagem do e-mail |
|---|---|---|---|---|
| `mesh-claro` | `#F3E8FF` | 0% 0% → `#FAF5FF` 40% · 20% 35% → `#E9D5FF` 45% · 70% 0% → `#D8B4FE` 50% · 100% 30% → `#BC7AFF` 45% · 100% 75% → `#AD5CFF` 45% · 45% 80% → `#E9D5FF` 45% · 100% 95% → `#9934FF` 55% | Tinta `#18181B` / corpo `#353E4F` | `mesh-email-topo.png`, 600 × 400, some de 42% a 100% da altura |
| `mesh-roxo` | `#9934FF` | 0% 0% → `#821FE5` 55% · 0% 100% → `#7500EB` 50% · 45% 100% → `#9934FF` 50% · 100% 0% → `#AD5CFF` 45% · 100% 100% → `#BC7AFF` 45% | Sempre branco `#FFFFFF` | `mesh-email-cta.png`, 600 × 240, opaca |

Cada ponto é um `radial-gradient(at X Y, <cor> 0px, transparent <alcance>)`; o primeiro da lista
fica por cima. `python3 scripts/gerar-mesh.py css` imprime as duas receitas prontas em CSS.

Regras:
- **No mesh claro, os tons fortes ficam à direita e embaixo**, atrás da imagem de abertura —
  nunca atrás do título. Texto escuro sobre o roxo continua proibido.
- **No mesh roxo, os lilases ficam nos cantos da direita**, longe do texto, que é branco e
  alinhado à esquerda. Medido na imagem: o título (26px, texto grande) fica a 4,3:1 no pior
  ponto e a frase de 15px a 4,5:1 até 450px de largura — por isso a frase é uma linha só.
- **No e-mail, o mesh é imagem PNG**, nunca CSS: Gmail e Outlook ignoram `radial-gradient`.
  Entra como `background-image` do `<td>`, com `bgcolor` sólido por baixo e o par
  `v:rect`/`v:fill` para o Outlook Windows — já montado nos componentes.
- O mesh do topo some para transparente: o degradê termina no fundo da página nos dois modos
  (branco no claro, `#1A1A1A` no escuro). Por isso o topo precisa ter mais de 400px de altura,
  o que todo topo com título e imagem de abertura tem.
- Mudar uma cor ou um ponto é mudar `MESH` no `scripts/gerar-mesh.py`, esta tabela e as
  imagens na mesma leva (`CHANGELOG.md`). Não se cria terceiro mesh por campanha.

## Texto

| Token | Hex | Uso | Contraste sobre `page` |
|---|---|---|---|
| `ink` | `#18181B` | Títulos e texto forte | 17,72:1 (8,6:1 no pior ponto do mesh, atrás do título) |
| `body` | `#353E4F` | Texto corrido | 10,75:1 (8,1:1 sobre o mesh, na linha de data) |
| `muted` | `#525A6F` | Legal, legendas, rodapé | 6,88:1 (6,41:1 sobre a faixa lavanda do rodapé) |

## Dark mode

| Token | Hex |
|---|---|
| `page-dark` / `canvas-dark` | `#1A1A1A` |
| `surface-dark` | `#242424` |
| `accent-soft-dark` | `#262030` |
| topo e faixa de CTA | **Não** escurecem: o mesh é imagem, e o texto sobre ele fica escuro no topo e branco na faixa |
| `accent-dark` | `#D5BFFF` |
| `ink-dark` | `#F5F5F5` |
| `body-dark` | `#C9C9C9` |
| `muted-dark` | `#8F8F8F` |
| `hairline-dark` | `#333333` |

O fundo da página no topo vira `#1A1A1A` e o mesh claro some nele: no escuro, o topo é um
brilho lavanda sobre o fundo escuro. O texto do topo continua tinta, de propósito — o mesh atrás
dele é claro nos dois modos.

O **CTA roxo não inverte** no dark — `#9934FF` faz 3,56:1 com `#1A1A1A`, o bastante para a
forma do botão, e o texto branco continua em cima dele. Só o CTA neutro escuro (`#18181B`)
usa `.dm-btn` para virar branco.

## Tipografia

Stack: `'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`

| Papel | Tamanho / line-height / peso |
|---|---|
| Título da edição (`01`) | 46px / 50px / 600, letter-spacing -1.2px · mobile 36 / 40 |
| Título de seção (`02b`) | 30px / 36px / 600, letter-spacing -0.6px · mobile 23 / 29 |
| Headline de abertura (`02`), título da faixa (`89`), card (`05`) | 26px / 32px / 600 · mobile 23 / 29 |
| Card title | 20px / 26px / 600 |
| Card title compacto | 17px / 23px / 600 |
| Body | 16px / 25px / 400 |
| Body small | 15px / 23px / 400 |
| Número de destaque | 32px / 38px / 600 (`08` B) · 28px / 34px / 600 (`08` A), letter-spacing -0.5px |
| Eyebrow / tag | 12px / 16px / 600, letter-spacing 1px, uppercase |
| CTA | 15px / 15px / 600 |
| Legal | 12px / 18px / 400 |

Tudo alinhado à **esquerda**. A exceção é o `06-card-oferta`,
centralizado por ser vitrine. Nenhum texto abaixo de 15px, fora o legal e a tag (12px).

## Espaçamento e formas

Escala: `8 · 12 · 16 · 20 · 24 · 32 · 40 · 48`
- Container padding lateral: 32px desktop / 20px mobile
- Padding interno de card e painel: 32px desktop / 16–20px mobile
- Topo → headline: 36px · entre seções: linha fina com 40px em cima e embaixo · entre itens
  de uma seção: 40px · imagem do painel → título: 20px · último bloco → faixa de CTA: 40px
- Raio: card e painel 20px · imagem 12–16px · miniatura 12px · botão 100px · faixas: sem raio

## Tamanhos de imagem

| Bloco | Exibição | Exportar (2x) |
|---|---|---|
| Imagem de abertura (`01`) / imagem solta (`03`) | 536 × auto | 1072 × auto |
| Imagem no painel (`11`), 16:9 | 472 × auto | 944 × auto |
| Imagem no painel (`11`), 1:1 | 400 × 400 (recorte: 380) | 800 × 800 |
| Mesh do topo / da faixa | 600 × 400 / 600 × 240 | 1x — degradê não perde nitidez |
| Miniatura compacta (1:1) | 160 desktop / 88 mobile | 320 × 320 |
| Artigo alternado | 248 × 248 | 496 × 496 |
| Logo do Optimall (`01`, `90`) | 143 × 24 | 286 × 48 |
| Galeria dentro do card (`13a`, 1:1) | 224 × 224 | 448 × 448 |
| Ícone social | 24 × 24 | 48 × 48 |
