# Optimall · e-mail

E-mail marketing ou newsletter B2B: fala com quem decide no shopping (superintendência,
marketing, CRM, operação), nunca com o consumidor final. O arquivo final é o próprio HTML.

Regras da marca: `https://marcas.taclalabs.workers.dev/optimall/BRAND.md`.

## Briefing

Obrigatório:
- **Assunto** (até 45 caracteres) e **chamada** de abertura.
- **O que a peça quer**: o pedido é sempre *Fale com um consultor*.
- **Título da edição** (o nome do módulo ou da série, até 24 caracteres) e o mês do envio.
- **Imagem de abertura** 16:9 (mínimo 1072 px de largura), e até 2 imagens quadradas (mínimo
  800 × 800) se houver artigos com imagem.
- **Motivo do recebimento** (ex.: "é gestor de um shopping parceiro do Optimall").

Padrão se faltar:
- Preheader: escreva a partir da chamada, 60 a 90 caracteres.
- Números: os oficiais do `BRAND.md`. Número que não está lá não entra.
- Sem imagem de abertura: apague a linha da imagem no topo (o mesh fica só com logo e título).
- Título e frase da faixa de CTA: escreva a partir da chamada — título até 40 caracteres, frase
  de uma linha.
- Briefing que fala com o consumidor ("participe", "ganhe prêmios"): pare e pergunte.

## Modelo

`https://marcas.taclalabs.workers.dev/optimall/modelos/email.html` — 600 px, só tabelas e CSS
inline, com dark mode. Desenho fixo, sobre a página branca, tudo alinhado à esquerda:

1. **Topo com gradient mesh claro:** logo colorido, título da edição grande, data e a imagem de
   abertura entrando no degradê.
2. **Conteúdo solto na página:** headline e texto; linha fina; seção com título grande e duas
   notícias com a imagem num painel lavanda; os números oficiais.
3. **Faixa de CTA em gradient mesh roxo:** título e frase em branco, botão branco
   *Fale com um consultor*.
4. **Rodapé na faixa lavanda:** logo e redes, `© <ano> - Optimall`, motivo do recebimento e
   Política de Privacidade.

O gradient mesh é imagem pronta da marca, já no modelo. Não gere outro, não troque as cores e
não escreva degradê em CSS: Gmail e Outlook ignoram.

Troque só o que tem `data-slot`. Texto entre colchetes é exemplo.

| Campo | Limite |
|---|---|
| `preheader` | 60 a 90 caracteres |
| `titulo-edicao` | até 24 caracteres, uma linha ("Clube de Benefícios") |
| `data` | mês e ano do envio |
| `titulo` | manchete de abertura, até 60 caracteres, 2 linhas |
| `texto-abertura` | 1 a 3 frases, até 200 caracteres |
| `titulo-secao` | uma linha ("Como funciona") |
| `artigo-N-titulo` | até 40 caracteres |
| `artigo-N-texto` | até 3 linhas, cerca de 160 caracteres |
| `imagem-abertura` | 16:9 ou mais panorâmica, arquivo com 1072 px de largura ou mais |
| `artigo-N-imagem` | quadrada (tolerância de 2%), 800 × 800 ou mais. Print de tela com fundo branco: painel `#F9F8FC` e borda na imagem (a nota está no modelo) |
| `titulo-cta` | até 40 caracteres |
| `frase-cta` | uma linha só — é ela que garante o contraste do texto branco |
| `motivo` | uma frase, depois de "porque" |
| `ano` | o ano do envio |

- **No máximo 4 seções de conteúdo.** Para tirar um bloco, apague o `<tr>` inteiro dele.
- **Um CTA por peça,** na faixa roxa: o botão *Fale com um consultor* →
  `https://www.optimall.com.br/fale-conosco`. Artigo sem link próprio fica sem link — não
  repita o botão.
- Texto sobre o roxo é sempre **branco**; o botão da faixa é branco com texto `#9025F4`. Texto
  roxo sobre claro é `#9025F4`. O texto do topo fica escuro, sobre a parte clara do mesh.
- Imagem: JPG ou PNG. Nunca WebP, AVIF, HEIC nem SVG (Outlook e Gmail não mostram). E-mail não
  recorta: a imagem entra com a proporção que tem. Proporção errada, peça outro arquivo.
- Imagens precisam estar hospedadas: o `src` é o endereço público de cada uma.
- Tela do produto (painel, app) não está no hub: entra como imagem que o time manda. Nunca gere
  nem redesenhe tela.
- **Nenhuma variável `{{...}}`** e nenhum link de descadastro: a regra do sistema de envio do
  Optimall ainda está pendente. Avise isso na entrega.
- **Nunca apague os condicionais do Outlook** (`<!--[if mso]>`, `<!--[if !mso]><!-->`,
  `<!--<![endif]-->`): sem eles o botão some.
- Fonte do e-mail: Inter, já no modelo. Não troque pela Halyard.
- Peso do HTML final abaixo de 100 KB (o Gmail corta acima disso).

## Gerar o arquivo

O HTML preenchido é o arquivo final: ele vai para o sistema de envio. Para ver como fica,
abra no navegador; para ver o modo escuro, ative o tema escuro do sistema operacional.

## Conferência

- [ ] Assunto até 45 caracteres; preheader entre 60 e 90.
- [ ] Nenhum texto entre colchetes sobrou; nenhum `{{...}}` na peça.
- [ ] Topo com o mesh, o logo, o título da edição, a data e a imagem de abertura; conteúdo
      alinhado à esquerda; faixa de CTA roxa; rodapé na faixa lavanda.
- [ ] Um botão só, *Fale com um consultor*, branco, na faixa roxa.
- [ ] Números só os oficiais, com "+" e a legenda.
- [ ] Toda imagem com `alt` e hospedada; proporções certas.
- [ ] "o Optimall", nunca "a Optimall"; nada do Podi nem da Tacla Labs.
- [ ] Rodapé com `© <ano> - Optimall`, o motivo e só a Política de Privacidade.
- [ ] Aviso na entrega: a regra de envio do Optimall está pendente.
