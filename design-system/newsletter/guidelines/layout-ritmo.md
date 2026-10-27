# Layout e ritmo visual

Como uma newsletter do Optimall se organiza. As restrições técnicas estão em
[`email-compat.md`](email-compat.md); aqui é a intenção de design.

## O princípio

**Página e container têm a mesma cor** (`#FAF5FF`). O container não se destaca do fundo
— quem constrói a estrutura visual são os **cards brancos**, com raio de 20px.

## Hierarquia dentro de um bloco

```
eyebrow / tag (opcional)
    ↓
headline centralizada, 28–32px semibold
    ↓
texto de apoio, 16px
    ↓
CTA pill
```

## Ritmo da peça

Alternância: bloco de card claro → imagem full-bleed → bloco de card claro.

Blocos de artigo alternam imagem à esquerda e à direita no desktop. **No mobile, sempre
imagem acima do texto.**

## Limites

- Máximo de **2 pesos tipográficos** por e-mail (regular + semibold).
- Máximo de **4 seções de conteúdo**. Acima disso, cortar ou dividir em dois envios.
- **Um CTA primário por seção.** Links secundários em texto com seta `→`, na cor
  `accent-ink` (`#9025F4`).

## CTA

- **Primário:** roxo de marca, variante A do `components/_button.html`, sempre com
  texto `#FFFFFF`. Nunca texto escuro sobre o roxo. No Optimall o CTA principal é
  *Fale com um consultor* (`brand/marca.json` → `links.cta`).
- **Secundário:** CTA neutro escuro, variante B — e só ele leva a classe `.dm-btn`
  para inverter no dark mode.
