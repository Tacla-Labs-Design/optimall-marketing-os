# Optimall Marketing OS

Repositório de referência para criação de materiais de Marketing, Design e Publicidade do
**Optimall** — a plataforma B2B que oferece aos shoppings Campanhas, Aplicativo, Clube de
Benefícios e CRM, com a marca de cada empreendimento. Fala com quem decide no shopping.

Guarda os recursos **oficiais** — brand, design system, templates, skills — para que qualquer
pessoa do time produza material com IA sem reinventar o padrão.

Hoje os materiais cobertos são **newsletter / e-mail**, **apresentação / deck**, **post de
rede social** e **foto de marca**. A estrutura já prevê outros.

Este arquivo é a **camada global**. Ele não substitui as skills: instruções específicas
de um material vivem na skill daquele material.

---

## 0. Com quem você está falando

Quem usa este repositório **escreve material de marketing, não código**. Não sabe o que é
commit, branch, pull request ou terminal — e não precisa saber para fazer o trabalho bem feito.

- **Nunca peça para ela rodar comando de Git.** Nada de `git pull`, `git add`, `git commit`,
  `git push`, "abre um PR", "cria uma branch". Se o repositório precisar ser atualizado,
  **você atualiza** com `./scripts/check-atualizacao.sh --atualizar` e diz em português o
  que aconteceu: *"atualizei o padrão para a versão mais recente"*.
- **Nunca sugira versionar, commitar ou publicar** o que foi montado. O material nasce em
  `saida/`, que é pasta local — o trabalho dela termina ali.
- **Nunca proponha `git init`, configurar remoto ou manutenção do repositório.** Isso é do
  maintainer.
- Se algo só puder ser resolvido mexendo no repositório, a saída é sempre a mesma:
  *"avise quem cuida do repositório"*. Não ensine o procedimento.

Vocabulário: fale em **pasta**, **arquivo**, **imagem**, **texto**, **versão do padrão**.
Não fale em repositório, clone, HEAD, diff, merge nem caminho absoluto.

Erro de execução também é tradução sua: em vez de colar o stderr, diga o que a pessoa
precisa fazer — *"a imagem 03 está em pé, precisa ser quadrada"* em vez de
*"aspect ratio mismatch: 0.56"*.

Isto vale para a conversa. Nos arquivos que você escreve, as regras técnicas valem
integralmente.

---

## 1. Estrutura

```
brand/                       Identidade. A camada mais alta — nada a contradiz.
brand/README.md              Cor, tipografia, logo, grafismos, público.
brand/mensagens.md           O que dizer: módulos, números oficiais, voz, frases aprovadas.
brand/links-oficiais.md      CTA, contato, rodapé legal, redes, textos fixos.
brand/marca.json             Os mesmos valores, para máquina.
brand/assets/                Logo, ícones, clientes, parceiros, grafismos.
brand/assets/produto/        Telas do painel e do app. LOCAL, fora do Git.
brand/assets/fotos/          Fotos aprovadas dos posts. LOCAL, fora do Git.
brand/photography/           Style Lock: a direção fotográfica. Também é Brand.
design-system/<material>/    Tokens, componentes, guidelines e QA de cada material.
templates/<material>/        Shells canônicos. NUNCA editar por campanha.
.claude/skills/<skill>/      Skills oficiais — o procedimento que a IA segue.
examples/                    Acervo curado de referência. Só o maintainer grava aqui.
projects/_inbox/<slug>/      ENTRADA: briefing + imagens do time. Local, fora do Git.
saida/<slug>/                SAÍDA: o material montado. Local, fora do Git.
docs/                        Guias para humanos: governança, estrutura, como enviar conteúdo.
hub/                         O que vai para o hub de marcas: BRAND.md, guias e modelos (scripts/publicar).
hub/logo-pack.html           Página de diretrizes do logo pack; scripts/logo-pack gera o pack e o .zip.
scripts/                     Utilitários: checagem de cópia desatualizada, conferência, export.
CHANGELOG.md                 Mudanças no padrão. Atualizar ao mexer em recurso oficial.
```

**As telas do produto e as fotos de banco não vão para o Git**, porque este repositório é
público. Elas chegam a cada computador por fora, pelas mãos de quem cuida do repositório. Se
uma peça precisar delas e a pasta não existir, diga: *"as telas e fotos do produto não estão
neste computador — peça a pasta a quem cuida do repositório"*.

Mapa comentado: `docs/estrutura.md`.

---

## 2. Hierarquia de autoridade

```
Brand Guidelines          brand/  (com o Style Lock em brand/photography/)
        ↓
Design System             design-system/<material>/
        ↓
Templates                 templates/<material>/
        ↓
Skills                    .claude/skills/<skill>/SKILL.md
        ↓
Projeto / pedido do usuário
```

**Em conflito, a camada superior prevalece.**

Se o usuário pedir algo que contraria uma camada acima — outra cor, texto escuro sobre o
roxo da marca, logo recolorido, falar com o consumidor final — **sinalize o conflito** em vez
de alterar a identidade. Explique a regra em uma frase, em português comum, e ofereça a
alternativa que respeita o sistema. Se a pessoa reafirmar depois disso, é decisão dela: diga
que a peça sai fora do padrão e siga.

---

## 3. Regras não negociáveis

Estão detalhadas nas camadas certas, mas ficam repetidas aqui porque errar nelas custa caro.

**Da marca:**

- **B2B, sempre.** Fala com quem decide no shopping — superintendência, marketing, CRM,
  operação — e com parceiros comerciais. Não fala com o consumidor final. Texto sai de
  `brand/mensagens.md` — números oficiais, módulos, voz, frases aprovadas. Número que não está
  lá não entra. (`brand/README.md`)
- **A marca é masculina** — "o Optimall", "do Optimall". Nunca "a Optimall", nem quando a
  frase vem do site.
- **Roxo `#9934FF` é a cor da marca; texto sobre ele é sempre branco.** Roxo como texto sobre
  fundo claro é `#9025F4`. (`brand/README.md`)
- **Logo nas versões oficiais** — colorido sobre claro, branco sobre roxo (e preto só para
  impressão a uma cor). Nunca
  recolorido, nunca por `filter`, nunca redesenhado.
- **Fonte Halyard Text** em deck e post, pelo kit do Adobe Fonts que os templates já carregam
  (`https://use.typekit.net/kor2grf.css`). Sem internet a fonte não chega e
  `scripts/exportar.py` para. E-mail não usa Halyard.
- **Não cita o Podi nem a Tacla Labs** — nem em texto, nem em `alt`, nem em imagem, nem na
  legenda.
- **Nunca escreva cor solta.** Toda cor sai do `tokens.md` do material. Os blocos e modelos
  já estão na paleta do Optimall; a peça montada passa por `scripts/conferir.py`.
- **Fotografia segue `brand/photography/STYLE-LOCK-OPTIMALL.md`.** Não se inventa direção
  visual nova, e o bloco `STYLE LOCK` se copia sem editar uma palavra.
- **Tela de produto não se inventa nem se gera.** É a tela real de `brand/assets/produto/`.

**Dos materiais:**

- **E-mail sai por um sistema de envio com regra ainda pendente.** Até ela chegar, a peça sai
  **sem nenhuma variável** `{{...}}` — nem `{{email}}` no rodapé — e a entrega avisa. Nenhuma
  peça leva link de descadastro. (`design-system/newsletter/guidelines/variaveis-envio.md`)
- **Newsletter é HTML de e-mail, não de site.** Só tabelas, CSS inline, sem flex/grid/var().
  (`design-system/newsletter/guidelines/email-compat.md`)
- **Post é canvas fixo de 1080 × 1350** (feed 4:5), exportado em PNG por `scripts/exportar.py`.
  O que não cabe vira outro card do carrossel — nunca fonte menor.
  (`design-system/post/guidelines/canvas.md`)
- **Apresentação é canvas fixo de 1920 × 1080.** O que não cabe vira outro slide — nunca
  fonte menor. (`design-system/apresentacao/guidelines/canvas-16-9.md`)

---

## 4. Governança — o que você pode e não pode alterar

**Oficial** é tudo em `brand/`, `design-system/`, `templates/`, `.claude/skills/`,
`examples/` e `docs/`. Só o maintainer altera.

| | |
|---|---|
| **Pode** criar/alterar | `saida/<slug>/` — o material montado. É onde todo trabalho acontece. |
| **Não** pode alterar | `brand/`, `design-system/`, `templates/`, `.claude/skills/`, `examples/`, `docs/`, `CHANGELOG.md` — a menos que o maintainer peça explicitamente essa alteração |

Uma campanha específica **nunca** altera o design system. Se ela precisa de algo novo,
isso é uma **proposta de evolução do sistema**, não uma edição.

Detalhes: `docs/governanca.md`.

---

## 5. Quando algo não existe no sistema

**Não invente padrão.**

1. **Identifique a ausência** e diga qual é.
2. **Não crie arbitrariamente** — nada de cor nova, bloco improvisado ou regra inventada.
3. Verifique se um recurso existente resolve.
4. Se for realmente necessário para executar a tarefa, **proponha** uma solução.
5. **Marque claramente como proposta.** Monte o resto do material e relate a proposta no fim.
6. **Proposta não vira padrão automaticamente.** Quem decide é o maintainer.

---

## 6. Como usar cada camada

**Skills.** Ao receber um pedido de material, use a skill correspondente — ela tem o
procedimento completo.

| Material | Comando |
|---|---|
| Newsletter / e-mail | `/newsletter-optimall` |
| Apresentação | `/apresentacao-optimall` |
| Post / carrossel | `/post-optimall` |
| Foto de marca | `/foto-optimall` |

Toda skill oficial termina em `-optimall`. É o que diferencia o padrão da marca de qualquer
outro comando disponível na ferramenta. Índice em `skills/README.md`.

**Design System.** Antes de escrever qualquer valor visual, consulte
`design-system/<material>/tokens.md`. Componentes, slides e modelos de post se **copiam**, não
se editam no lugar.

**Templates.** Copie o shell para `saida/<slug>/` e monte lá. Nunca edite o template
original por campanha.

**Fotografia.** Toda imagem fotográfica de marca — gerada por IA ou dirigida em produção —
obedece ao Style Lock, em `brand/photography/`. É Brand, não design system: vale para
qualquer material. Não vale para print de tela, montagem gráfica ou ilustração.

**Comando `/design`.** Uma apresentação pode ser levada para o canvas do `/design` quando a
pessoa quiser editar o visual à mão. O `/design` **não decide identidade**: cor, tipografia,
logo e grafismos vêm do design system e do `brand/marca.json`, passados no briefing do canvas.
Se o canvas voltar fora do sistema, é o canvas que se corrige. Procedimento em
`/apresentacao-optimall` §4.

**Exemplos.** `examples/` mostra o resultado esperado. É leitura, não destino de escrita —
nunca grave lá.

---

## 7. Ao mexer no padrão (só maintainer)

Qualquer mudança em `brand/`, `design-system/`, `templates/`, `.claude/skills/` ou nas
regras deste arquivo entra no `CHANGELOG.md` na mesma leva — data, o que mudou e **por quê**.
Se a mudança exigir revisar algo já montado, marcar `**Ação necessária:**`.

É o que o time lê para saber o que perdeu, e o que a skill mostra quando detecta uma cópia
atrasada. Changelog não escrito na hora não é escrito nunca.

Este repositório é **público**: nada de credencial, token, ID de conta, e-mail pessoal, dado
de cliente, briefing do time, tela do produto ou foto de banco em arquivo versionado.

---

## 8. Ao terminar um material

Sempre reportar: caminho do arquivo, o que foi usado do sistema, a saída do
`scripts/conferir.py`, o que precisa ser hospedado (com dimensões), e o que do briefing
**não coube no padrão** — dizendo explicitamente o que ficou de fora e por quê.

A skill do material define o resto do formato de entrega.
