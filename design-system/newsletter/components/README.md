# Componentes — newsletter

Blocos de HTML de e-mail. **Copiar e colar** dentro do
[`templates/newsletter/base.html`](../../../templates/newsletter/base.html), no lugar marcado.
Não editar o arquivo do componente por campanha.

A numeração é a ordem em que os blocos costumam aparecer na peça.

| Arquivo | O que é |
|---|---|
| `01-header.html` | Header: logo do Optimall centralizado numa placa branca |
| `02-hero-title.html` | Headline de abertura |
| `02a-eyebrow.html` | Tag / eyebrow acima de um título |
| `02b-titulo-secao.html` | Título de seção |
| `03-hero-image.html` | Imagem de abertura, largura inteira |
| `04-texto-cta.html` | Bloco de texto com CTA |
| `05-card-quote.html` | Citação |
| `06-card-oferta.html` | Card de oferta |
| `07-artigos-alternados.html` | Artigos com imagem alternando esquerda/direita (1:1) |
| `08-destaque-numeros.html` | Números de destaque com label. Variante A 3 colunas, B 1 coluna |
| `09-galeria-2col.html` | Galeria de duas colunas |
| `10-divider.html` | Divisor |
| `11-card-noticia.html` | Notícia com imagem no topo, largura inteira (16:9) |
| `12-card-noticia-compacta.html` | Notícia com miniatura ao lado do texto (1:1) |
| `13-card-conteudo.html` | Card único com todo o conteúdo dentro + os itens dele (texto, título de grupo, lista, nota, linha fina, CTA) |
| `13a-card-galeria-2col.html` | Item do `13`: galeria de 2 colunas 1:1 com texto e etiqueta opcional |
| `13b-card-extrato.html` | Item do `13`: extrato de dados, rótulo à esquerda e valor à direita |
| `90-social.html` | Rodapé social: logo à esquerda, Instagram e LinkedIn à direita — URLs já fixas |
| `91-footer-legal.html` | Rodapé legal completo |
| `99-spacer.html` | Espaçador vertical |
| `_button.html` | CTA no padrão VML (`<v:roundrect>` + `<a>`). Variante A roxa, B neutra escura |

Obrigatórios em toda peça: `01-header`, `90-social` e `91-footer-legal`.
Entre blocos, usar `99-spacer`.

---

## Header e rodapé

- O **header** é uma placa branca com o logo positivo (tricolor) em PNG, 143 × 24. A placa
  **não escurece** no dark mode: ela garante o logo colorido legível em todo cliente, sem
  depender de troca de imagem por CSS (`guidelines/email-compat.md`).
- O **rodapé social** leva o mesmo logo — e, no modo escuro, troca pelo logo branco oficial
  onde o cliente permite (Apple Mail, iOS, Outlook.com); no resto, fica o colorido e só as redes oficiais: Instagram e LinkedIn
  (`brand/marca.json` → `redes`). O Optimall não tem Facebook nem Spotify — não acrescentar
  rede que não existe. Fica numa linha só também no mobile.
- O **rodapé legal** é `© <ano> - Optimall`, o motivo do recebimento e a Política de
  Privacidade. Sem Termos de Uso (o Optimall não tem) e sem nenhuma variável `{{...}}`
  enquanto a regra de envio estiver pendente (`guidelines/variaveis-envio.md`).

---

## O card único

`13-card-conteudo` resolve e-mail curto de uma mensagem só — transacional, gatilho de
campanha —, em que vários cards soltos quebrariam a leitura. Ele conta como **uma** seção
no limite de quatro. Dentro dele:

- linha fina entre grupos, e **sempre** antes do botão (o item CTA já traz a linha);
- **um CTA só**, sempre o último item;
- `13a` é diferente do `09-galeria-2col`: o `09` é solto na página, 4:3 e sem texto; o
  `13a` vive dentro do card, é 1:1 e carrega texto.

---

## Caminhos de imagem

Os `src` dos componentes apontam para `../../brand/assets/…`, que é o caminho correto a
partir de `saida/<slug>/index.html`. Se o arquivo montado for para outro lugar, ajustar.
Antes de enviar, esses caminhos relativos viram URLs absolutas `https://`.
