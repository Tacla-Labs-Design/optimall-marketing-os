---
name: newsletter-optimall
description: Monta uma newsletter, informativo ou e-mail marketing do Optimall (B2B, para gestores de shopping) a partir de um briefing em projects/_inbox/<slug>/. Use quando pedirem para gerar, montar ou criar uma newsletter, um informativo ou um e-mail marketing do Optimall a partir de um documento e uma pasta de imagens.
---

# Montar uma newsletter do Optimall

Argumento: o slug da pasta em `projects/_inbox/`. Sem argumento, listar as pastas
disponíveis e perguntar qual.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e
valem integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md`, `brand/links-oficiais.md`, `brand/marca.json` | Identidade, contraste, público, links fixos, regra de envio |
| Brand | `brand/mensagens.md` | O que dizer: números oficiais, módulos, voz, frases aprovadas |
| Brand | `brand/photography/STYLE-LOCK-OPTIMALL.md` | Direção fotográfica — só quando a peça pedir **foto nova** |
| Design System | `design-system/newsletter/` | Tokens, componentes, compatibilidade, ritmo, variáveis de envio, QA |
| Template | `templates/newsletter/base.html` | O shell |

Em caso de conflito, a camada mais alta prevalece. Ver `docs/governanca.md`.

O Optimall é **masculino**: "o Optimall", "do Optimall". Nunca "a Optimall".

## 0. Atualizar o padrão

Antes de qualquer coisa, e **sem perguntar nada ao usuário**:

```bash
./scripts/check-atualizacao.sh --atualizar
```

Quem usa este comando não é pessoa técnica (`CLAUDE.md`). Não peça para ela rodar Git:
o script já traz a versão nova sozinho.

- **Saída 0** → seguir. Se o script disse que atualizou, mencione em uma linha, em
  português comum: *"Atualizei o padrão para a versão mais recente antes de montar."*
  Se não atualizou nada, não comente — silêncio é o esperado.
- **Saída 1** → houve alteração local conflitante. **Parar.** Dizer que esta cópia do
  padrão está diferente da oficial e que é preciso avisar quem cuida do repositório.
  Não tentar resolver, não sugerir comando, não montar assim mesmo: o e-mail sairia com
  o template antigo e nada no arquivo denunciaria isso.

Sem Git, sem remoto ou offline, o script sai 0 e o trabalho segue normalmente.

## 1. Ler tudo antes de decidir qualquer coisa

```bash
ls -R projects/_inbox/<slug>/
```

- `.docx` → `textutil -convert txt -stdout arquivo.docx`
- `.pdf` → `pdftotext arquivo.pdf -`
- `.zip` → `unzip -o arquivo.zip -d projects/_inbox/<slug>/imagens/`
- Imagens → **abrir de fato** com a tool Read. Nome de arquivo não é prova de conteúdo,
  e você precisa da proporção real para escolher o bloco.

O e-mail do Optimall é **sempre B2B**: fala com quem decide no shopping (superintendente,
gerente de marketing, gestor de operação), nunca com o consumidor final. Se o briefing
parece falar com o consumidor, **perguntar** antes de montar.

## 2. Mapear imagem → componente

O nome do arquivo carrega a intenção (ver `docs/como-enviar-conteudo.md`):

| Nome | Significado | Componente |
|---|---|---|
| `capa.*` | Abertura da edição | a imagem do `01-header`, entrando no mesh do topo |
| `NN-nome.*` | Notícia NN, imagem em largura inteira | `11-card-noticia`, imagem no painel |
| `NN-nome-1x1.*` | Notícia NN, imagem quadrada | `11-card-noticia` (painel, 400px), `07-artigos-alternados` ou `12-card-noticia-compacta` |

No `11`, o painel se escolhe pela imagem: **arte** (mockup, ilustração) → variante A, lavanda;
**print de tela** com fundo branco → variante B, `#F9F8FC` com borda; **PNG transparente**
(celular na mão, produto recortado) → variante C, encostando no pé do painel. Abra a imagem
para saber — o nome não diz.

O `NN` casa com o número do bloco no documento. Se o texto e a imagem não fecharem,
**perguntar** — associação errada é pior que pergunta a mais.

Tela do produto (painel, app) entra como imagem do briefing ou de `brand/assets/produto/`.
Essa pasta fica fora do Git: se ela não existir neste computador, dizer *"as telas e fotos do
produto não estão neste computador — peça a pasta a quem cuida do repositório"* e montar o
resto.

## 3. Conferir a proporção antes de montar

E-mail não recorta imagem: o arquivo entra com a forma que tem.

- Sem sufixo / `capa` → **16:9 ou mais panorâmica**, mínimo 1072px de largura
- `-1x1` → **quadrada**, tolerância de 2%, mínimo 800×800 (no painel do `11` ela aparece a
  400px; no `07`, a 248px, e 496×496 basta)
- Galeria dentro do card (`13a`) → **quadrada**, mínimo 448×448

Quando não bater, **não distorça e não corte por conta própria**. Monte o resto do
e-mail e relate no fim: qual arquivo, qual proporção veio, qual era esperada.

Exceção: se a imagem estiver só acima do tamanho mínimo (proporção certa, sobra de
pixel), pode usar — o `width` do HTML resolve.

Formato fora de JPG/PNG (WebP, AVIF, HEIC, SVG) é bloqueio: converter com
`sips -s format jpeg` e avisar, ou pedir o arquivo certo.

## 4. Montar

1. Público e tom estão em `brand/README.md`; **o texto** — manchete, corpo, números, frases —
   sai de `brand/mensagens.md`. Número que não está lá não entra.
   **Nenhuma peça leva link de descadastro**
   (`design-system/newsletter/guidelines/variaveis-envio.md`).
2. Copiar `templates/newsletter/base.html` para **`saida/<slug>/index.html`** e colar os
   blocos de `design-system/newsletter/components/` no lugar marcado: `01-header` (mesh claro,
   logo, título da edição, data e a `capa`) → blocos de conteúdo (`02` a `13b`), soltos na
   página branca e alinhados à esquerda → `89-faixa-cta-mesh` (o CTA da peça) → `90-social` →
   `91-footer-legal`. O ritmo e os espaçadores estão em
   `design-system/newsletter/guidelines/layout-ritmo.md`.
   O **título da edição** é o nome do módulo ou da série ("Clube de Benefícios", "Novidades do
   Optimall"), até 24 caracteres — não é a manchete; a manchete vai no `02`, logo depois do
   topo. A **linha de data** é o mês e o ano do envio. Trocar o
   `{{TITULO_INTERNO}}` e o `{{PREHEADER}}` do template (preheader que o briefing não trouxer,
   escrever a partir da chamada, 60–90 caracteres). Os comentários dos blocos podem ficar — o
   `conferir` não os lê. **Nunca apagar** os condicionais do Outlook (`<!--[if mso]>`,
   `<!--[if !mso]><!-->`, `<!--<![endif]-->`): sem eles o botão some.
   As imagens do briefing vão para **`saida/<slug>/imagens/`**, e a peça aponta para lá.
   Link de artigo (`07`, `11`, `12`) que o briefing não trouxer **sai** — a linha inteira —,
   em vez de repetir o CTA principal: um CTA por peça, e ele fica na `89-faixa-cta-mesh`. Os
   outros blocos com botão (`04`, `05`, `06`) entram sem a tabela do botão. A exceção é a peça
   montada no `13-card-conteudo`: o CTA fica dentro do card, e a `89` sai.
   O título e a frase da faixa saem do briefing ou de `brand/mensagens.md`: título até 40
   caracteres, frase de uma linha só (é ela que garante o contraste do texto branco).
   Nunca gravar em `examples/` — aquilo é acervo curado, gravado só por quem cuida do padrão.
3. Máximo de **4 blocos de conteúdo**. Passou disso, cortar ou propor dois envios.
4. Ativos e links fixos de `brand/links-oficiais.md` — logo, URLs sociais, CTA, Política de
   Privacidade — **não se inventa**. O CTA principal é *Fale com um consultor*, apontando
   para `links.cta` do `marca.json`.
5. **Nunca escrever cor solta.** Toda cor sai de `design-system/newsletter/tokens.md`. O roxo
   de marca é fundo (botão, tag); texto sobre ele é sempre branco; roxo como texto é o
   `accent-ink` `#9025F4`. O gradient mesh é imagem pronta (`brand/assets/grafismos/`): não se
   gera mesh novo, não se troca cor dele e não se escreve degradê em CSS na peça.
6. **Nenhuma variável `{{...}}`.** Enquanto `envio.variaveis` do `marca.json` estiver vazio,
   o rodapé sai sem o "em {{email}}" ("Você recebeu este e-mail porque …"), e campo
   personalizado do briefing (`{{nome}}` e afins) vira texto fixo ou sai da peça. Se o
   briefing insistir no campo, perguntar antes de montar.

## 5. Quando falta algo no sistema

Se o conteúdo pede um bloco, uma cor ou um layout que não existe:

1. **Não invente.** Não crie uma cor nova, não improvise um bloco com CSS solto.
2. Verifique se um componente existente resolve com outro conteúdo.
3. Se realmente não resolve, monte o resto do e-mail e **relate a ausência no fim**,
   marcada explicitamente como **proposta**: o que falta, onde seria usado, e o que você
   sugere.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer (`docs/governanca.md`).

Se o briefing pedir uma **fotografia que ainda não existe**, a direção visual não se
inventa: ela está em `brand/photography/STYLE-LOCK-OPTIMALL.md`. Relate o que falta e
aponte o Style Lock como referência — ou monte o prompt com `/foto-optimall`.

Isso vale **só para fotografia**. As imagens que chegam em `_inbox/` não passam por
avaliação de estilo fotográfico — muitas são print de tela, montagem gráfica ou arte, e
para elas o único critério continua sendo formato e proporção (§3).

Se o pedido do usuário conflita com o brand — outra cor, texto escuro sobre o roxo, logo
recolorido, falar com o consumidor final — **sinalize o conflito** em vez de alterar a
identidade. Explique a regra em uma frase e ofereça a alternativa que respeita o sistema.

## 6. QA e entrega

Rodar `design-system/newsletter/guidelines/qa-checklist.md` inteiro antes de dizer que
está pronto. Os itens verificáveis por comando:

```bash
python3 -I scripts/conferir.py saida/<slug>/index.html   # saída 0
```

Ele lê a peça sem os comentários e confere, de uma vez: peso abaixo de 100 KB, nada de
`<script>`, `<form>`, `<iframe>`, flex, `calc()` ou `var(--)`, toda tabela com
`role="presentation"`, toda imagem com `alt`, todo link com `target="_blank"`, nenhum
`{{...}}`, nenhum "a Optimall".

O `{{...}}` é o mais caro de errar: `{{MAIUSCULA}}` que sobrou é placeholder não preenchido,
e qualquer variável de envio é proibida enquanto a regra do sistema estiver pendente
(`design-system/newsletter/guidelines/variaveis-envio.md`).

Além disso, o `conferir` acusa cor fora da paleta, roxo de marca como texto e sobra do Podi
ou da Tacla Labs. Pendência aqui é correção antes de entregar, não item de relatório.

Relatar sempre: caminho do arquivo, **subject** (≤45 caracteres), **preheader** (60–90),
peso do HTML, componentes usados, imagens a hospedar com dimensão final (inclusive o logo,
os ícones sociais e as duas imagens de mesh — `mesh-email-topo.png` 600 × 400 e
`mesh-email-cta.png` 600 × 240), e o que ficou de fora e por quê.

Enquanto a regra de envio estiver pendente, a entrega diz, em destaque: **a regra de envio
do Optimall ainda não foi definida** — a peça saiu sem nenhuma variável, e quem for disparar
precisa conferir no sistema de envio.
