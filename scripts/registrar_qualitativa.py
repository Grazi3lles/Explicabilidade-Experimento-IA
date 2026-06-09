import argparse
import csv
import json
import sys
from datetime import datetime

from _paths import RESPOSTAS_QUALITATIVAS_CSV, SONDAS_QUALITATIVAS_JSON


def carregar_texto_alternativa(pergunta_id: str, escolha_sonda: str) -> str:
    sondas = json.loads(SONDAS_QUALITATIVAS_JSON.read_text(encoding="utf-8"))
    sonda = sondas.get(pergunta_id)
    if sonda is None:
        print(
            f"erro: sonda não encontrada para {pergunta_id!r} em {SONDAS_QUALITATIVAS_JSON}",
            file=sys.stderr,
        )
        sys.exit(1)

    alternativas = sonda.get("alternativas", {})
    texto = alternativas.get(escolha_sonda)
    if texto is None:
        print(
            f"erro: alternativa {escolha_sonda!r} não encontrada na sonda {pergunta_id!r}",
            file=sys.stderr,
        )
        sys.exit(1)

    return texto


def registrar(
    sessao: str,
    pergunta_id: str,
    configuracao: str,
    escolha: str,
    escolha_sonda: str,
    resposta_qualitativa: str,
) -> None:
    data_hora = datetime.now().isoformat()

    RESPOSTAS_QUALITATIVAS_CSV.parent.mkdir(parents=True, exist_ok=True)
    novo_arquivo = (
        not RESPOSTAS_QUALITATIVAS_CSV.exists()
        or RESPOSTAS_QUALITATIVAS_CSV.stat().st_size == 0
    )

    with RESPOSTAS_QUALITATIVAS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if novo_arquivo:
            writer.writerow(
                [
                    "sessao",
                    "perguntaId",
                    "configuracao",
                    "escolha",
                    "escolhaSonda",
                    "respostaQualitativa",
                    "dataHora",
                ]
            )
        writer.writerow(
            [
                sessao,
                pergunta_id,
                configuracao,
                escolha,
                escolha_sonda,
                resposta_qualitativa,
                data_hora,
            ]
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Registra resposta qualitativa (sonda) do experimento."
    )
    parser.add_argument("sessao")
    parser.add_argument("perguntaId")
    parser.add_argument("configuracao", choices=["1", "2"])
    parser.add_argument("escolha", choices=["A", "B"])
    parser.add_argument("escolhaSonda", choices=["A", "B", "C", "D"])
    args = parser.parse_args()

    resposta = carregar_texto_alternativa(args.perguntaId, args.escolhaSonda)

    registrar(
        args.sessao,
        args.perguntaId,
        args.configuracao,
        args.escolha,
        args.escolhaSonda,
        resposta,
    )
    print("ok")


if __name__ == "__main__":
    main()
