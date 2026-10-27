# Design System — Newsletter

O sistema visual das newsletters e e-mails do Optimall.

```
tokens.md        Cor, tipografia, espaçamento, dark mode, tamanhos de imagem
components/      Os 21 blocos de HTML de e-mail (com a moldura de conteúdo) + o botão VML
guidelines/
  ├── email-compat.md   Regras técnicas de HTML de e-mail (não negociáveis)
  ├── layout-ritmo.md   Hierarquia, ritmo da peça, limites de CTA e de seções
  ├── variaveis-envio.md O que o sistema de envio aceita e por que não há descadastro
  └── qa-checklist.md   Checklist obrigatório antes de entregar
```

## Autoridade

Este design system **obedece** ao [`brand/`](../../brand/README.md) e não pode contradizê-lo.
A regra de contraste do roxo de marca nasce lá; aqui ela só é aplicada.

## O que é específico de e-mail

Quase tudo em `guidelines/email-compat.md` e a tabela de tamanhos de imagem em `tokens.md`
existem por causa das limitações dos clientes de e-mail. Não servem para outro material.

**O que sobreviveria a outro suporte:** a paleta e a regra de contraste, os papéis
tipográficos (não os px de e-mail), a escala de espaçamento, o raio de 20px do card e o
princípio "cards brancos estruturam, fundo não se destaca".

A fonte do e-mail é a **Inter**, não a Halyard Text do deck e do post: o kit web da Halyard
não carrega na maioria dos clientes de e-mail (Gmail e Outlook ignoram), e a peça sairia
com letras diferentes em cada caixa de entrada.

## Alterar isto

Só maintainer. Ver [`docs/governanca.md`](../../docs/governanca.md).
