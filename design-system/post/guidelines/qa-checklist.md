# QA — rodar antes de entregar qualquer post

## Canvas

- [ ] Todo post tem 1080 × 1350 e nada foi cortado por `overflow:hidden`
- [ ] Texto e logo dentro da margem de segurança de 64px
- [ ] Nenhum texto abaixo de 24px; título e frase principal a partir de 56px
- [ ] Carrossel entre 3 e 10 cards, com capa e fecho

## Cor e tipografia

- [ ] Todos os cards são da biblioteca `design-system/post/posts/`
- [ ] Nenhuma cor escrita direto no post — tudo por `var(--token)` de `../tokens.md`
- [ ] Texto sobre o roxo é branco (ou `--lavanda` no vidro)
- [ ] Só Halyard Text, nos pesos do `tokens.md`
- [ ] `python3 -I scripts/conferir.py saida/<slug>/index.html` → saída 0

## Imagens

- [ ] Todas em `assets/` da própria pasta, com caminho relativo e `alt`
- [ ] Nenhuma distorcida ou cortada para caber; foto nova segue o Style Lock do Optimall
- [ ] Logo pela versão certa do fundo (`<use href="#logo-optimall…">`), nunca PNG nem `filter`

## Conteúdo

- [ ] Nenhum `{{PLACEHOLDER}}` sobrou
- [ ] Uma mensagem por card; o título cabe em até 3 linhas
- [ ] Todo número está em `brand/mensagens.md`, com a legenda certa
- [ ] B2B: fala com quem decide no shopping; sempre "o Optimall", nunca "a Optimall"
- [ ] Nada do Podi nem da Tacla Labs (texto, logo, @, link, `alt`, legenda)
- [ ] `legenda.txt` com Instagram, LinkedIn e ALT de cada card

## Export

- [ ] `python3 -I scripts/exportar.py png saida/<slug>/index.html` → saída 0
- [ ] Um PNG por card, na ordem, e **abrir cada um** para conferir de olho
