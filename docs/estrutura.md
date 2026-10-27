# Estrutura do repositório

Mapa comentado. Visão para quem usa está no [README](../README.md).

```
brand/                                   IDENTIDADE — camada mais alta
├── README.md                            Público, cor, tipografia (Halyard), logo tricolor, grafismos
├── mensagens.md                         O que dizer: módulos, números oficiais, voz, frases aprovadas
├── links-oficiais.md                    CTA, contato, rodapé legal, redes, textos fixos
├── marca.json                           Fonte de máquina: cores, paleta_extra, logo, links, envio
├── photography/
│   ├── README.md                        Como ler um Style Lock
│   └── STYLE-LOCK-OPTIMALL.md           Direção fotográfica oficial — blocos copiados byte a byte
└── assets/
    ├── header/                          Logo colorido, branco e preto, símbolo (SVG) e PNGs 2x do e-mail
    ├── icones/                          Ícones sociais roxos do rodapé do e-mail
    ├── icones-ui/                       Ícones HugeIcons bulk (currentColor) dos chips
    ├── clientes/                        Logos dos shoppings clientes (roxo do deck e cinza do site)
    ├── parceiros/                       Logos das integrações
    ├── grafismos/                       Símbolo gigante, vidros, elipse e demais grafismos do Figma
    ├── produto/                         Telas do painel e do app — LOCAL, fora do Git
    └── fotos/                           Fotos aprovadas dos posts — LOCAL, fora do Git

design-system/newsletter/                DESIGN SYSTEM do material "newsletter"
├── README.md                            O que é reutilizável e o que é só de e-mail
├── tokens.md                            Cor, tipografia, espaçamento, dark mode, imagens
├── components/                          20 blocos de HTML de e-mail + o botão VML
│   └── README.md                        Catálogo
└── guidelines/
    ├── email-compat.md                  Regras técnicas de HTML de e-mail
    ├── layout-ritmo.md                  Hierarquia, ritmo, limites de CTA e de seções
    ├── variaveis-envio.md               Variáveis de envio — regra pendente: nenhuma
    └── qa-checklist.md                  Checklist obrigatório antes de entregar

design-system/apresentacao/              DESIGN SYSTEM do material "apresentação"
├── README.md                            Catálogo + como escolher o tipo
├── tokens.md                            Cor, degradês, vidro, Halyard, grafismos, logo
├── slides/                              Os 14 tipos de slide, dos modelos do Figma
└── guidelines/
    ├── canvas-16-9.md                   Canvas fixo 1920×1080, preview e export em PDF
    ├── layout-ritmo.md                  Hierarquia no slide, ritmo do deck, limites
    └── qa-checklist.md                  Checklist obrigatório antes de entregar

design-system/post/                      DESIGN SYSTEM do material "post" (feed 4:5, 1080×1350)
├── README.md                            Catálogo + como escolher o modelo
├── tokens.md                            Cor, tipografia, grafismos do post
├── posts/                               Os 7 modelos, um <section class="post"> por arquivo
└── guidelines/                          canvas, carrossel, legenda, qa-checklist

templates/newsletter/base.html           Shell do e-mail, com dark mode. NUNCA editar por campanha
templates/apresentacao/base.html         Shell do deck: tokens, logos, Halyard, escala e PDF
templates/post/base.html                 Shell do post: canvas 1080×1350 e prévia

.claude/
└── skills/
    ├── newsletter-optimall/SKILL.md     Skill oficial — monta o e-mail
    ├── apresentacao-optimall/SKILL.md   Skill oficial — monta o deck 16:9
    ├── post-optimall/SKILL.md           Skill oficial — monta post/carrossel, PNG e legenda
    └── foto-optimall/SKILL.md           Skill oficial — escreve o prompt de foto de marca

skills/README.md                         Índice das skills (elas moram em .claude/skills/)

examples/                                ACERVO CURADO — só o maintainer grava

projects/
├── README.md                            Como preparar um envio
└── _inbox/<slug>/                       ENTRADA: briefing + imagens. Fora do Git

saida/<slug>/                            SAÍDA: o material montado. Fora do Git

docs/
├── como-usar.md                         Guia de primeira vez
├── como-enviar-conteudo.md              Guia de quem escreve: documento e nome das imagens
├── governanca.md                        Quem altera o quê, como propor mudança
└── estrutura.md                         Este arquivo

scripts/check-atualizacao.sh             Verifica/atualiza a cópia local do padrão
scripts/publicar                         Publica a marca no hub de marcas (só maintainer)

hub/BRAND.md, hub/guias/, hub/modelos/   A marca no hub: regras curtas, um guia por peça, modelos com data-slot
scripts/conferir.py                      Confere a peça montada (paleta, sobras, variáveis) e a marca
scripts/exportar.py                      PNG de post e PDF de deck pelo Chrome; confere a fonte antes

CLAUDE.md                                Contexto global para agentes de IA
README.md                                Porta de entrada, linguagem não técnica
CHANGELOG.md                             Mudanças no padrão, com o porquê
```

## Por que assim

**Uma marca, um repositório.** Tudo aqui é do Optimall: a identidade mora direto em `brand/`,
cada material tem uma biblioteca só, e as skills não perguntam de quem é a peça. O que não é
do Optimall não entra — nem como referência.

**Os blocos de e-mail já nascem na paleta do Optimall.** Cada componente é escrito com os
valores de `design-system/newsletter/tokens.md`, roxo e lavanda, com o botão de texto branco.
Não existe passo de troca de cor no fim da montagem: um passo a mais seria um passo que
alguém esquece. O `scripts/conferir.py` só confere o que foi montado.

**Telas do produto e fotos de banco fora do Git.** O repositório é público. As telas do painel
e do app mostram o produto por dentro, e as fotos dos posts são de banco de imagem, com
licença que não permite redistribuir o arquivo. As duas pastas existem no computador de quem
monta e entram no `.gitignore`; os slides e posts apontam para elas pelo nome. O resto — logos
de clientes, parceiros, grafismos, ícones — é público e fica versionado.

**Fotografia dentro de `brand/`.** Direção fotográfica é identidade, como a cor e o logo —
vale para e-mail, deck, post e impresso.

**`brand/` separado de `design-system/`.** A cor de marca e a regra de contraste valem para
qualquer material. As regras de tabela e VML valem só para e-mail. Misturar as duas faria
todo material novo herdar limitação de Outlook.

**`design-system/<material>/`.** Cada material tem tokens, componentes e QA próprios. O que é
comum — paleta, contraste, papéis tipográficos — está em `brand/` ou repetido em cada
`tokens.md` com o valor certo para aquele suporte.

**Apresentação e post podem usar CSS moderno.** Flex, grid, `var()`, degradê e
`backdrop-filter` são proibidos no e-mail por causa do Outlook e livres no deck e no post, que
abrem num navegador. Foi exatamente para isso que as camadas ficaram separadas.

**`scripts/exportar.py`.** PNG de post e PDF de deck saem do Chrome da máquina, sem instalar
nada. O script confere a fonte antes: a Halyard vem do kit web do Adobe Fonts, e sem internet
ela não chega — o script para em vez de exportar com outra letra.

**Componentes fora de `templates/`.** O template é só o shell. Os blocos, slides e posts são
componentes do design system: se copiam para dentro do template, não são templates.

**`projects/` e `saida/` fora do Git.** O trabalho de cada pessoa é local. Ninguém
sobrescreve ninguém, e material bruto não infla o histórico do repositório.

**Skills com sufixo `-optimall`.** A ferramenta de IA traz dezenas de comandos próprios. Sem o
sufixo, na hora de digitar não dá para saber qual comando é o padrão da marca.

**Skills em `.claude/skills/`.** É a pasta que o Claude Code descobre sozinho. Uma segunda
cópia em `skills/` criaria duas versões divergindo — por isso `skills/` é só o índice.

**`hub/` e `scripts/publicar`.** O time também usa a marca fora deste repositório, pelo hub de
marcas (`https://marcas.taclalabs.workers.dev/optimall/manifest.json`), que qualquer ferramenta lê sem
clonar nada. O hub tem uma versão curta do padrão: `BRAND.md`, um guia por peça e modelos HTML com
`data-slot`, que puxam logos e imagens pelo endereço do hub. A fonte dessa versão é a pasta
`hub/`; o `scripts/publicar` monta a pasta da marca, confere que todo endereço citado existe e
envia ao bucket, com o manifesto por último. Mudou uma regra aqui que o hub repete? Mude também em
`hub/` e publique de novo.

