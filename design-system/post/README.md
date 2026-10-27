# Design System — Post

Posts de rede social do Optimall: **feed 4:5, 1080 × 1350**, sozinhos ou em carrossel. Saem em
PNG, um por card, prontos para subir no Instagram e no LinkedIn.

```
tokens.md            Cor, tipografia, grafismos do post
posts/               Os 7 modelos, um <section class="post"> por arquivo
guidelines/
  ├── canvas.md        O canvas fixo, a margem de segurança, o export em PNG
  ├── carrossel.md     Como um carrossel se organiza: capa, miolo, fecho
  ├── legenda.md       O texto que acompanha o post (legenda, CTA, hashtags)
  └── qa-checklist.md  Checklist obrigatório antes de entregar
```

Shell de montagem: `templates/post/base.html`. Procedimento: `/post-optimall`.

## Autoridade

Obedece ao [`brand/`](../../brand/README.md) e não pode contradizê-lo. Cor, logo, fonte e voz
são da marca; aqui só são aplicados a um canvas de 1080 × 1350.

## O que é específico de post

- **O canvas é fixo** e pequeno na tela do celular. Um post tem uma mensagem; o que não cabe
  vira outro card do carrossel — nunca fonte menor.
- **A leitura é de passagem.** A pessoa decide em um segundo se para. Título grande, pouca
  palavra, imagem de produto ou pessoa que se entende sem legenda.
- **Pode usar CSS moderno** (flex, grid, `var()`, degradê, `backdrop-filter`). Abre no Chrome
  para exportar, não num cliente de e-mail.
- **O texto longo mora na legenda**, não na arte (`guidelines/legenda.md`).

## Modelos

Os 7 modelos do Figma *Social Media – Optimall* (seção "posts aprovados"). Cada arquivo é um
`<style>` + um `<section class="post">` de 1080 × 1350 — **se copia** para dentro de
`templates/post/base.html`. Tokens: [`tokens.md`](tokens.md). Regras: [`guidelines/`](guidelines/).

Os modelos vêm com o texto aprovado do Figma (com "o Optimall" e os números oficiais). Os
únicos `{{PLACEHOLDER}}` são os de depoimento — depoimento só entra real, com nome e cargo.

| Arquivo | O que é | Fundo |
|---|---|---|
| `posts/01-foto-titulo.html` | Foto recortada, título e subtítulo no canto, ícones subindo do celular | Lavanda |
| `posts/02-grade-recursos.html` | Título com destaque desenhado + 4 cards de vidro com ícone | Roxo |
| `posts/03-mockup-painel.html` | Logo e site no topo, título, tela do painel sangrando | Roxo em degradê |
| `posts/04-citacao.html` | Depoimento em painel de vidro escuro | Lavanda + vidro |
| `posts/05-modulos-orbita.html` | "Tudo em 1 plataforma": ícones em órbita do símbolo + painel | Claro |
| `posts/06-foto-faixa-cta.html` | Foto grande, faixa roxa com destaque e lista, pílula de CTA | Lavanda |
| `posts/07-depoimento-foto.html` | Foto grande com card roxo de depoimento | Lavanda |

## Como escolher

| A informação é… | Modelo |
|---|---|
| Uma promessa, com gente | `01-foto-titulo` |
| 3 ou 4 coisas de peso igual (modalidades, módulos, benefícios) | `02-grade-recursos` |
| O produto em tela | `03-mockup-painel` |
| Uma prova em pessoa, sem foto | `04-citacao` |
| A plataforma inteira / tudo integrado | `05-modulos-orbita` |
| Um convite (seja cliente, fale com a gente) com lista de benefícios | `06-foto-faixa-cta` |
| Uma prova em pessoa, com foto | `07-depoimento-foto` |

## No carrossel

| Posição | Modelos que funcionam |
|---|---|
| Capa | `01`, `03`, `05` |
| Miolo | `02` (um card por recurso, repetido), `03` (uma tela por passo), `04`/`07` |
| Fecho | `06` (CTA) |

Estrutura e limites em [`guidelines/carrossel.md`](guidelines/carrossel.md).

## Imagens

Na montagem, copiar de `brand/assets/` (`fotos/`, `produto/`, `grafismos/`) para
`saida/<slug>/assets/`, achatado. `fotos/` e `produto/` não vêm com o padrão: ficam numa pasta
local, entregue por quem cuida do repositório. Os modelos `01`, `03`, `05`, `06` e `07` usam
foto ou tela.

Foto nova: mesma proporção do slot e Style Lock do Optimall (`/foto-optimall`). Tela nova de
produto: PNG transparente, na proporção da que substitui.

Não existe (ainda): story 9:16 e quadrado 1:1 — proposta.

## Alterar isto

Só maintainer. Ver [`docs/governanca.md`](../../docs/governanca.md).
