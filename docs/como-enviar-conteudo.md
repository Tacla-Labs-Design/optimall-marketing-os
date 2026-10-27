# Como enviar o conteúdo para o Claude montar o material

Guia para quem escreve. Não precisa saber HTML.

Você entrega **duas coisas**: um documento com os textos e uma pasta com as imagens.
O Claude cuida do resto — layout, cores, dark mode, versão mobile, QA.

Todo material do Optimall fala com **quem decide no shopping** — superintendência,
marketing, CRM, operação. Nunca com o consumidor final. Os números, os nomes dos módulos e
as frases prontas estão em [`brand/mensagens.md`](../brand/mensagens.md): comece por lá.

---

## 1. Crie a pasta

Dentro de `projects/_inbox/`, crie uma pasta com este nome:

```
AAAA-MM-<assunto>
```

Exemplos: `2026-10-lancamento-clube`, `2026-11-deck-grupo-norte`, `2026-11-carrossel-campanhas`.

Dentro dela:

```
2026-10-lancamento-clube/
├── brief.docx          ← os textos (pode ser .md, .txt ou .pdf também)
└── imagens/            ← as imagens (ou um imagens.zip, o Claude descompacta)
```

---

## 2. E-mail

### O documento

Não precisa formatar bonito. O que o Claude precisa achar:

**No começo, o cabeçalho do envio:**

```
Público: gestores de marketing dos shoppings clientes
Data de envio: 15/10/2026
Objetivo: apresentar o novo Clube de Benefícios e levar a uma conversa com o consultor
Chamada: A campanha termina. O clube mantém o cliente.
Texto de apoio: Pontos, recompensas por perfil e comunicação segmentada, num lugar só.
Motivo do recebimento: você é gestor de um shopping parceiro do Optimall
```

**Depois, um bloco por assunto, numerado na ordem em que deve aparecer:**

```
## 01 — Pontos em cada campanha
Tag: Clube de Benefícios
Texto: Cada nota fiscal validada numa campanha vira ponto no clube, e o cliente
volta para usar.

## 02 — Comunicação pelo histórico de compras
Tag: CRM & Dados
Texto: Em vez de disparo genérico para a base toda, a mensagem certa para cada perfil.
```

O número (`01`, `02`…) é o que amarra o texto à imagem. É a parte que não pode faltar.

**O botão** do Optimall é fixo: *Fale com um consultor*, com o link oficial. Não precisa
mandar. Se quiser outro destino, diga o rótulo e o link:

```
CTA: Ver o case → https://exemplo.com.br/case
```

**Variáveis como `{{nome}}` não entram.** O sistema que dispara o e-mail do Optimall ainda
não passou a regra das variáveis que aceita; até lá, o e-mail sai sem nenhuma. Link de
descadastro também não entra.

### As imagens

O nome do arquivo diz ao Claude **de qual bloco é a imagem** e **como ela vai ser usada**.

```
NN-nome-curto.jpg          → imagem no topo do bloco, ocupando a largura inteira
NN-nome-curto-1x1.jpg      → imagem ao lado do texto (esquerda ou direita)
capa.jpg                   → a imagem grande da abertura
```

O `NN` é o mesmo número do bloco no documento. O `nome-curto` é só para você se achar —
o Claude usa o número.

```
imagens/
├── capa.jpg                    → abertura
├── 01-pontos-clube.jpg         → bloco 01, imagem no topo
└── 02-crm-1x1.jpg              → bloco 02, imagem lateral
```

Se um bloco não tiver imagem, é só não mandar — o Claude usa um layout só de texto.

**As duas proporções.** Não é preferência de estilo: e-mail **não recorta imagem**. O
arquivo entra com a forma que tem. Fora da proporção, ele distorce ou estoura a coluna.

| Sufixo | Onde aparece | Proporção | Tamanho mínimo |
|---|---|---|---|
| *(sem sufixo)* | No painel do bloco, largura inteira | **16:9 ou mais panorâmica** | 1072 × 604 |
| `-1x1` | No painel do bloco ou ao lado do texto | **1:1 exata** (quadrada) | 800 × 800 |
| `capa` | Abertura | **16:9 ou mais panorâmica** | 1072 × 602 |

Os tamanhos são o dobro do que aparece na tela — é o que mantém a imagem nítida em
celular moderno. Menor que isso, borra.

**Sobre o 1:1:** se a imagem original é vertical (print de celular, foto em pé), recorte
num quadrado **antes** de mandar. Você escolhendo o recorte sai melhor do que qualquer
corte automático.

**Formato: JPG ou PNG.** Não mande WebP, AVIF, HEIC nem SVG — Outlook e Gmail não abrem, e o
leitor vê um quadrado vazio.

---

## 3. Apresentação

```
Objetivo: reunião comercial com o grupo X — apresentar a plataforma
Para quem: superintendente e gerente de marketing
Duração: 20 minutos

## Roteiro (se você já tiver um)
1. Capa
2. O problema: sistemas que não conversam
3. A plataforma
4. Campanhas Promocionais
5. Encerramento
```

- **Sem roteiro?** Diga o objetivo e para quem — o Claude propõe o roteiro e **espera você
  confirmar** antes de montar.
- Os slides da biblioteca já vêm com o texto aprovado do deck comercial. Num deck comercial
  padrão, boa parte fica como está.
- **Número só se estiver no guia** (`brand/mensagens.md`). Número novo: mande a fonte e avise
  quem cuida do repositório.
- **Telas do produto já estão no padrão.** Mande só imagem que não existe lá, nomeada com o
  número do slide (`04-relatorio.png`).

Você recebe o deck em `saida/<slug>/index.html` e o PDF ao lado.

---

## 4. Post ou carrossel

Mesma pasta em `projects/_inbox/`, com um documento curto. Um bloco por card:

```
Onde sai: Instagram e LinkedIn
Formato: carrossel
Objetivo: gestor de marketing pedir uma conversa com o comercial

## 01 — capa
Sistema de gestão para ações promocionais

## 02
3 modalidades de campanha: Compre e Ganhe, Compre e Concorra, Roleta de Prêmios

## 03 — fecho
Seja cliente Optimall
```

- **Uma ideia por card.** O que não cabe vira outro card; o texto longo vai para a legenda,
  que o Claude escreve.
- **Número só se estiver no guia** (`brand/mensagens.md`).
- **Imagem:** telas do painel e do app já estão no padrão; mande só foto nova ou print
  específico, nomeado com o número do card (`02-painel-campanha.png`). Foto de pessoa em
  proporção 4:5 (em pé) ou 1:1.
- **Depoimento só real**, com nome, cargo e empreendimento, e com autorização.

Você recebe de volta os PNGs de cada card (`saida/<slug>/png/`) e a legenda pronta para
Instagram e LinkedIn (`saida/<slug>/legenda.txt`).

---

## 5. Peça a montagem

Abra o Claude Code na pasta do projeto e escreva o comando do material com o nome da pasta:

```
/newsletter-optimall 2026-10-lancamento-clube
/apresentacao-optimall 2026-11-deck-grupo-norte
/post-optimall 2026-11-carrossel-campanhas
```

Ou, em português mesmo:

> Gera a newsletter de projects/_inbox/2026-10-lancamento-clube

---

> Antes de montar, o Claude atualiza sozinho o padrão para a versão mais recente — você
> não precisa fazer nada. Se ele avisar que não conseguiu, é só falar com quem cuida do
> padrão. O que mudou em cada versão fica no [CHANGELOG.md](../CHANGELOG.md).

## 6. O que você recebe de volta

- O material montado em `saida/<slug>/` — pasta local, não vai para o Git
- No e-mail: **subject** (até 45 caracteres), **preheader** (60 a 90) e a lista de imagens
  para hospedar, com o tamanho final de cada uma
- No deck: o PDF. No post: os PNGs e a legenda
- O que ficou de fora do briefing e por quê

---

## Erros que aparecem toda semana

**Imagem sem número.** `foto-legal.jpg` não diz a que bloco pertence. O Claude vai
perguntar em vez de adivinhar — e você perde uma rodada.

**Vertical marcada como `-1x1`.** Um print de celular 9:16 salvo como `03-app-1x1.jpg`
não vira quadrado sozinho. Recorte antes.

**Imagem pequena.** Uma imagem de 600px de largura numa faixa que precisa de 1072 fica
borrada em qualquer celular recente.

**Texto importante dentro da imagem.** Número, data, título: a maioria dos clientes de e-mail
bloqueia imagem por padrão, e quem abre vê um retângulo cinza. Esse tipo de informação tem
que estar no documento, como texto.

**Falar com o consumidor.** "Baixe o app", "participe e ganhe": isso é peça do shopping, não
do Optimall. O Claude vai sinalizar e propor o texto para o gestor.

**Mais de 4 blocos de conteúdo no e-mail.** Acima disso o e-mail cansa e a taxa de clique
cai. Se o mês rendeu muito, o caminho é dividir em dois envios.
