# Skills

As skills oficiais ficam em **`.claude/skills/`** — é a pasta que o Claude Code descobre
sozinho ao abrir o repositório. Manter uma segunda cópia aqui só criaria duas versões
divergindo, então esta pasta é apenas o índice.

| Skill | Arquivo | O que faz |
|---|---|---|
| `newsletter-optimall` | [`.claude/skills/newsletter-optimall/SKILL.md`](../.claude/skills/newsletter-optimall/SKILL.md) | Monta um e-mail ou informativo a partir de um briefing em `projects/_inbox/<slug>/` |
| `apresentacao-optimall` | [`.claude/skills/apresentacao-optimall/SKILL.md`](../.claude/skills/apresentacao-optimall/SKILL.md) | Monta uma apresentação 16:9 a partir de um briefing em `projects/_inbox/<slug>/` e gera o PDF |
| `post-optimall` | [`.claude/skills/post-optimall/SKILL.md`](../.claude/skills/post-optimall/SKILL.md) | Monta um post ou carrossel 1080×1350, exporta em PNG e escreve a legenda |
| `foto-optimall` | [`.claude/skills/foto-optimall/SKILL.md`](../.claude/skills/foto-optimall/SKILL.md) | Escreve o prompt de uma foto de marca, seguindo o Style Lock de `brand/photography/` |

## Como usar

Dentro do repositório, digite o nome da skill com barra:

```
/newsletter-optimall 2026-10-lancamento-clube
```

Ou peça em português — a skill é escolhida sozinha pela descrição.

## Em outra ferramenta de IA

Se usar Codex ou outro agente que não leia `.claude/skills/` automaticamente, aponte
para o arquivo `SKILL.md` da tabela acima junto com o `CLAUDE.md` da raiz.

## O sufixo de marca

Toda skill oficial termina em **`-optimall`**. A ferramenta de IA traz dezenas de comandos
próprios, e sem o sufixo não dá para saber, na hora de digitar, qual deles é o padrão da
marca. Skill nova nasce com o sufixo.

## Criar uma skill nova

Skill nova é recurso oficial: só maintainer cria. Ver [`docs/governanca.md`](../docs/governanca.md).
