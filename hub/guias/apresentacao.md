# Optimall · apresentação 16:9

Deck comercial, reunião com shopping, apresentação de módulo. B2B: fala com quem decide no
shopping. Sai em PDF (uma página por slide) a partir do HTML.

Regras da marca: `https://marcas.taclalabs.workers.dev/optimall/BRAND.md`.

## Briefing

Obrigatório: o objetivo do deck, o público (qual shopping ou grupo, quem estará na sala) e o
que cada slide precisa dizer (tópicos).

Padrão se faltar:
- Duração: 5 minutos ≈ 8 slides; 20 minutos ≈ 20 slides (o máximo).
- Ordem do deck comercial: **capa → números e clientes → problema → (plataforma e módulos) →
  segurança → encerramento**.
- Nome do shopping que não pode aparecer: capa padrão, sem nome.
- Números: só os oficiais do `BRAND.md`. Depoimento: só real, com nome e cargo, confirmado.

Antes de montar, escreva o roteiro (número, slide, o que ele diz em uma frase) e confirme com
quem pediu. Refazer 15 slides custa mais que discordar de uma lista.

## Modelo

`https://marcas.taclalabs.workers.dev/optimall/modelos/apresentacao-16x9.html`, 1920 × 1080
por slide, Halyard pelo kit do Adobe Fonts. Slides:

| Slide | Quando usar | Limites |
|---|---|---|
| capa (roxo) | primeiro slide, sempre | `frase` até 3 linhas curtas (padrão: a tagline); `linha-fina` até 110 caracteres |
| números e clientes | a prova: logo depois da capa | fixo: os 4 números oficiais e os 15 clientes |
| problema (claro) | a dor que o Optimall resolve | `titulo` até 80; `lead` até 220; `texto` até 260; `faixa` até 200 |
| segurança (branco) | LGPD, dados, criptografia | `titulo` até 70; os 2 cards até 60 cada |
| título e texto | uma ideia só; com a classe `titulo-texto--roxo` vira divisor de seção | `tag` até 20; `titulo` até 70; `texto-1` e `texto-2` até 180 |
| citação (roxo) | depoimento real de cliente | `depoimento` até 200; `nome`; `cargo` |
| encerramento (roxo) | último slide, sempre | fixo: tagline, *Fale com um consultor* e os contatos |

Copie a `<section class="slide">` de cada slide, com o `<style>` que vem antes dela, na ordem
do roteiro, e troque só os `data-slot`. Apague os slides que não usar. Não crie slide novo nem
mude cor, fonte, tamanho ou posição. `numero` é o número do slide no rodapé, em sequência
(capa e encerramento não têm).

- **Uma ideia por slide**, até ~60 palavras. Estourou: vira dois slides. Nunca fonte menor que
  24 px, nunca margem menor que 64 px.
- Alterne o fundo: roxo marca a virada; claro, claro-2 e branco dão respiro.
- Logo: branco sobre o roxo, colorido sobre claro — já estão nos slides. Nunca recolorir.
- Texto sobre o roxo é sempre branco. Texto roxo sobre claro é `#9025F4`.
- **Telas do produto** (plataforma, módulos, app, white label) não estão no hub: esses slides
  existem só no repositório da marca. Num deck que precise mostrar o produto, a tela vem do
  arquivo que o time recebe por fora, num `<img>` dentro de um card branco com raio de 40 px.
  Nunca gere nem redesenhe tela.

## Gerar o PDF

Abra o HTML no navegador para conferir (precisa de internet: a fonte vem do kit). Para o PDF:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer \
  --virtual-time-budget=8000 --print-to-pdf="apresentacao.pdf" "file://$PWD/apresentacao.html"
```

No Windows, o caminho do Chrome é `C:\Program Files\Google\Chrome\Application\chrome.exe`.
O PDF sai em paisagem, uma página por slide. Se a letra sair diferente da Halyard, a fonte não
carregou: confira a internet e gere de novo — não entregue com outra letra.

## Conferência

- [ ] Roteiro confirmado; capa primeiro, encerramento por último.
- [ ] Nenhum texto entre colchetes sobrou; nenhum texto estourando a área.
- [ ] Até ~60 palavras por slide; nenhuma fonte abaixo de 24 px.
- [ ] Números só os oficiais, com "+" e a legenda. Depoimento só real e autorizado.
- [ ] Logo branco sobre roxo, colorido sobre claro; texto sobre o roxo sempre branco.
- [ ] Encerramento com *Fale com um consultor* e os contatos oficiais.
- [ ] "o Optimall", nunca "a Optimall"; nada do Podi nem da Tacla Labs.
- [ ] Halyard em todo o texto; PDF com uma página por slide, em 16:9.
