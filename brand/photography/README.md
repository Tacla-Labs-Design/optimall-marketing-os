# Fotografia

Direção fotográfica oficial do Optimall. Faz parte de `brand/`: é a camada mais alta, e
**nada abaixo dela pode contradizê-la** — nem design system, nem template, nem skill,
nem pedido de campanha. Ver `docs/governanca.md`.

A fonte única da direção fotográfica é o [`STYLE-LOCK-OPTIMALL.md`](STYLE-LOCK-OPTIMALL.md):
luz natural de claraboia, contra-plongée, espaço negativo claro, o roxo em três valores, e um
elenco de quem vive o shopping — o cliente e quem trabalha nele (lojistas, gerentes, equipe,
gestores), em business-casual sem exagero. Este arquivo só diz como ler o Style Lock.

---

## As duas regras que quebram tudo se forem ignoradas

1. **Leia o Style Lock antes de escrever qualquer prompt de imagem.** Não gere de memória,
   nem numa conversa longa em que o arquivo já "passou" antes — ele pode ter mudado.
2. **O bloco `STYLE LOCK` (§4.A interior · §4.B outlet) se copia byte a byte.** Nunca
   parafraseie, resuma, reordene ou "melhore" uma palavra. Ele existe justamente para não
   variar: é o que faz duzentas imagens geradas ao longo de meses parecerem do mesmo ensaio.
   A **única** substituição autorizada é a frase da lente para 35mm, documentada na §4.A.

## O que é normativo e o que é ferramenta

| Seção | Papel |
|---|---|
| §1 DNA fotográfico · §2 Tradução para o interior · §4 blocos STYLE LOCK · §6 Checklist · §8 Roxo | **Normativo.** É a diretriz de marca. Só o maintainer altera. |
| §3 Fórmula de slots · §5 Suíte de variações · §7 Prompt único · §2.8–2.10 negative por gerador | **Ferramenta de execução.** Ajuda a montar o prompt; não redefine a direção. |

## O roxo dentro da foto

O roxo **`#9934FF`** (`brand/README.md`) está resolvido dentro do Style Lock como
`vivid violet purple` / `deep royal purple` / `soft lavender` — a tradução dele para o
vocabulário que os geradores entendem. Não são hexadecimais alternativos e não se trocam por
campanha.

**Isto não conflita com as regras de cor do layout.** Lá, o `#9934FF` é fundo, ícone e
grafismo, e o roxo de texto é o `#9025F4`. Aqui, o roxo é figurino, objeto e brilho de tela
dentro da foto — outro eixo, outra regra.

## Imagens de referência

O Optimall **ainda não tem imagens de referência aprovadas**. Até ter, a direção inteira está
no texto do Style Lock. Quando o maintainer aprovar as primeiras imagens, elas passam a valer
como `--sref` (Midjourney) e como imagem de entrada (Gemini / Nano Banana) — e só elas: imagem
de outra paleta puxa a cor junto.

## Tela de produto não se gera

Painel, dashboard e app do Optimall saem da foto como um glow roxo ilegível. A tela real entra
na montagem da peça, a partir de `brand/assets/produto/` — pasta local, fora do Git, porque o
repositório é público.

## Como se usa na prática

O procedimento — enquadrar o pedido, montar o prompt, escolher parâmetros por gerador,
arquivar o que foi entregue — está na skill **`/foto-optimall`**
([`.claude/skills/foto-optimall/SKILL.md`](../../.claude/skills/foto-optimall/SKILL.md)).

A divisão é a de sempre: este arquivo define **o que é permitido visualmente**, a skill
ensina **como executar**. A skill referencia o Style Lock; nunca copia trechos dele.
