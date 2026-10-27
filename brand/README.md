# Brand — Optimall

Camada mais alta do Marketing OS do Optimall. **Nada abaixo pode contradizer esta pasta.**

Se um pedido conflita com o que está aqui, a IA sinaliza o conflito em vez de alterar
a identidade. Ver `docs/governanca.md`.

Fontes da identidade: o site publicado [optimall.com.br](https://www.optimall.com.br) e os
arquivos do Figma *Apresentação Comercial 2026* e *Social Media – Optimall*. Aprovado pelo
maintainer em 2026-09-30.

| Arquivo | O que tem |
|---|---|
| [`marca.json`](marca.json) | Fonte de máquina: cores, logo, links, textos, redes, contato, fonte — lida por `scripts/conferir.py` |
| [`mensagens.md`](mensagens.md) | **O que dizer**: público, posicionamento, módulos, números oficiais, voz, frases aprovadas |
| [`links-oficiais.md`](links-oficiais.md) | CTA, contato, rodapé legal, redes, textos fixos |
| [`photography/STYLE-LOCK-OPTIMALL.md`](photography/STYLE-LOCK-OPTIMALL.md) | Direção fotográfica |
| `assets/` | Logo, ícones, clientes, parceiros, grafismos — e, só no computador, telas e fotos (abaixo) |

---

## Marca

**Optimall** — a plataforma B2B que reúne Campanhas, Aplicativo, Clube de Benefícios e CRM
para shoppings, com a marca de cada shopping. **A peça do Optimall é 100% dele**:

- **não cita o Podi**, não usa o logo, a cor, as redes nem os links do Podi;
- **não leva a Tacla Labs**.

Vale para texto, `alt`, legenda, nome de arquivo e imagem. O `scripts/conferir.py` acusa
qualquer sobra.

**A marca é masculina.** Escreva sempre **o Optimall**, **do Optimall**, **no Optimall**,
**pelo Optimall**. Nunca "a Optimall" — nem quando a frase vem do site, que ainda usa o feminino.

## Público e tom

**B2B, sempre.** Fala com quem decide no shopping — superintendência, marketing, CRM, operação
— e com parceiros comerciais. **Não fala com o consumidor final.** Tom objetivo, seguro,
orientado a número, um CTA por bloco: *Fale com um consultor*. Tudo em
[`mensagens.md`](mensagens.md).

## Cor

| Papel | Hex | Uso |
|---|---|---|
| Roxo Optimall | `#9934FF` | A cor da marca. Fundo de capa, faixa, botão, chip de ícone, destaque |
| Texto sobre o roxo | `#FFFFFF` | **Sempre branco** sobre o roxo (4,9:1). Nunca preto, nunca cinza |
| Roxo de texto | `#9025F4` | O roxo quando ele é **texto** sobre fundo claro (link, número, palavra de destaque) |
| Lavanda | `#FAF5FF` · `#F3E8FF` · `#E9D5FF` | Fundos claros, cards, chips |
| Lilás | `#C084FC` · `#D8B4FE` | Só grafismo: pontos do pattern, linhas, brilho |
| Tinta | `#18181B` | Títulos sobre claro |
| Corpo | `#353E4F` | Texto corrido sobre claro |
| Apoio | `#525A6F` | Legenda, rótulo, texto secundário |

**O roxo pode ser texto** sobre fundo claro — mas na versão `#9025F4`, que passa 4,5:1 sobre
branco e sobre as lavandas. O `#9934FF` fica para fundo, ícone e grafismo.

O Optimall **não tem cor secundária**: régua, chip e bullet usam o próprio roxo. Os degradês,
o vidro e os lilases do deck e do post estão nos `tokens.md` de cada material
(`design-system/apresentacao/tokens.md`, `design-system/post/tokens.md`) e em `paleta_extra`
do `marca.json`. Os do e-mail, em `design-system/newsletter/tokens.md`. Nenhuma cor fora
dessas listas.

## Regras de cor e contraste

**Nunca escreva cor solta.** Toda cor sai dos tokens do material
(`design-system/<material>/tokens.md`), e os valores por papel estão em `marca.json`.
Todo material passa pelo `scripts/conferir.py` antes de ser entregue: ele acusa cor fora da
paleta.

**Nenhum texto abaixo de 4,5:1.** Vale para qualquer material — e-mail, deck, post, impresso.

**Texto em cima do roxo é branco.** É o papel `ink-on-brand` do `marca.json`, medido — nunca
se escolhe no olho.

**Logo não é texto.** Ele é marca gráfica, e a regra de contraste governa palavras. O que é
proibido é **recolorir por filtro ou por efeito** (abaixo).

**Não se inventa URL nem arte** para o que já existe em [`links-oficiais.md`](links-oficiais.md).

## Tipografia

**Halyard Text** (Adobe Fonts, licença do time). Pesos em uso: **400** (corpo) e **500**
(títulos, números, botões). Títulos com espaçamento negativo (−0,02em).

- Vem da web, pelo **kit do Adobe Fonts** do Optimall
  (`<link rel="stylesheet" href="https://use.typekit.net/kor2grf.css">`), com o nome de família
  `halyard-text-variable` (variável, pesos 100 a 800). Os templates de deck e post já trazem o
  link. O `scripts/exportar.py` confere antes de gerar PNG ou PDF e para se ela não carregar.
- **E-mail não usa Halyard**: quem recebe não tem a fonte. O e-mail segue a pilha de fontes do
  design system de newsletter.

## Logo

Em `assets/header/`. O logo do Optimall é **tricolor** — símbolo de três formas sobrepostas e
a palavra *optimall*. As versões oficiais vêm do Figma *[BRAND] Optimall – ID Assets* (nós 55:43 colorido, 55:89 branco, 69:78 preto), e **nenhuma se recolore**:

| Arquivo | Versão | Onde |
|---|---|---|
| `logo-optimall.svg` | Colorido: símbolo `#9934FF`/`#525A6F`/`#BD7CFF`, palavra `#525A6F` | Fundo branco ou lavanda |
| `logo-optimall-branco.svg` | Branco, monocromático (a sobreposição do símbolo em transparência) | Fundo roxo (deck, post) ou escuro (e-mail no modo escuro), foto |
| `logo-optimall-preto.svg` | Preto, monocromático | Impressão a uma cor, fundo claro sem cor |
| `simbolo-optimall.svg` | Só o símbolo, colorido | Selo pequeno, avatar, favicon |
| `logo-optimall.png`, `-branco.png`, `-preto.png` | As três versões oficiais em 2x, transparentes (286×48, exibidas a 143×24) | E-mail: `01-header` usa o branco sobre a faixa roxa; `90-social`, o colorido (e o branco no modo escuro) |

O logo **não é monocromático**: não se pinta por `currentColor`, não se troca cor por
`filter`, não se redesenha. Usa-se a versão certa para o fundo. No deck e no post ele entra
como `<symbol>` do template (`#logo-optimall` e `#logo-optimall-branco`).

## Assinatura "Uma solução Optimall"

Vai em toda peça das marcas que o Optimall assina — hoje, o **Byfrost**. A marca assinada fala
primeiro; o Optimall assina no fim da leitura. Arquivos em `assets/assinatura/`, publicados no
hub de marcas nas mesmas chaves que o Byfrost usa
(`https://marcas.taclalabs.workers.dev/optimall/assinatura/optimall-assinatura-<cor>.svg`, com
PNG de 600 e 1200 px).

| Arquivo | Onde |
|---|---|
| `optimall-assinatura-branco.svg` | Arquivo oficial. Fundo roxo, degradê, foto ou fundo escuro |
| `optimall-assinatura-preto.svg` | A branca em preto. Fundo branco ou claro: app, PDFs do sistema, impressos |
| `optimall-assinatura-colorido.svg` | "Uma solução" em grafite `#525A6F` + o logo colorido. Só fundo branco, em e-mail e material externo. Nunca sobre degradê nem colada a outro logo colorido |

- **Mínimo:** 140 px de largura na tela e 35 mm no impresso. Área livre em volta: a altura dela.
- **Hierarquia:** sempre menor que o logo da marca assinada, no fim da leitura — rodapé, pé do
  painel, último slide. Nunca no cabeçalho nem no lugar do logo.
- **Use o arquivo.** Não reescreva "Uma solução" em texto, não separe o símbolo do texto, não
  recolora.
- Não vai em app icon, favicon, webclip nem avatar.
- A colorida usa no símbolo o mesmo lilás do logo oficial (`#BD7CFF`).

## Grafismos

A linguagem visual do Optimall (deck e post) — degradê radial roxo, pattern de pontos lilás
que some em direção ao centro, o símbolo gigante em transparência, cards brancos e painéis de
vidro sobre lavanda, pílulas de número, chips de ícone roxos. Arquivos em
`assets/grafismos/`; as receitas, nos `tokens.md` de deck e post.

## A pasta `assets/`

| Pasta | O que tem | No repositório? |
|---|---|---|
| `header/` | Logo colorido, branco e preto, símbolo (SVG) e PNGs 2x do e-mail | Sim |
| `assinatura/` | "Uma solução Optimall" em preto, branco e colorido (SVG) | Sim |
| `icones/` | Ícones sociais roxos do e-mail (`<rede>-marca.png`) | Sim |
| `icones-ui/` | Ícones HugeIcons bulk em `currentColor`, para chips de deck e post | Sim |
| `clientes/` | Logos dos shoppings clientes: `<nome>-roxo.svg` (deck) e `<nome>.png` (cinza-azulado, do site) | Sim |
| `parceiros/` | Logos das integrações (estacionamento, cinema, intranet) | Sim |
| `grafismos/` | Símbolo gigante, vidros, elipse e demais grafismos do Figma | Sim |
| `produto/` | Telas do painel e do app (`deck-*`, `post-*`) — a prova visual do produto | **Não — só no computador** |
| `fotos/` | Fotos aprovadas dos posts (banco de imagem licenciado) | **Não — só no computador** |

**`produto/` e `fotos/` ficam fora do Git.** O repositório é público, e telas do produto e
fotos de banco de imagem não podem ser redistribuídas. Quem cuida do repositório passa a pasta
ao time por fora; ela é copiada para `brand/assets/` e o resto funciona igual. Se a peça
precisar de uma tela ou foto e a pasta não estiver no computador, a resposta é: *"as telas e
fotos do produto não estão neste computador — peça a pasta a quem cuida do repositório"*.

Tela de produto é sempre a real, desta pasta: a IA não gera nem redesenha painel, dashboard ou
app.

## E-mail

O e-mail do Optimall sai por um sistema de envio cujas regras (variáveis aceitas, hospedagem
das imagens) ainda não foram passadas. Até lá:

- a peça sai **sem nenhuma variável `{{...}}`** — nem `{{email}}` no rodapé;
- o relatório de entrega avisa que a regra de envio está pendente.

O botão do e-mail é roxo com **texto branco**. O rodapé legal leva só a Política de
Privacidade: o Optimall não tem Termos de Uso.

Ver `envio` em `marca.json` e `design-system/newsletter/guidelines/variaveis-envio.md`.

## Fotografia

Segue o Style Lock, e o bloco `STYLE LOCK` se copia sem editar uma palavra:
[`photography/STYLE-LOCK-OPTIMALL.md`](photography/STYLE-LOCK-OPTIMALL.md). Como ler:
[`photography/README.md`](photography/README.md). O procedimento é o `/foto-optimall`.
