# Experimento IA

Projeto para conduzir um experimento acadêmico sobre **percepção de confiabilidade e explicabilidade** em respostas de sistemas de IA. O participante escolhe entre duas alternativas (A ou B) para cada pergunta de história; as alternativas variam em nível de explicação (detalhada vs. curta) e veracidade, conforme um desenho experimental controlado.

## Como executar

1. Abra este repositório no **Cursor**.
2. A regra [`.cursor/rules/agente-experimento.mdc`](.cursor/rules/agente-experimento.mdc) orienta o agente a conduzir o experimento (acolhimento, 12 perguntas, registro de dados).
3. Inicie um chat com o agente e siga o fluxo como participante.

## Fluxo para o participante

1. Conversa de acolhimento (nome, idade, profissão, escolaridade — uma informação por vez).
2. Aviso de que a atividade **não é um teste de conhecimento**.
3. Doze perguntas de história, em ordem fixa, cada uma com alternativas A e B.
4. Escolha entre A ou B em cada pergunta.
5. Após cada escolha, uma pergunta qualitativa (sonda) sobre o motivo da preferência.

## Dados coletados

| Arquivo | Conteúdo |
|---------|----------|
| [`dados/participantes.csv`](dados/participantes.csv) | `id`, `sessao`, dados demográficos, `dataHora` |
| [`dados/respostas.csv`](dados/respostas.csv) | `sessao`, `perguntaId`, `configuracao`, `escolha`, `dataHora` |
| [`dados/respostas_qualitativas.csv`](dados/respostas_qualitativas.csv) | Respostas às sondas qualitativas após cada escolha |
| [`dados/banco_questoes.json`](dados/banco_questoes.json) | Enunciados e quatro variantes de resposta por questão |
| [`dados/sondas_qualitativas.json`](dados/sondas_qualitativas.json) | Sondas por categoria (explicabilidade, confiança, etc.) |

A coluna `sessao` liga cada participante às suas respostas.

## Scripts (teste manual)

Na raiz do repositório:

```bash
python scripts/registrar_participante.py "Maria" "28" "Estudante" "Superior completo"
python scripts/registrar_resposta.py "SESSAO-UUID" "q01" "1" "A"
python scripts/registrar_qualitativa.py "SESSAO-UUID" "q01" "1" "A" "explicabilidade" "exp_01" --resposta "A explicação foi clara."
```

Substitua `SESSAO-UUID` pelo valor impresso pelo primeiro comando.

## Equipe de pesquisa

O agente possui **chaves de controle** descritas na regra do experimento (auditoria de gabarito e configuração). Esses comandos são apenas para pesquisadoras e não devem ser divulgados aos participantes.

## Estrutura

```
Experimento-IA/
├── .cursor/rules/agente-experimento.mdc
├── dados/
│   ├── banco_questoes.json
│   ├── participantes.csv
│   └── respostas.csv
└── scripts/
    ├── _paths.py
    ├── registrar_participante.py
    ├── registrar_resposta.py
    └── registrar_qualitativa.py
```

## Requisitos

- Python 3.10+ (biblioteca padrão apenas).
