# Optimall Marketing OS

O lugar onde ficam guardados os **padrões oficiais do Optimall** para criação de materiais de
Marketing, Design e Publicidade — cores, componentes, modelos e as instruções que a IA segue
para montar tudo isso.

A ideia é simples: você traz o conteúdo, a IA monta o material já dentro do padrão da
marca. Ninguém precisa lembrar de cor, tamanho de fonte ou regra de rodapé.

O **Optimall** é a plataforma B2B dos shoppings — Campanhas, Aplicativo, Clube de Benefícios
e CRM, com a marca de cada empreendimento. Toda peça fala com **quem decide no shopping**,
nunca com o consumidor final.

---

## Para quem é

Para o time de Marketing, Design e Publicidade do Optimall.

**Não é preciso saber programar.** Você escreve o conteúdo e organiza as imagens; a IA faz
o resto. Se em algum momento uma resposta pedir que você mexa no repositório, algo saiu do
lugar — avise quem cuida do padrão.

---

## O que existe hoje

| Material | Comando | Situação |
|---|---|---|
| **Newsletter / e-mail** | `/newsletter-optimall` | Completo — design system, blocos na paleta do Optimall, modelo e QA |
| **Apresentação / deck** | `/apresentacao-optimall` | Completo — 14 tipos de slide, dos modelos do Figma. Exporta PDF |
| **Post / carrossel** | `/post-optimall` | Completo — 7 modelos 1080×1350, PNG e legenda prontos |
| **Foto de marca** | `/foto-optimall` | Completo — direção fotográfica (Style Lock) e skill que escreve o prompt |
| Outros materiais | — | Ainda não. A estrutura já está preparada para receber |

> Deck e post usam a fonte **Halyard Text**, que vem da web pelo kit do Adobe Fonts do
> Optimall: não precisa instalar nada, mas precisa de internet para exportar.

> As **telas do produto** e as **fotos dos posts** não ficam neste repositório, que é público.
> Peça a pasta a quem cuida do repositório antes de montar deck ou post.

---

## Como usar

Primeira vez aqui? Comece por [`docs/como-usar.md`](docs/como-usar.md) — é o guia do zero ao
primeiro material montado.

**1. Monte a pasta do envio** em `projects/_inbox/`, com o documento de textos e as imagens.
O guia completo é o [`docs/como-enviar-conteudo.md`](docs/como-enviar-conteudo.md) — leia
antes do primeiro envio, ele explica como nomear as imagens.

**2. Peça a montagem.** Dentro do repositório:

```
/newsletter-optimall 2026-10-lancamento-clube
```

Ou simplesmente, em português:

> "Gera a newsletter de `projects/_inbox/2026-10-lancamento-clube`"

**3. Confira o resultado** em `saida/<nome-da-pasta>/`. Essa pasta é sua e fica só no seu
computador.

Para ver o e-mail com as imagens carregando, rode:

```bash
python3 -m http.server 4321
```

e abra `http://localhost:4321/saida/<nome-da-pasta>/index.html`.

Antes de aprovar um e-mail, teste a renderização real via Litmus / Email on Acid ou um
disparo de teste pela própria ferramenta de envio.

---

## Como o projeto está organizado

```
brand/               A identidade do Optimall — logo, cores, tom de voz, mensagens, links
design-system/       Como cada tipo de material se constrói: cores, componentes, regras
templates/           Os modelos em branco
examples/            Materiais prontos, para ver como fica
projects/_inbox/     Onde você deixa o conteúdo que quer transformar em material
saida/               Onde o material montado aparece — fica no seu computador
docs/                Os guias
skills/              Índice das instruções que a IA segue
```

Mapa detalhado: [`docs/estrutura.md`](docs/estrutura.md).

---

## O que é oficial

Tudo em **`brand/`, `design-system/`, `templates/`, `examples/`, `docs/` e as skills** é
recurso oficial. É o padrão da marca.

**`projects/_inbox/` e `saida/` são seus.** Ficam no seu computador, não vão para lugar
nenhum e não afetam ninguém.

Uma campanha específica **não altera** o padrão. Se ela precisar de algo que não existe, a
IA vai apontar isso como uma **proposta** — e a decisão de virar padrão é de quem mantém o
repositório.

---

## Governança

Neste momento (MVP), **o único maintainer é Bruno Pinheiro** — responsável por Design,
Produto e Marketing.

- Qualquer pessoa pode **usar** o Marketing OS para criar materiais.
- Ninguém deve **alterar** brand, design system, templates ou skills diretamente.
- Futuramente outros colaboradores autorizados poderão ser adicionados.

O controle é feito pelo Git: só quem tem permissão de escrita altera o repositório oficial.
Não há nenhum sistema de senha ou login dentro do projeto.

Detalhes: [`docs/governanca.md`](docs/governanca.md).

---

## Como propor uma mudança

Não mexa nos arquivos oficiais. Em vez disso:

1. Monte o material do jeito que der com o que existe hoje.
2. Anote o que faltou — e a IA já faz isso sozinha no relatório final.
3. Mande isso para o maintainer, em uma frase: *o que faltou, onde seria usado, por quê*.

Se for aprovado, o recurso entra no padrão e no
[`CHANGELOG.md`](CHANGELOG.md) — que é o que o time lê para saber o que mudou.

---

## Como adicionar um recurso novo (maintainer)

1. Colocar o recurso na camada certa: identidade → `brand/`; regra visual ou componente →
   `design-system/<material>/`; modelo em branco → `templates/<material>/`; procedimento
   que a IA segue → `.claude/skills/<skill>/SKILL.md`.
2. Documentar no README da própria pasta.
3. Escrever a entrada no `CHANGELOG.md` **na mesma leva** — com o porquê, e com
   `**Ação necessária:**` se algo já montado precisar ser revisto.

O repositório é **público**: tela do produto, foto de banco, dado de cliente, briefing e
credencial nunca entram em arquivo versionado.

---

## Como usar com IA

O contexto geral fica em [`CLAUDE.md`](CLAUDE.md) — o Claude lê sozinho a cada sessão, não
precisa colar as regras no pedido. As instruções específicas de cada material ficam nas
skills, em [`skills/README.md`](skills/README.md).

Funciona no Claude Code sem configuração. Em outra ferramenta (Codex, por exemplo),
aponte para o `CLAUDE.md` e para o `SKILL.md` do material.

---

## Referência rápida

- **A marca:** [`brand/README.md`](brand/README.md) · [mensagens](brand/mensagens.md) · [links oficiais](brand/links-oficiais.md)
- **Logo pack e guia visual:** logo, símbolo e assinatura em SVG e PNG, com as regras de uso, em [marcas.taclalabs.workers.dev/optimall/guia/](https://marcas.taclalabs.workers.dev/optimall/guia/) (botão para baixar o .zip)
- **Newsletter:** [`design-system/newsletter/README.md`](design-system/newsletter/README.md) · [componentes](design-system/newsletter/components/README.md)
- **Apresentação:** [`design-system/apresentacao/README.md`](design-system/apresentacao/README.md)
- **Post:** [`design-system/post/README.md`](design-system/post/README.md)
- **Fotografia:** [`brand/photography/README.md`](brand/photography/README.md)
- **Como usar, do zero:** [`docs/como-usar.md`](docs/como-usar.md)
- **Como enviar conteúdo:** [`docs/como-enviar-conteudo.md`](docs/como-enviar-conteudo.md)
- **Mudanças no padrão:** [`CHANGELOG.md`](CHANGELOG.md)
