# Componentes — newsletter

Blocos de HTML de e-mail. **Copiar e colar** dentro do
[`templates/newsletter/base.html`](../../../templates/newsletter/base.html), no lugar marcado.
Não editar o arquivo do componente por campanha.

A numeração é a ordem em que os blocos costumam aparecer na peça.

| Arquivo | O que é |
|---|---|
| `01-header.html` | Topo: gradient mesh claro com logo, título da edição, data e a imagem de abertura entrando no degradê |
| `02-hero-title.html` | Headline de abertura, logo depois do topo |
| `02a-eyebrow.html` | Tag / eyebrow acima de um título |
| `02b-titulo-secao.html` | Título de seção, grande ("Como funciona", "Em números") |
| `03-hero-image.html` | Imagem solta em largura inteira no meio do conteúdo (a de abertura vai no `01-header`) |
| `04-texto-cta.html` | Parágrafo de apoio, com CTA opcional |
| `05-card-quote.html` | Citação, em painel lavanda |
| `06-card-oferta.html` | Oferta, em painel lavanda |
| `07-artigos-alternados.html` | Artigos com imagem alternando esquerda/direita (1:1) |
| `08-destaque-numeros.html` | Números de destaque. Variante A lista (um por linha), B um número em painel |
| `09-galeria-2col.html` | Galeria de duas colunas |
| `10-divider.html` | Divisor |
| `11-card-noticia.html` | Notícia: imagem num painel (A arte, B tela, C recorte) + título, texto e link opcional |
| `12-card-noticia-compacta.html` | Notícia com miniatura ao lado do texto (1:1), solta na página |
| `13-card-conteudo.html` | Card único com borda, com todo o conteúdo dentro + os itens dele (texto, título de grupo, lista, nota, linha fina, CTA) |
| `13a-card-galeria-2col.html` | Item do `13`: galeria de 2 colunas 1:1 com texto e etiqueta opcional |
| `13b-card-extrato.html` | Item do `13`: extrato de dados, rótulo à esquerda e valor à direita |
| `89-faixa-cta-mesh.html` | Fecho: faixa em gradient mesh roxo com título, frase e o CTA principal em botão branco |
| `90-social.html` | Rodapé social, na faixa lavanda: logo à esquerda, Instagram e LinkedIn à direita — URLs já fixas |
| `91-footer-legal.html` | Rodapé legal completo, continuando a faixa lavanda |
| `99-spacer.html` | Espaçador vertical |
| `_button.html` | CTA no padrão VML (`<v:roundrect>` + `<a>`). Variante A roxa, B neutra escura, C branca (só sobre o mesh roxo) |

Obrigatórios em toda peça: `01-header`, `90-social` e `91-footer-legal`.

O desenho da peça é sempre o mesmo, sobre a **página branca**: **topo com mesh** (logo,
título da edição, data, imagem de abertura) → **conteúdo solto na página**, alinhado à
esquerda, com seções separadas por linha fina e título grande → **faixa de CTA em mesh roxo**
(`89`) → **rodapé na faixa lavanda** (`90` + `91`).
Entre blocos de conteúdo, usar `99-spacer`. Da `89` em diante, as faixas ficam coladas, sem
espaçador.

---

## Header e rodapé

- O **header** é o topo com o gradient mesh claro (`brand/assets/grafismos/mesh-email-topo.png`),
  o logo colorido oficial em PNG, 143 × 24, o título da edição em 46px e a linha de data, tudo
  à esquerda. A imagem de abertura entra embaixo, com borda fina, e o degradê some para o fundo
  da página atrás dela. O texto do topo fica escuro nos dois modos: o mesh atrás dele é claro
  também no escuro (`tokens.md` → Gradient mesh).
- A **faixa de CTA** (`89`) é o fecho e o lugar do único CTA da peça: mesh roxo, texto branco,
  botão branco *Fale com um consultor*. Peça montada no `13-card-conteudo` leva o CTA dentro do
  card e não usa a faixa.
- O **rodapé** é uma faixa lavanda (`#FAF5FF`) de borda a borda. O **rodapé social** leva o mesmo logo — e, no modo escuro, troca pelo logo branco oficial
  onde o cliente permite (Apple Mail, iOS, Outlook.com); no resto, fica o colorido e só as redes oficiais: Instagram e LinkedIn
  (`brand/marca.json` → `redes`). O Optimall não tem Facebook nem Spotify — não acrescentar
  rede que não existe. Fica numa linha só também no mobile.
- O **rodapé legal**, alinhado à esquerda, é `© <ano> - Optimall`, o motivo do recebimento e a Política de
  Privacidade. Sem Termos de Uso (o Optimall não tem) e sem nenhuma variável `{{...}}`
  enquanto a regra de envio estiver pendente (`guidelines/variaveis-envio.md`).

---

## O card único

`13-card-conteudo` resolve e-mail curto de uma mensagem só — transacional, gatilho de
campanha —, em que vários blocos soltos quebrariam a leitura. Ele conta como **uma** seção
no limite de quatro. Dentro dele:

- linha fina entre grupos, e **sempre** antes do botão (o item CTA já traz a linha);
- **um CTA só**, sempre o último item;
- `13a` é diferente do `09-galeria-2col`: o `09` é solto na página, 4:3 e sem texto; o
  `13a` vive dentro do card, é 1:1 e carrega texto.

---

## Caminhos de imagem

Os `src` (e os `background` do mesh) dos componentes apontam para `../../brand/assets/…`, que é o caminho correto a
partir de `saida/<slug>/index.html`. Se o arquivo montado for para outro lugar, ajustar.
Antes de enviar, esses caminhos relativos viram URLs absolutas `https://`.
