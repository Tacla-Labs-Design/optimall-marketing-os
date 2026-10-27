# Layout e ritmo do deck

## O princípio

**Uma ideia por slide.** Se o slide precisa de duas frases para explicar do que ele trata,
são dois slides. Deck bom não é deck curto — é deck onde cada slide tem um trabalho só.

Quem lê está a metros da tela e tem 30 segundos por slide. Tudo aqui existe por causa disso.

## Hierarquia dentro de um slide

```
tag              o assunto, 16px caixa alta       (opcional: "MÓDULO", "WHITE LABEL")
    ↓
título           a ideia, 72px                    (obrigatório, exceto capa e fecho)
    ↓
régua            400 × 4px, roxo → transparente   (a pausa antes do conteúdo)
    ↓
conteúdo         cards, números, lista, tela do produto
    ↓
rodapé           fonte do dado · número do slide
```

A régua não é enfeite: ela é o intervalo que separa o título do conteúdo sem gastar mais
40px de espaço vertical.

## Ritmo do deck

- **Capa → prova → problema → plataforma → módulos → encerramento.** É a ordem do deck
  comercial. Um divisor (`12-titulo-texto--roxo`) a cada 4 a 6 slides num deck longo.
- **Alternar o campo de cor.** Roxo, roxo, roxo cansa; claro, claro, claro vira relatório.
  `slide--claro`, `slide--claro-2` e `slide--branco` dão respiro; o roxo marca a virada.
- **Uma tela de produto a cada 3 ou 4 slides**, no mínimo. Deck do Optimall sem o produto
  na tela vira promessa.
- **Nunca o mesmo modelo de módulo três vezes seguidas.** Repetir o mesmo layout faz a
  plateia achar que voltou o slide.

## Limites

| | Limite | Por quê |
|---|---|---|
| Slides no deck | 20 | Acima disso ninguém termina a apresentação |
| Palavras num slide | ~60 | Slide não é documento |
| Cards numa grade | 4 | O quinto card encolhe o texto abaixo do piso de 24px |
| Números num slide | 4 | Mais que isso e nenhum é lembrado |
| Itens numa lista | 12 | É o que cabe em duas colunas sem apertar |
| Linhas numa tabela | 6 | Tabela maior não se lê projetada |

Estourou um limite: o conteúdo vira dois slides. Nunca fonte menor, nunca margem menor.

## O roxo é campo, o branco é estrutura

O campo de cor não organiza nada sozinho. **Quem constrói a hierarquia visual são os cards
brancos** e as telas do produto. Um slide roxo com texto solto em cima parece um aviso; um
slide com cards e tela parece o produto.

Exceções legítimas: capa, divisor de seção e encerramento — os slides que existem para
respirar, não para informar.

## De onde isto veio

Os slides vêm da *Apresentação Comercial 2026*, no Figma, aprovada pelo time do Optimall. O
padrão **descreve o que já existia**; não inventou direção nova. Os dois derivados (`12` e
`13`) usam só peças que já estão nos outros slides.
