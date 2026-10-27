# QA — rodar antes de entregar qualquer e-mail

## Estrutura
- [ ] `<!DOCTYPE>` XHTML Transitional com `xmlns:v` e `xmlns:o`
- [ ] Bloco `<!--[if mso]>` com `PixelsPerInch` 96 e o override de `font-family: Arial !important`
- [ ] Preheader oculto é o primeiro elemento do `<body>`, com 60–90 caracteres
- [ ] Nenhum `<div>` fazendo papel de layout; só tabelas com `role="presentation"`
- [ ] Container 600px com ghost table MSO em volta
- [ ] Nenhum `margin` em elemento de layout (só em `<p>`/`<h*>` como reset)

## CSS
- [ ] Todo estilo visual está inline; o `<style>` só tem reset, media query e dark mode
- [ ] Zero `var()`, `calc()`, `flex`, `grid`, `position`, `float`, `rem`
- [ ] Nenhum texto abaixo de 15px (exceto legal 12px, eyebrow 12px e label de número 14px)
- [ ] Todo `<td>` com texto declara `font-family`, `font-size`, `line-height` e `color`

## Imagens
- [ ] Todas com `alt` descritivo, atributo `width` e `display:block;border:0`
- [ ] Todas em JPG/PNG (nada de WebP/SVG/AVIF) e exportadas em 2x
- [ ] URLs absolutas `https://`
- [ ] Teste com imagens bloqueadas: o e-mail continua compreensível e o CTA continua clicável

## Botões
- [ ] Todo CTA usa o par `<v:roundrect>` + `<a>` com `mso-hide:all`
- [ ] Largura do `roundrect` conferida contra o tamanho real do label
- [ ] Altura de toque ≥ 44px

## Responsivo
- [ ] Colunas lado a lado empilham em ≤600px
- [ ] Com a media query desativada, o layout ainda é legível
- [ ] Imagens não estouram o container em 320px de largura

## Dark mode
- [ ] Testado em Apple Mail dark e Outlook.com dark
- [ ] Logo legível nos dois modos (header: logo branco sobre a faixa roxa, que não muda)
- [ ] Nenhum texto escuro sobre fundo escuro

## Marca
- [ ] Header `01-header` com a faixa roxa, o logo branco e a imagem de abertura colada nela, conteúdo dentro da `00-moldura-conteudo`, rodapé social `90-social` fora dos cards, com o logo e as redes do Optimall
- [ ] Texto B2B, de `brand/mensagens.md`: fala com o gestor do shopping, números só os
      oficiais, CTA *Fale com um consultor*; sempre "o Optimall", nunca "a Optimall"
- [ ] Nada do Podi nem da Tacla Labs — nem no texto, nem no `alt`, nem em imagem
- [ ] `python3 -I scripts/conferir.py <arquivo>` saiu 0 — é ele que garante: nenhuma cor fora
      da paleta, roxo de marca nunca como texto sobre a página, nenhuma sobra de outra marca,
      nenhuma variável `{{...}}`

## Conteúdo e envio
- [ ] Subject ≤ 45 caracteres, sem emoji duplicado, sem CAPS
- [ ] Rodapé com `© <ano> - Optimall`, motivo do recebimento e Política de Privacidade
- [ ] **Nenhum link de descadastro** na peça (não existe variável para ele)
- [ ] `python3 -I scripts/conferir.py arquivo.html` sai com 0: **nenhum** `{{...}}` — nem `{{MAIUSCULA}}`
      sobrando, nem variável de envio, enquanto a regra do sistema estiver pendente
      (`variaveis-envio.md`), e a entrega avisa que a regra está pendente
- [ ] Link da Política de Privacidade conforme `brand/links-oficiais.md`
- [ ] Todos os links testados e com `target="_blank"`
- [ ] HTML final < 100 KB (o `conferir` mede)
- [ ] Sem `<script>`, `<form>`, `<iframe>`, `<video>`
- [ ] Versão texto puro gerada (se a ferramenta de envio não gerar sozinha)
