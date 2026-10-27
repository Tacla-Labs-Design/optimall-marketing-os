# Changelog

Mudanças no padrão — templates, tokens, regras e assets fixos.

Mantido pelo dono do repositório. Quem monta material lê para saber o que mudou desde a
última peça; as skills avisam quando a cópia local está atrás.

**Ação necessária** marca o que exige refazer ou revisar algo já montado. O resto
entra sozinho na próxima peça.

---

## 2026-10-27 — O Optimall no hub de marcas, com a assinatura "Uma solução Optimall"

O time passa a usar a marca também pelo hub (`https://marcas.taclalabs.workers.dev/optimall/`),
que qualquer ferramenta lê sem clonar o repositório. Até aqui o Optimall estava no hub só de
forma provisória, com o logo antigo e a assinatura publicados a partir de outro repositório.

### Novo

- **Assinatura "Uma solução Optimall"** em `brand/assets/assinatura/` (preto, branco e colorido)
  e as regras dela em `brand/README.md`. A colorida usa no símbolo o lilás do logo oficial
  (`#BD7CFF`), no lugar do `#C084FC` da versão anterior.
- **`hub/`**: `BRAND.md`, guias de e-mail, apresentação, post e foto, e modelos HTML com
  `data-slot` (e-mail, deck com os slides que não usam tela, post com os cards que não usam tela).
- **`scripts/publicar`**: monta a pasta da marca, gera os PNGs dos logos e da assinatura, confere
  que todo endereço citado existe e que nenhuma tela ou foto de banco vai junto, e envia ao bucket
  com o manifesto por último. As chaves da assinatura são as mesmas que o Byfrost já usa.

### Mudado

- `scripts/conferir.py` aceita imagem pelo endereço do hub e campo de imagem vazio com
  `data-slot`, e conta os condicionais do Outlook só fora dos comentários.

---

## 2026-10-27 — E-mail: logo e imagem de abertura num card só, conteúdo num card

O desenho do e-mail ficou fixo em três partes, a pedido do maintainer na revisão da primeira
peça: o **card do header** (faixa roxa com o logo branco e a imagem de abertura colada nela), o
**card de conteúdo** (do título ao último bloco) e o **rodapé solto** sobre o fundo lavanda.

### Mudado

- `01-header`: faixa roxa da marca (`#9934FF`) com o logo **branco** oficial no topo e, colada
  nela, a imagem de abertura (`capa` do briefing), nas bordas do card, com raio só nos cantos
  de baixo. Sem imagem de abertura, o card fica só com a faixa. A faixa não muda no dark mode.
- `03-hero-image` deixa de ser a abertura da peça: serve para imagem em largura inteira no
  meio do conteúdo.

### Novo

- `00-moldura-conteudo`: o card branco (escuro no dark mode) que envolve todos os blocos de
  conteúdo, com as partes ABRE e FECHA. Obrigatório.

**Ação necessária:** e-mail montado antes disto, se ainda não saiu, ganha o novo header e a
moldura de conteúdo.

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
