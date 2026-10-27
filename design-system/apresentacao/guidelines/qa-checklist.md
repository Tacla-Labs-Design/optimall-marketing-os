# QA — rodar antes de entregar qualquer apresentação

## Canvas

- [ ] Todo slide tem 1920 × 1080 e nada foi cortado por `overflow:hidden`
- [ ] Nenhum texto fora da margem de segurança de 64px
- [ ] Nenhuma barra de rolagem horizontal no navegador
- [ ] O último slide é o `11-encerramento`, com os contatos comerciais

## Cor

- [ ] Todos os slides são da biblioteca `design-system/apresentacao/slides/`
- [ ] Nenhuma cor escrita direto no slide — tudo por `var(--token)` de `../tokens.md`
- [ ] Texto sobre o roxo é branco (ou `--branco-90`/`--branco-80`), nunca preto, cinza ou lilás
- [ ] Roxo como texto sobre fundo claro é `--roxo-texto`, nunca `--roxo`

## Tipografia

- [ ] Só Halyard Text, nos pesos do `tokens.md`
- [ ] Nenhum texto de leitura abaixo de 24px
- [ ] O título de cada slide cabe em duas linhas

## Imagens

- [ ] Todas em `assets/` da própria pasta, com caminho relativo
- [ ] Todas com `alt` descrevendo o que a imagem mostra
- [ ] Exportadas em 2x da exibição (ver `../tokens.md`)
- [ ] Nenhuma distorcida ou cortada para caber
- [ ] Logo pelos `<symbol>` do template: branco sobre roxo, colorido sobre claro; nunca PNG,
      nunca `filter`, nunca recolorido
- [ ] Logo de cliente na versão roxa (`*-roxo.svg`) de `brand/assets/clientes/`

## Conteúdo

- [ ] Nenhum `{{PLACEHOLDER}}` sobrou
- [ ] Todo número está em `brand/mensagens.md`, com a legenda certa
- [ ] O CTA é *Fale com um consultor*, apontando para `links.cta` de `brand/marca.json`
- [ ] Sempre "o Optimall", nunca "a Optimall"
- [ ] Nada do Podi nem da Tacla Labs — nem no texto, nem no `alt`, nem na imagem
- [ ] Uma ideia por slide, nenhum slide acima de ~60 palavras

## Export

- [ ] PDF gerado em paisagem, margens nenhuma, fundos ligados
- [ ] Um slide por página no PDF, nada cortado, nenhum fundo faltando
- [ ] O deck abre sozinho a partir da pasta, sem depender de nada externo

## Comandos

```bash
f=saida/<slug>/index.html
python3 -I scripts/conferir.py $f     # saída 0 — placeholders, alt, assets/, paleta, sobras; "N slides"
python3 -I scripts/exportar.py pdf $f # saída 0 — uma página por slide
```
