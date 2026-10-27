# Variáveis de envio — o que o sistema aceita

**A regra de variáveis é do sistema que dispara.** O e-mail do Optimall sai por um sistema
de envio cujas regras **ainda não foram definidas**. O valor oficial está em `envio` de
[`brand/marca.json`](../../../brand/marca.json):

| Sistema | Variáveis permitidas |
|---|---|
| A definir — **regra pendente** | **nenhuma**, até a regra chegar |

Enquanto `envio.variaveis` estiver vazio:

- A peça sai **sem nenhuma variável `{{...}}`** — nem `{{email}}` no rodapé. A frase do
  motivo fica "Você recebeu este e-mail porque …", sem o "em {{email}}".
- A entrega avisa, em destaque: **a regra de envio do Optimall ainda não foi definida** — a
  peça saiu sem nenhuma variável, e quem for disparar precisa conferir no sistema de envio.
- Campo personalizado do briefing (`{{nome}}` e afins) **não entra**: vira texto fixo ou sai
  da peça. Se o briefing insistir no campo, perguntar antes de montar e relatar.

`python3 -I scripts/conferir.py <arquivo>` acusa qualquer `{{...}}` que sobrar.

Quando a regra chegar, o maintainer preenche `envio.sistema` e `envio.variaveis` no
`marca.json`, atualiza este arquivo e registra no `CHANGELOG.md`.

## Sem link de descadastro

Não existe variável para a URL de descadastro. Então:

- **Nenhuma peça leva link de descadastro.**
- Nunca inventar `{{URL_DESCADASTRO}}`, `{{unsubscribe}}` ou equivalente.
- O rodapé continua obrigatório com `© <ano> - Optimall`, o **motivo do recebimento** e a
  Política de Privacidade. É o que informa o destinatário. (O Optimall não tem Termos de Uso.)
- A saída do descadastro é tratada **fora do HTML**, por quem opera o envio.

## Placeholder de montagem ≠ variável de envio

Os componentes e o template usam `{{MAIUSCULAS_COM_UNDERSCORE}}` — `{{ANO}}`,
`{{PREHEADER}}`, `{{TITULO_INTERNO}}`, `{{MOTIVO_RECEBIMENTO}}`. Esses são
**placeholders de montagem**: existem para serem substituídos por texto no arquivo,
antes do envio.

Antes de entregar, conferir que não sobrou nada:

```bash
grep -o "{{[^}]*}}" saida/<slug>/index.html | sort -u
```

A lista tem que vir **vazia**. `{{MAIUSCULA}}` que sobrou é erro de montagem; qualquer outra
é variável que o sistema de envio ainda não aceita.
