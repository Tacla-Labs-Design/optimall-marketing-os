# Optimall · foto de marca (prompt)

Transforma um pedido em português ("foto de uma gerente de loja atendendo", "hero do site") num
prompt pronto para gerador de imagem. A direção visual é fixa; o pedido escolhe só a cena.
Sem modelo HTML: a entrega é o prompt.

Regras da marca: `https://marcas.taclalabs.workers.dev/optimall/BRAND.md`.

## A direção, em uma linha

Fotografia editorial **dentro do shopping**, com **luz natural** (claraboia, fachada de vidro)
batendo no sujeito, câmera **abaixo dos olhos**, quadro claro, e **um único accent: roxo**, em
três valores — `vivid violet purple`, `deep royal purple`, `soft lavender` — em peças inteiras de
roupa e props. Todo o resto em neutros: pedra clara, branco quente, creme, areia, vidro.

- **Elenco:** clientes do shopping **e** quem trabalha nele — lojistas, gerentes de loja, equipe
  de atendimento, gestores. Figurino casual ou business-casual **sem exagero**: tricô, camisa,
  overshirt, blazer desestruturado. Nunca terno e gravata, nunca sala de reunião de escritório.
- **Celular não é obrigatório.** A cena pode ser de trabalho, conversa, atendimento ou passeio.
  Se houver aparelho, a tela é só um brilho violeta, ilegível.
- **Nunca olhar para a câmera.** O olhar vai para o que a pessoa faz na cena.
- **Tela de produto nunca se gera.** A foto sai com a tela ilegível e a tela real entra na
  montagem.
- O Optimall ainda não tem imagens de referência aprovadas: nada de `--sref` nem imagem de
  entrada até elas existirem.

## O que decidir antes de escrever

| Decisão | Opções |
|---|---|
| Tipo de shot | close · plano médio · plano aberto · detalhe de mãos |
| Sujeito + ação | quem é (idade, aparência, papel: cliente, lojista, gerente, atendente, gestor) e o que faz |
| Cenário (só estes) | 1 átrio sob claraboia · 2 mezanino com guarda-corpo de vidro · 3 escada rolante contra átrio envidraçado · 4 praça de alimentação/café com vidro do chão ao teto · 5 corredor com claraboia longitudinal · 6 hall de entrada envidraçado (balcão de informações, totem) · 7 lounge sob claraboia (planta fora do quadro, só a sombra) · 8 porta de loja, com a loja dissolvida em bokeh e o sujeito na luz da claraboia |
| Posição na luz | **obrigatória**: onde o sujeito está em relação à claraboia ou ao vidro, sempre dentro da luz natural e nunca sob a luz da loja |
| Figurino e props roxos | pelo menos uma peça inteira roxa por pessoa em destaque, em 1 a 3 valores |
| Formato | 4:5 feed · 9:16 story · 16:9 banner e site · 1:1 miniatura |
| Lente | 85mm f/2.0 é o padrão. 35mm f/3.2 quando a arquitetura é o assunto (cenários 1, 3, 5) ou com duas ou mais pessoas |

Não pergunte o que dá para inferir ("foto para o Instagram" → 4:5; "banner do site" → 16:9).

## Fórmula

```
[TIPO DE SHOT] + [SUJEITO + AÇÃO] + [CENÁRIO] + [POSIÇÃO NA LUZ NATURAL]
+ [FIGURINO E PROPS ROXOS] + STYLE LOCK + CLEAN-FRAME (só se o gerador não tiver campo de negative)
```

O prompt sai **em inglês**. Nunca escreva hexadecimal dentro do prompt: use os três nomes de cor.

### STYLE LOCK — cole sem editar uma palavra

A **única** troca permitida: com lente de 35mm, a frase que começa em `Shot on` até o ponto
vira `Shot on Sony A7R V, 35mm lens at f/3.2, focus locked on the face, architecture legible but subordinate.`

```text
STYLE LOCK — shot from a low camera angle looking slightly upward, subject placed off-center
with generous clean negative space above and to one side filled by the bright pale void of the
atrium, its warm white ceiling and the glass skylight, a fragment of real blue sky visible
through the glass, confident crop where limbs and hands run off the frame edge, strong
architectural diagonal of a glass balustrade, escalator or mezzanine slab crossing the
background, no horizon line. Lit only by real daylight falling from a large glass skylight
overhead and a full-height glazed facade, a defined shaft of sunlight landing on the subject,
crisp semi-hard shadows with soft edges filled by bounce off the pale polished stone floor so
shadows never reach pure black, natural gobo shadows of skylight mullions and structural beams
raking across the wall, subtle specular sheen on skin. White balance anchored to daylight:
neutral-warm skin at 5400K against cooler 6800K glass, steel and shade, while the mall's
retail lighting stays out of the daylight and reads only as small warm out-of-focus highlights
deep in the background, never touching the subject. Medium-high contrast on an overall
high-key frame exposed for the daylight, lifted cyan-leaning shadows, gentle highlight
rolloff, no clipping. Selective saturation: a desaturated pale stone-grey, warm travertine and
white environment carrying a single dominant saturated purple accent layered across three
values — deep royal purple, vivid violet purple, soft lavender — always a cool violet purple,
never pink or magenta. Natural skin tones, never orange. Natural unretouched skin texture with
visible pores and loose strands of hair. Storefronts, signage and passers-by dissolved into
clean creamy out-of-focus shapes with no readable text or logos. Subject is absorbed in the
moment — eyes on what they are doing in the scene, such as a phone or tablet screen, a
colleague, a customer, a shop window or the mall itself — never on the camera, head slightly
tilted, genuine unposed micro-expression; any phone, tablet or laptop in frame is unbranded,
its screen emitting a soft violet glow, screen content indistinct and unreadable. Clean
high-resolution digital capture, no film grain, no vignette, no chromatic aberration. Shot on
Sony A7R V, 85mm lens at f/2.0, focus locked on the face, background strongly compressed and
separated. Editorial commercial advertising photography, optimistic, confident, sunlit,
unpolished-real.
```

### CLEAN-FRAME CLAUSE — para GPT Image, ChatGPT, Gemini / Nano Banana e Midjourney

Esses geradores não têm campo de negative: listar proibições dentro do prompt faz o modelo
desenhá-las. Cole este bloco depois do STYLE LOCK, sem editar:

```text
CLEAN-FRAME CLAUSE — this is a real photograph taken on a camera. Shadows are present and
directional, and the darkest tone in the frame is a soft cool grey rather than black. Every
edge is crisply frozen, corner brightness is even, and the optics are neutral and modern.
Skin keeps its pores, fine lines and stray hairs. Exactly one saturated hue exists in the
image and it is a cool violet purple; every other surface is pale stone grey, warm white,
cream or clear glass, and any plants stay outside the frame or appear only as soft shadows.
The concourse is quiet and nearly empty, and the few distant figures read as soft featureless
shapes. Storefronts are unbranded and dissolve into smooth creamy blur. The image contains no
writing of any kind: no signage, no banners, no badges, no screens with interfaces, charts or
numbers, no watermark, no caption. Any phone, tablet or laptop is a plain unbranded device, and
its screen is a single soft violet glow with no shapes or icons in it. Hands are anatomically
correct with five fingers each. The subject's eyes stay on what they are doing in the scene,
never on the camera, and the posture is relaxed and caught mid-moment rather than held for the
camera.
```

## Parâmetros por gerador

| Gerador | Como usar |
|---|---|
| Midjourney v6.1 / v7 | fim do prompt: `--ar 4:5 --style raw --stylize 250 --v 6.1` (troque o `--ar` pelo formato) |
| FLUX.1 | guidance 3.0–3.5, 30–40 steps; tamanho do formato (ex.: 1080 × 1350) |
| GPT Image / ChatGPT | sem parâmetros; o formato em palavras no início (`A vertical 4:5 portrait-format photograph.`) |
| Gemini / Nano Banana | formato em palavras; sem imagem de entrada até haver referências aprovadas |
| Ideogram / SDXL | `style: photographic`, CFG 4–6 |

## Entrega

Um bloco por foto: título (cena · cenário · formato), o prompt completo, a versão para GPT Image
e Gemini (com a CLEAN-FRAME) e os parâmetros, mais 2 a 4 linhas de direção — o que reforçar se a
imagem sair fora do padrão.

## Conferência (antes de aprovar a imagem gerada)

- [ ] Câmera abaixo da linha dos olhos; o sujeito não olha para a câmera.
- [ ] Sujeito dentro da luz natural, nunca sob spot de loja; pele neutra, sem amarelo.
- [ ] Quadro claro; sombras com borda definida e base que não chega ao preto.
- [ ] Um único accent, roxo violeta (nunca rosa ou magenta), em mais de um valor e em volume.
- [ ] Nenhuma folhagem verde em volume; nada vermelho ou laranja em destaque.
- [ ] Telas ilegíveis (só o brilho violeta); nenhuma interface, gráfico ou número inventado.
- [ ] Vitrines, letreiros e pessoas ao fundo dissolvidos; nenhum logo de terceiro, nenhum crachá legível.
- [ ] Figurino casual ou business-casual, sem terno e gravata.
- [ ] Mãos corretas; pele com textura; espaço livre para título e logo.
