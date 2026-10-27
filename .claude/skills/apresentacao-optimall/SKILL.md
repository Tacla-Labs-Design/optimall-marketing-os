---
name: apresentacao-optimall
description: Monta uma apresentação, deck, pitch ou slide do Optimall (B2B, para gestores de shopping) em 16:9 a partir de um briefing em projects/_inbox/<slug>/, seguindo o design system de apresentação. Use quando pedirem para gerar, montar ou criar uma apresentação, um deck, um pitch, um slide ou um PowerPoint do Optimall.
---

# Montar uma apresentação do Optimall

Argumento: o slug da pasta em `projects/_inbox/`. Sem argumento, listar as pastas
disponíveis e perguntar qual. Se não houver briefing em pasta nenhuma, o assunto pode vir
direto da conversa — mas o roteiro (§2) continua obrigatório.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e valem
integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md`, `links-oficiais.md`, `marca.json` | Identidade, contraste, logo, CTA e contatos fixos |
| Brand | `brand/mensagens.md` | O que dizer: números oficiais, módulos, voz, frases aprovadas |
| Brand | `brand/photography/STYLE-LOCK-OPTIMALL.md` | Direção fotográfica — só quando a peça pedir **foto nova** |
| Design System | `design-system/apresentacao/` | Tokens, os 14 tipos de slide, canvas, ritmo, QA |
| Template | `templates/apresentacao/base.html` | O shell |

Em caso de conflito, a camada mais alta prevalece. Ver `docs/governanca.md`.

O deck do Optimall é **sempre B2B**: fala com quem decide no shopping. Sempre "o Optimall",
nunca "a Optimall". **Não cita o Podi nem a Tacla Labs** — nem no texto, nem no `alt`, nem
em imagem.

## 0. Atualizar o padrão

Antes de qualquer coisa, e **sem perguntar nada ao usuário**:

```bash
./scripts/check-atualizacao.sh --atualizar
```

Quem usa este comando não é pessoa técnica (`CLAUDE.md`). Não peça para ela rodar Git:
o script já traz a versão nova sozinho.

- **Saída 0** → seguir. Se o script disse que atualizou, mencione em uma linha, em
  português comum: *"Atualizei o padrão para a versão mais recente antes de montar."*
  Se não atualizou nada, não comente.
- **Saída 1** → houve alteração local conflitante. **Parar.** Dizer que esta cópia do
  padrão está diferente da oficial e que é preciso avisar quem cuida do repositório.

## 1. Ler tudo antes de decidir qualquer coisa

```bash
ls -R projects/_inbox/<slug>/
```

- `.docx` → `textutil -convert txt -stdout arquivo.docx`
- `.pdf` → `pdftotext arquivo.pdf -`
- `.pptx` → `textutil -convert txt -stdout arquivo.pptx`, e **abrir as imagens** que vierem
- `.zip` → `unzip -o arquivo.zip -d projects/_inbox/<slug>/imagens/`
- Imagens → **abrir de fato** com a tool Read. Nome de arquivo não é prova de conteúdo, e
  você precisa da proporção real para escolher o slide.

Antes de montar, saber três coisas. Se o briefing não disser, **perguntar**:

1. **Para quem** — shopping prospect, shopping cliente, evento do setor, ou time interno.
2. **Quanto tempo** — 5 minutos são ~8 slides; 20 minutos, ~20. É o teto de slides.
3. **Qual é o pedido** — o que a plateia deve fazer no fim. É o `11-encerramento`.

Todo texto sai de `brand/mensagens.md` — números só os oficiais de lá, CTA *Fale com um
consultor*. Número do briefing que não está lá **não entra**: relate no fim.

## 2. Definir o roteiro — e confirmar antes de montar

Escreva o roteiro como uma lista: **número, tipo de slide, o que ele diz em uma frase.**

```
01  00-capa                   Optimall para o Shopping X
02  01-numeros-clientes       a prova: números oficiais e quem já usa
03  02-problema               o shopping não sabe quem entra
04  03-plataforma-modulos     a plataforma em uma tela
...
NN  11-encerramento           fale com um consultor
```

O tipo se escolhe pelo **formato da informação**, não pela vontade de variar — a tabela de
decisão está em `design-system/apresentacao/README.md`. O fecho é sempre o `11-encerramento`.

**Mostre o roteiro e espere a pessoa confirmar antes de montar.** Deck errado é caro:
refazer 18 slides depois de prontos é o dobro do trabalho de discordar de uma lista.

Respeite os limites de `design-system/apresentacao/guidelines/layout-ritmo.md` — 20 slides,
~60 palavras por slide, 4 cards por grade, um divisor a cada 4 a 6 slides num deck longo.

## 3. Montar

1. Copiar `templates/apresentacao/base.html` para **`saida/<slug>/index.html`** e trocar o
   `{{TITULO_DA_APRESENTACAO}}` do `<title>`.
2. Copiar os slides escolhidos de `design-system/apresentacao/slides/` para dentro do
   `<div class="deck">`, na ordem do roteiro. Os slides já trazem o texto aprovado do deck
   comercial: num deck comercial padrão, boa parte fica como está. Num deck sob medida, trocar
   o texto pelo do roteiro, mantendo o formato. Depoimento (`{{DEPOIMENTO}}`, `{{NOME}}`,
   `{{CARGO_E_EMPREENDIMENTO}}`) só entra real e autorizado.
   Nunca gravar em `examples/` — aquilo é acervo curado.
3. Criar `saida/<slug>/assets/` e colocar ali **todas** as imagens, **achatadas**, com o nome
   que o slide usa: as do briefing e as fixas de `brand/assets/` (`produto/`, `clientes/`,
   `parceiros/`, `grafismos/`, `fotos/`). O deck precisa abrir sozinho se alguém mandar a pasta.

   As telas do produto (`produto/`) e as fotos (`fotos/`) **não vêm com o padrão**: ficam numa
   pasta local. Antes de usar slide que tenha tela ou foto (`03` a `09`):

   ```bash
   ls brand/assets/produto brand/assets/fotos
   ```

   Se faltar, **parar** e dizer: *"as telas e fotos do produto não estão neste computador —
   peça a pasta a quem cuida do repositório"*. Não montar com tela de outro lugar nem deixar
   o slot vazio.
4. Trocar os `<svg>` genéricos dos chips pelo glifo certo do assunto (HugeIcons bulk de
   `brand/assets/icones-ui/`), mantendo `currentColor`.
   O **logo não é imagem**: é o `<symbol>` que já vem no template, tricolor —
   `#logo-optimall-branco` sobre roxo, `#logo-optimall` sobre claro, `#simbolo-optimall`
   como selo. Nunca trocar por PNG, nunca recolorir, nunca `filter`.
5. **Nunca escrever cor solta.** Toda cor sai de `design-system/apresentacao/tokens.md`, por
   `var(--token)`.
6. **Texto sobre o roxo é sempre branco.** Roxo como texto sobre fundo claro é `--roxo-texto`.
7. Numerar os slides no rodapé e conferir se o CTA é o `links.cta` de `brand/marca.json`.
8. A fonte é a **Halyard Text**, que o template já carrega do kit do Adobe Fonts. Nenhuma outra.

Proporção de imagem fora do esperado: **não distorça e não corte por conta própria.**
Monte o resto e relate no fim — qual arquivo, qual proporção veio, qual era esperada.

## 4. A rota `/design`

Quando a pessoa quiser **editar o visual à mão** em vez de receber o HTML pronto, o mesmo
conteúdo vai para o comando `/design` do Claude, como artboards de **1920 × 1080**.

O que não pode escapar: **o `/design` não decide nada de identidade.** Ele recebe as
decisões prontas. Ao chamar, passe no briefing do canvas, explicitamente:

- Os tokens de `design-system/apresentacao/tokens.md` — **os hex**, não os nomes.
- Canvas 1920 × 1080, margem de segurança de 64px.
- Halyard Text e a escala tipográfica inteira do `tokens.md`.
- As regras de contraste: texto sobre o roxo `#9934FF` é **sempre branco**; roxo como texto
  sobre fundo claro é `#9025F4`.
- O logo em SVG (`brand/assets/header/`): branco sobre roxo, colorido sobre claro. Nunca
  recolorido.
- O roteiro do §2, com o tipo de slide de cada artboard.

Se o canvas voltar com cor, fonte ou logo fora do sistema, **é o canvas que se corrige**,
não o design system.

As duas rotas convivem: o HTML em `saida/<slug>/index.html` continua sendo a versão
canônica e a que vira PDF. Rodar as duas para o mesmo deck é normal.

## 5. Quando falta algo no sistema

Se o conteúdo pede um tipo de slide, uma cor ou um layout que não existe (agenda, timeline,
tabela, comparativo):

1. **Não invente.** Não crie uma cor nova, não improvise um slide com CSS solto.
2. Verifique se um dos 14 tipos resolve com outro conteúdo.
3. Se realmente não resolve, monte o resto do deck e **relate a ausência no fim**, marcada
   explicitamente como **proposta**: o que falta, em qual slide seria usado, o que sugere.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer (`docs/governanca.md`).

Se o briefing pedir uma **fotografia que ainda não existe**, a direção visual não se
inventa: ela está em `brand/photography/STYLE-LOCK-OPTIMALL.md`. Relate o que falta e aponte o
Style Lock — ou monte o prompt com `/foto-optimall`. Tela de produto não se gera: entra a
tela real.

Se o pedido conflita com o brand — outra cor, texto escuro sobre o roxo, logo recolorido,
falar com o consumidor final — **sinalize o conflito** em vez de alterar a identidade.
Explique a regra em uma frase e ofereça a alternativa que respeita o sistema. Se a pessoa
reafirmar, é decisão dela: diga que a peça sai fora do padrão e siga.

## 6. QA e entrega

Rodar `design-system/apresentacao/guidelines/qa-checklist.md` inteiro antes de dizer que
está pronto. Os itens verificáveis por comando:

```bash
python3 -I scripts/conferir.py saida/<slug>/index.html   # saída 0, e "N slides" = o roteiro
```

Ele lê a peça sem os comentários e confere: nenhum `{{...}}`, toda imagem com `alt` e dentro
de `assets/`, cor só da paleta, nada do Podi nem da Tacla Labs, nenhum "a Optimall" — e diz
quantos slides há.

Gerar o PDF:

```bash
python3 -I scripts/exportar.py pdf saida/<slug>/index.html   # → saida/<slug>/<slug>.pdf
```

Se ele disser que a fonte não carregou, dizer em português comum: *"a fonte do Optimall
(Halyard Text) não carregou — confira a internet e me avise para gerar de novo"*. Não gerar
com outra fonte.

Depois abrir o PDF (ou a peça no navegador) e conferir de olho: nenhum slide cortado, nada
fora da margem, o PDF sai em paisagem com um slide por página.

Relatar sempre: caminho do arquivo, **quantos slides e quais tipos**, imagens a substituir
com a dimensão final, onde está o PDF, e **o que do briefing não coube no padrão** — dizendo
explicitamente o que ficou de fora e por quê.
