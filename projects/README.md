# projects/ — o trabalho, separado dos recursos oficiais

O Marketing OS guarda os **recursos oficiais** do Optimall: brand, design system, templates,
skills. Um material específico — uma campanha, um deck, um envio — **não é** recurso oficial
e não altera nenhum deles.

```
projects/
└── _inbox/          ENTRADA — briefing e imagens que o time manda (fica no seu computador)

saida/               SAÍDA — o material montado (fica no seu computador)
```

Nenhuma das duas vai para o repositório. O que você monta é seu, local, e não sobrescreve
o trabalho de ninguém.

## Entrada: `projects/_inbox/`

Uma pasta por material:

```
projects/_inbox/2026-10-lancamento-clube/
├── brief.docx          (ou .md / .txt / .pdf — o material bruto, do jeito que veio)
└── imagens/            (ou imagens.zip — o Claude descompacta)
    ├── capa.jpg                 → abertura do e-mail       (16:9, ≥1072px)
    ├── 01-pontos-clube.jpg      → bloco 01, topo          (16:9, ≥1072px)
    └── 02-crm-1x1.jpg           → bloco 02, lateral       (1:1, ≥496×496)
```

Nome da pasta: `AAAA-MM-<assunto>`. Exemplos: `2026-10-lancamento-clube`,
`2026-11-deck-grupo-norte`, `2026-11-carrossel-campanhas`.

> **Guia completo para quem escreve:** [`docs/como-enviar-conteudo.md`](../docs/como-enviar-conteudo.md)
> — e-mail, deck e post: formato do documento, nomes de arquivo e proporções. Leia antes do
> primeiro envio.

## Como pedir a montagem

```
/newsletter-optimall 2026-10-lancamento-clube
/apresentacao-optimall 2026-11-deck-grupo-norte
/post-optimall 2026-11-carrossel-campanhas
```

ou, em português mesmo:

> "Gera a newsletter de `projects/_inbox/2026-10-lancamento-clube`"

## O que ajuda no briefing

- Objetivo da peça em uma frase
- Público: que cargo, que tipo de empreendimento (é sempre B2B)
- Data de envio ou da reunião
- Textos já aprovados (se houver) ou os fatos brutos — números só os de `brand/mensagens.md`
- O que a pessoa deve fazer depois de ver (o CTA padrão é *Fale com um consultor*)

## Se a campanha precisar de algo que não existe

Um projeto **não altera** o design system, o template nem a skill. Se o material pede
um bloco ou uma cor que não existe, isso vira uma **proposta de evolução do sistema** —
ver [`docs/governanca.md`](../docs/governanca.md).
