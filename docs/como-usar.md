# Como usar o Optimall Marketing OS

Guia de primeira vez. Você não precisa saber HTML nem mexer em nada técnico — precisa
saber escrever o conteúdo e organizar uma pasta. O resto é um comando.

Siga na ordem: o passo 1 instala o padrão no seu computador, e o passo 3 monta o primeiro
material.

---

> ## Se você é o Claude Code lendo este documento
>
> A pessoa acabou de te dar o link deste repositório e pediu para você prepará-lo. Faça,
> nesta ordem:
>
> 1. **Baixe o repositório** para uma pasta na máquina dela e entre nessa pasta.
> 2. **Leia o [`CLAUDE.md`](../CLAUDE.md) da raiz.** Ele é a camada global: hierarquia de
>    autoridade, regras não negociáveis e como falar com quem usa o repositório — que não
>    é uma pessoa técnica. Nunca peça comando de Git a ela.
> 3. **Reconheça as skills.** Elas já vêm no repositório, em `.claude/skills/`. Não é
>    preciso instalar nada: basta abrir o Claude Code dentro da pasta que
>    `/newsletter-optimall`, `/apresentacao-optimall`, `/post-optimall` e `/foto-optimall`
>    ficam disponíveis. Confirme que os quatro aparecem e diga isso em português.
> 4. **Confira as telas e as fotos.** Se `brand/assets/produto/` ou `brand/assets/fotos/` não
>    existirem, diga: *"as telas e fotos do produto não estão neste computador — peça a pasta
>    a quem cuida do repositório"*. O e-mail funciona sem elas; deck e post, não.
> 5. **Confirme em uma frase** que está pronto e pergunte qual material ela quer montar.
>
> Não altere `brand/`, `design-system/`, `templates/`, `.claude/skills/`, `examples/`,
> `docs/` nem o `CHANGELOG.md`. O trabalho nasce em `saida/`.

---

## O que vamos ver

1. **A primeira vez** — instalar o padrão no seu computador, uma vez só
2. **Um comando por material** — e-mail, deck, post, foto
3. **Montando um material** — da pasta de briefing à peça pronta
4. **O que ele nunca deixa passar** — as regras que protegem a marca sozinhas

---

## O problema: cada peça recomeçava do zero

Cor escolhida na hora, número de cliente que ninguém sabia de onde veio, "a Optimall" num
slide e "o Optimall" no seguinte. Nenhuma peça saía errada o bastante para alguém reclamar —
e nenhuma saía igual à anterior.

O Marketing OS existe para que a decisão de padrão seja tomada **uma vez**, e não a cada
peça.

### As quatro camadas

| Camada | O que é |
|---|---|
| **Brand** | A identidade: cor, logo, fotografia, mensagens, links fixos. Nada abaixo pode contradizer. |
| **Design System** | Como cada material se constrói: tokens, blocos prontos, checklist de QA. |
| **Templates** | O esqueleto da peça. Nunca editado por campanha. |
| **Skills** | O comando que você digita. É ele que executa tudo acima. |

Quando duas camadas discordam, **a de cima ganha** — e o Claude avisa em vez de mudar a
marca por conta própria.

---

## 1. A primeira vez

Instalar o padrão no seu computador. Leva alguns minutos, e você faz isso **uma vez só**.

**1 · Abra o Claude.** O aplicativo do Claude no seu computador.

**2 · Vá para o Claude Code.** É a parte do app que trabalha com pastas do seu computador,
e não só com conversa.

**3 · Cole o link e peça.** Cole o endereço do repositório que quem cuida dele te passou e
escreva, com essas palavras mesmo:

```
<endereço do repositório>

Instala esse repositório aqui, lê o docs/como-usar.md e deixa as skills prontas.
```

**4 · Traga as telas e as fotos.** Quem cuida do repositório te passa uma pasta com as telas
do produto e as fotos dos posts. Elas não ficam no repositório porque ele é público. Peça ao
Claude: *"coloca as telas e as fotos desta pasta no lugar certo"*.

**5 · Pronto.** Da próxima vez, você só abre essa mesma pasta.

Não estamos instalando um programa — estamos trazendo uma pasta com o padrão da marca
dentro.

### Você nunca mais faz isso

A instalação é **uma vez por computador**. Depois, é só abrir a pasta e pedir.

E antes de montar qualquer coisa, ele traz sozinho a versão mais recente do padrão — você
não precisa atualizar nada, nem saber que existe versão.

---

## 2. Um comando por material

Todos terminam com **`-optimall`**. O sufixo existe porque a ferramenta tem dezenas de
comandos próprios, e você precisa saber, na hora de digitar, qual é o da marca.

| Comando | O que faz |
|---|---|
| **`/newsletter-optimall`** | Monta o e-mail ou o informativo a partir da sua pasta de briefing. |
| **`/apresentacao-optimall`** | Monta um deck 16:9 com os slides do Figma comercial, pronto para virar PDF. Confirma o roteiro com você antes. |
| **`/post-optimall`** | Monta um post ou carrossel 1080×1350, entrega os PNGs e a legenda. Confirma o roteiro antes. |
| **`/foto-optimall`** | Escreve o prompt de uma foto de marca seguindo a direção fotográfica oficial. |

O texto de toda peça sai do guia de mensagens do Optimall
([`brand/mensagens.md`](../brand/mensagens.md)) — com os módulos, a voz e os números oficiais.

### O que ele resolve sozinho, e o que ele pergunta

| Ele pergunta antes de decidir | Ele resolve sem perguntar |
|---|---|
| Qual imagem é de qual bloco, quando o nome do arquivo não diz | Layout, hierarquia e ordem dos blocos |
| O roteiro do deck e do carrossel, antes de montar | Cor, dark mode e versão mobile do e-mail |
| O que fazer quando o briefing pede algo que não existe no padrão | Subject, preheader, legenda e o QA técnico |
| Um número que não está no guia de mensagens | O CTA *Fale com um consultor* e o link dele |

A coluna da direita é o que você deixa de fazer. A da esquerda é o que ele **não** adivinha
— e é de propósito: número errado num material comercial é pior que uma pergunta a mais.

---

## 3. Montando um material

Quatro passos, e nenhum deles é técnico.

**1 · Prepare a pasta.** Em `projects/_inbox/`, uma pasta `AAAA-MM-assunto` com o documento e
as imagens dentro.

**2 · Peça.** `/newsletter-optimall 2026-10-lancamento-clube` — ou pede em português mesmo:
*"gera a newsletter de projects/_inbox/2026-10-lancamento-clube"*.

**3 · Confira.** Ele abre no navegador e conta o que do briefing não caiu na peça, e por quê.

**4 · Entregue.** No e-mail, você recebe o arquivo, o subject, o preheader e a lista de
imagens para hospedar. No deck, o PDF. No post, os PNGs e a legenda.

### O nome do arquivo é a instrução

Esta é a parte que mais economiza retrabalho. No e-mail, o nome do arquivo diz de qual bloco
é a imagem e como ela vai ser usada.

| Nome do arquivo | Onde aparece | Proporção | Mínimo |
|---|---|---|---|
| `capa.jpg` | Abertura do e-mail | 16:9 ou mais larga | 1072 × 602 |
| `01-painel-campanha.jpg` | Topo do bloco 01 | 16:9 ou mais larga | 1072 × 604 |
| `03-clube-1x1.jpg` | Ao lado do texto | 1:1 exata | 496 × 496 |
| `foto-legal.jpg` | Sem número, ele não adivinha | — | Ele pergunta |

O guia completo de briefing e nomes está em
[`docs/como-enviar-conteudo.md`](como-enviar-conteudo.md). Leia antes do primeiro envio.

### Ele não inventa padrão

Se o conteúdo pede um bloco, uma cor ou um layout que não existe, ele monta o resto da peça
e relata a ausência no fim, marcada como **proposta**.

Proposta não vira padrão sozinha — quem decide é quem cuida do repositório. É isso que
impede o padrão de virar uma coleção de exceções.

---

## 4. As regras que ele nunca quebra

- Toda peça fala com o gestor do shopping, nunca com o consumidor final
- Texto sobre o roxo da marca é sempre branco
- O roxo, quando é texto sobre fundo claro, é a versão mais escura `#9025F4`
- O logo é tricolor, na versão certa para o fundo — nunca recolorido
- Número só entra se estiver no guia de mensagens
- Nenhuma cor escrita fora dos tokens
- Imagem fora da proporção ele relata, nunca corta sozinho
- No e-mail, nenhuma variável `{{...}}` enquanto a regra do sistema de envio estiver pendente
- No máximo 4 blocos de conteúdo por e-mail
- A marca é masculina: **o Optimall**, **do Optimall** — nunca "a"

Duas delas valem a explicação: a **regra de envio** está pendente porque o sistema que
dispara o e-mail ainda não passou as variáveis que aceita — e variável errada pode derrubar o
envio inteiro. E o **texto branco sobre o roxo** dá 4,9:1 de contraste; texto escuro em cima
dele perde leitura e foge da marca.

---

## O que já está pronto para usar

| | |
|---|---|
| **20** | blocos de e-mail prontos, do header ao rodapé legal |
| **14** | tipos de slide de apresentação |
| **7** | modelos de post |
| **4** | comandos — um por tipo de material |

Nada disso precisa ser criado de novo.

---

## Dúvidas que sempre aparecem

**"Preciso instalar alguma coisa além do Claude?"**
Não. A fonte do deck e do post vem da internet sozinha. O resto ele resolve.

**"E se eu não gostar do resultado?"**
Você pede a mudança em português. Ele remonta.

**"Posso mudar a cor de uma campanha?"**
Pode pedir — ele vai sinalizar que sai do padrão e explicar a regra. Se você confirmar, ele
faz e avisa que a peça saiu fora do padrão.

**"Como sei que estou com a versão certa do padrão?"**
Ele atualiza sozinho antes de montar. Se não conseguir, ele para e avisa — aí é falar com
quem cuida do repositório.

**"Onde fica o material que eu montei?"**
Em `saida/<nome-da-pasta>/`. É pasta local, no seu computador: não vai para o Git e não
afeta ninguém.

---

## Para continuar

- **Como enviar conteúdo:** [`docs/como-enviar-conteudo.md`](como-enviar-conteudo.md)
- **A marca:** [`brand/README.md`](../brand/README.md) · [mensagens](../brand/mensagens.md)
- **Índice das skills:** [`skills/README.md`](../skills/README.md)
- **O que mudou no padrão:** [`CHANGELOG.md`](../CHANGELOG.md)

O padrão é do time. O comando é seu.
