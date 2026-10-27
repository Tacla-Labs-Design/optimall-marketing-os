# Optimall · post e carrossel

Post de feed para Instagram e LinkedIn, 1080 × 1350 (4:5), sozinho ou em carrossel. B2B: fala
com quem decide no shopping, nunca com o consumidor final. Sai em PNG, um por card, com a
legenda pronta.

Regras da marca: `https://marcas.taclalabs.workers.dev/optimall/BRAND.md`.

## Briefing

Obrigatório: **onde sai** (Instagram, LinkedIn ou os dois), **post único ou carrossel** (e a
história em passos) e **o pedido** (o que a pessoa faz depois de ver).

Padrão se faltar:
- Pedido: *Fale com um consultor* — "link na bio" no Instagram, a URL no LinkedIn.
- Carrossel: capa → um ponto por card → fecho com o CTA. De 3 a 10 cards.
- Números: só os oficiais do `BRAND.md`. Depoimento: só real, com nome e cargo, confirmado.

Antes de montar, escreva o roteiro (card, modelo, o que ele diz) com o texto de cada card e
confirme com quem pediu.

## Modelo

`https://marcas.taclalabs.workers.dev/optimall/modelos/post-1080x1350.html`, Halyard pelo kit
do Adobe Fonts.

| Card | Quando usar | Limites |
|---|---|---|
| foto com título (lavanda) | capa: uma promessa, com gente | `titulo` até 4 linhas curtas (~45 caracteres); `linha-fina` até 60 |
| grade de recursos (roxo) | 3 coisas de peso igual (modalidades, módulos, benefícios) | `titulo` até 2 linhas; `item-N` até 20 cada; `frase` até 40 |
| citação (lavanda + vidro) | prova em pessoa, sem foto | `depoimento` até 5 linhas de ~20 caracteres; `nome`; `cargo` |
| foto com faixa e lista (lavanda) | fecho: convite com lista de benefícios | `titulo` até 2 linhas; `lista` até 5 itens de ~30 |
| depoimento com foto (lavanda) | prova em pessoa, com foto | `depoimento` até 3 linhas, ~75 caracteres; `nome`; `cargo` |

Copie a `<section class="post">` de cada card, com o `<style>` que vem antes dela, na ordem do
carrossel, e troque só os `data-slot`. Apague os que não usar. Não crie layout novo nem mude
cor, fonte, tamanho ou posição.

- **O que não cabe vira outro card.** Nunca fonte menor: título a partir de 56 px, apoio no
  mínimo 24 px. Margem de 64 px para texto e logo.
- O texto longo mora na **legenda**, não na arte.
- **Foto** (`data-slot="foto"`): vem do time — as fotos de banco não estão no hub. JPG na
  proporção do espaço, que corta o centro. Foto nova segue o guia de foto
  (`https://marcas.taclalabs.workers.dev/optimall/guias/foto.md`).
- **Tela do produto** (cards de painel e plataforma) não está no hub: esses cards existem só no
  repositório da marca. Nunca gere nem redesenhe tela.
- Logo branco sobre roxo, colorido sobre claro — já estão nos cards. Texto sobre o roxo é sempre
  branco.

## Legenda

Um arquivo `legenda.txt` para o post ou o carrossel inteiro:

```
INSTAGRAM
<gancho de até ~125 caracteres na 1ª linha> <2 a 5 frases curtas> <CTA: Fale com um consultor, link na bio> <3 a 5 hashtags específicas>

LINKEDIN
<a mesma legenda, com a URL https://www.optimall.com.br/fale-conosco e até 3 hashtags>

ALT
01: <o que o card 1 mostra e o texto que está nele>
02: …
```

A primeira linha se lê sozinha (sem "Você sabia", sem emoji, sem começar pelo nome da marca).
Emoji: de preferência nenhum. Menção a cliente (@ de shopping) só com autorização.

## Gerar os PNGs

Um PNG por card, no tamanho real. Abra o arquivo com `#card=N` no fim do endereço: a página
mostra só aquele card, em 1080 × 1350. Para cada card (1, 2, 3…):

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --hide-scrollbars \
  --window-size=1080,1350 --virtual-time-budget=8000 \
  --screenshot="01.png" "file://$PWD/post.html#card=1"
```

No Windows, o caminho do Chrome é `C:\Program Files\Google\Chrome\Application\chrome.exe`.
Precisa de internet (a fonte vem do kit). Se a letra sair diferente da Halyard, a fonte não
carregou: gere de novo — não entregue com outra letra.

## Conferência

- [ ] Roteiro confirmado; de 3 a 10 cards num carrossel; capa, miolo, fecho com o CTA.
- [ ] Nenhum texto entre colchetes sobrou; nada cortado; nenhuma fonte abaixo de 24 px.
- [ ] Números só os oficiais; depoimento só real e autorizado.
- [ ] Foto com proporção certa e sem distorção; nenhuma tela de produto gerada.
- [ ] "o Optimall", nunca "a Optimall"; nada do Podi nem da Tacla Labs — na arte e na legenda.
- [ ] PNGs de 1080 × 1350, um por card, na ordem; `legenda.txt` com Instagram, LinkedIn e ALT.
