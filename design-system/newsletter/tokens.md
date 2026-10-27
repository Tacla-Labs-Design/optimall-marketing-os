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
| Texto/link de marca **sobre claro** | `#9025F4` (`accent-ink`) | 5,59:1 sobre branco, 5,21:1 sobre a página e 4,74:1 sobre a tag `#F3E8FF`, que é o piso real |
| Texto/link de marca no **dark mode** | `#D5BFFF` (`accent-on-dark`) | 10,55:1 sobre `#1A1A1A` |

O `#9934FF` entra como **fundo** — botão, tag, régua de destaque. Como texto, use sempre o
`#9025F4`: o roxo de marca passa sobre branco, mas fica a 4,56:1 sobre a página `#FAF5FF`.

Os **ícones sociais do rodapé** são roxos (`brand/assets/icones/<rede>-marca.png`), só
Instagram e LinkedIn — as redes oficiais. Sobre a página clara o roxo dá 4,56:1; sobre o
dark `#1A1A1A`, 3,56:1. O ícone é alvo de toque, não de leitura: quem sustenta o link é o
`alt` com o nome da rede e a área de toque.

## Fundos

| Token | Hex | Uso |
|---|---|---|
| `page` | `#FAF5FF` | Fundo da mensagem, fora do container |
| `canvas` | `#FAF5FF` | Fundo do container 600px — mesma cor da página |
| `surface` | `#FFFFFF` | Fundo dos cards de seção e da placa do header |
| `surface-alt` | `#F9F8FC` | Fundo alternativo dentro de card |
| `accent-soft` | `#F3E8FF` | Fundo de tag/eyebrow e de card de destaque |
| `hairline` | `#E3DDF1` | Divisores |

`page` e `canvas` são a mesma cor de propósito: o container não se destaca do fundo,
e quem constrói a estrutura visual são os **cards brancos**.

## Texto

| Token | Hex | Uso | Contraste sobre `page` |
|---|---|---|---|
| `ink` | `#18181B` | Títulos e texto forte | 16,51:1 |
| `body` | `#353E4F` | Texto corrido | 10,02:1 |
| `muted` | `#525A6F` | Legal, legendas, rodapé | 6,41:1 |

## Dark mode

| Token | Hex |
|---|---|
| `page-dark` / `canvas-dark` | `#1A1A1A` |
| `surface-dark` | `#242424` |
| `accent-soft-dark` | `#262030` |
| `header-card-dark` | `#FFFFFF` — a placa do header **não** escurece: o logo é o positivo, tricolor |
| `accent-dark` | `#D5BFFF` |
| `ink-dark` | `#F5F5F5` |
| `body-dark` | `#C9C9C9` |
| `muted-dark` | `#8F8F8F` |
| `hairline-dark` | `#333333` |

O **CTA roxo não inverte** no dark — `#9934FF` faz 3,56:1 com `#1A1A1A`, o bastante para a
forma do botão, e o texto branco continua em cima dele. Só o CTA neutro escuro (`#18181B`)
usa `.dm-btn` para virar branco.

## Tipografia

Stack: `'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`

| Papel | Tamanho / line-height / peso |
|---|---|
| Hero headline | 30px / 38px / 600 |
| Section headline | 26px / 32px / 600 |
| Card title | 20px / 26px / 600 |
| Card title compacto | 17px / 23px / 600 |
| Body | 16px / 25px / 400 |
| Body small | 15px / 23px / 400 |
| Número de destaque | 32px / 38px / 600, letter-spacing -0.5px |
| Label de número | 14px / 20px / 400 |
| Eyebrow / tag | 12px / 16px / 600, letter-spacing 1px, uppercase |
| CTA | 15px / 15px / 600 |
| Legal | 12px / 18px / 400 |

O **label de número** (14px) é a única exceção ao piso de 15px do corpo de texto: ele é
legenda de um número grande, nunca texto corrido, e só aparece no `08-destaque-numeros`
variante A (3 colunas). Na variante B (1 coluna), o rótulo é frase e usa o Body 16/25.

## Espaçamento e formas

Escala: `8 · 12 · 16 · 20 · 24 · 32 · 40 · 48`
- Container padding lateral: 32px desktop / 20px mobile
- Padding interno de card: 24–32px desktop / 16–20px mobile
- Gap entre seções: 32px · entre cards de uma mesma lista: 16px
- Raio: card 20px · imagem 12–16px · miniatura 12px · botão 100px

## Tamanhos de imagem

| Bloco | Exibição | Exportar (2x) |
|---|---|---|
| Hero / imagem de seção | 536 × auto | 1072 × auto |
| Card de notícia (topo) | 536 × auto | 1072 × auto |
| Miniatura compacta (1:1) | 160 desktop / 88 mobile | 320 × 320 |
| Artigo alternado | 248 × 248 | 496 × 496 |
| Logo do Optimall (`01`, `90`) | 143 × 24 | 286 × 48 |
| Galeria dentro do card (`13a`, 1:1) | 224 × 224 | 448 × 448 |
| Ícone social | 24 × 24 | 48 × 48 |
