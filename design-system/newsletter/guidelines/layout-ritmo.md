# Layout e ritmo visual

Como uma newsletter do Optimall se organiza. As restrições técnicas estão em
[`email-compat.md`](email-compat.md); aqui é a intenção de design.

## O princípio

**Página branca, conteúdo solto, alinhado à esquerda.** Container e página têm a mesma cor
(`#FFFFFF`). O que estrutura a peça é:

- o **topo com gradient mesh** claro — logo, título da edição grande, data e a imagem de
  abertura entrando no degradê;
- **títulos de seção grandes** (30px) com **linha fina** entre as seções;
- **painéis** de raio 20px em volta das imagens (lavanda para arte e recorte, `#F9F8FC` para
  print de tela), com o texto solto embaixo;
- a **faixa de CTA em mesh roxo** fechando o conteúdo, e o **rodapé na faixa lavanda**.

Não há card branco em volta do conteúdo. O único card é o `13-card-conteudo`, com borda.

## Hierarquia da peça

```
logo
    ↓
título da edição, 46px (no mesh)        ← "Clube de Benefícios", "Novidades do Optimall"
    ↓
data / subtítulo
    ↓
imagem de abertura
    ↓
headline de abertura, 26px + texto 16px
    ↓  ─── linha fina ───
título de seção, 30px
    ↓
painel com imagem → título 20px → texto 15px     (repete, 40px entre itens)
    ↓
faixa de CTA: título 26px branco, frase, botão branco
```

## Ritmo

- Topo → headline de abertura: 36px.
- Entre seções: linha fina (`10-divider`) com 40px em cima e embaixo, depois o `02b`.
- Entre itens de uma seção: 40px. Imagem do painel → título do item: 20px.
- Último bloco → faixa de CTA: 40px. Da faixa em diante, nada de espaçador.

Blocos de artigo (`07`) alternam imagem à esquerda e à direita no desktop. **No mobile,
sempre imagem acima do texto**, e o texto continua à esquerda.

## Limites

- Máximo de **2 pesos tipográficos** por e-mail (regular + semibold).
- Máximo de **4 seções de conteúdo**. Acima disso, cortar ou dividir em dois envios.
- **Um CTA por peça**, na `89-faixa-cta-mesh`. Links secundários de artigo (quando o briefing
  traz) em texto com seta `→`, na cor `accent-ink` (`#9025F4`).

## CTA

- **Na faixa de CTA:** botão branco com texto `accent-ink`, variante C do
  `components/_button.html` — já montado na `89`.
- **Primário fora da faixa** (peça sem a `89`, como o `13-card-conteudo`): roxo de marca,
  variante A, sempre com texto `#FFFFFF`. Nunca texto escuro sobre o roxo. No Optimall o CTA principal é
  *Fale com um consultor* (`brand/marca.json` → `links.cta`).
- **Secundário:** CTA neutro escuro, variante B — e só ele leva a classe `.dm-btn`
  para inverter no dark mode.
