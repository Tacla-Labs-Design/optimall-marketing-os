# Changelog

Mudanças no padrão — templates, tokens, regras e assets fixos.

Mantido pelo dono do repositório. Quem monta material lê para saber o que mudou desde a
última peça; as skills avisam quando a cópia local está atrás.

**Ação necessária** marca o que exige refazer ou revisar algo já montado. O resto
entra sozinho na próxima peça.

---

## 2026-10-27 — Repositório próprio do Optimall

O Optimall passa a ter um Marketing OS só dele: identidade, design system, templates e skills
de uma marca só, sem passo de escolha de marca e sem nada que não seja do Optimall. O
repositório é **público** — por isso algumas pastas ficam fora dele (abaixo).

### O que tem

- **Brand** (`brand/`): identidade; tipografia Halyard Text, carregada pelo kit web do Adobe
  Fonts (não precisa instalar, precisa de internet para exportar); logos oficiais do Figma
  *[BRAND] Optimall – ID Assets* — colorido, branco e preto, em SVG e PNG 2x (o branco é o logo
  sobre roxo no deck e no post); grafismos, `mensagens.md` (público B2B, módulos, números oficiais, voz, frases
  aprovadas), `links-oficiais.md` e `marca.json`. Marca aprovada pelo maintainer em
  2026-09-30.
- **E-mail** (`design-system/newsletter/`, `/newsletter-optimall`): 20 blocos e o botão VML,
  **já escritos na paleta do Optimall** — roxo `#9934FF` com texto branco no botão, lavandas
  nos fundos, `#9025F4` para link e destaque sobre claro, dark mode próprio. Header com o logo
  do Optimall, rodapé social com Instagram e LinkedIn, rodapé legal com `© Optimall` e só a
  Política de Privacidade. Não existe passo de troca de cor no fim da montagem.
- **Apresentação** (`design-system/apresentacao/`, `/apresentacao-optimall`): os 14 tipos de
  slide da *Apresentação Comercial 2026*, canvas 1920×1080, export em PDF.
- **Post** (`design-system/post/`, `/post-optimall`): os 7 modelos do *Social Media –
  Optimall*, canvas 1080×1350, export em PNG e legenda.
- **Foto** (`brand/photography/`, `/foto-optimall`): Style Lock novo — a mesma luz natural,
  lente e composição de sempre, em tons de roxo; o celular deixa de ser obrigatório no
  quadro; o elenco vai além do cliente do shopping, com lojistas, gerentes e equipe, num
  registro de negócio sem exagero.
- **Scripts**: `conferir.py` (paleta, sobras, variáveis e a própria marca), `exportar.py`
  (PNG e PDF, conferindo antes se a Halyard carregou) e `check-atualizacao.sh`. O `conferir.py`
  ignora os comentários do HTML e, no e-mail, acusa botão quebrado fora do Outlook.

### Fora do repositório

- **Telas do produto** (`brand/assets/produto/`) e **fotos dos posts** (`brand/assets/fotos/`,
  de banco de imagem) ficam só no computador de quem monta, no `.gitignore`. Os slides e
  posts apontam para elas pelo nome; o maintainer passa a pasta ao time por fora. Sem ela, a
  skill para e diz o que fazer.

### Pendente

- **Regra de envio do e-mail.** O sistema que dispara o e-mail ainda não passou as variáveis
  que aceita. Até lá, a peça sai **sem nenhuma variável `{{...}}`** — nem `{{email}}` no
  rodapé — e a entrega avisa.
- **Refs fotográficas próprias.** O Style Lock ainda não tem imagens de referência
  aprovadas; até lá, o prompt sai sem `--sref`.
