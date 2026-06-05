import argparse
import csv
from datetime import datetime
from pathlib import Path

from _paths import RESPOSTAS_QUALITATIVAS_CSV


def registrar(
    sessao: str,
    pergunta_id: str,
    configuracao: str,
    escolha: str,
    categoria: str,
    sonda_id: str,
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
                    "categoria",
                    "sondaId",
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
                categoria,
                sonda_id,
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
    parser.add_argument("categoria")
    parser.add_argument("sondaId")
    parser.add_argument(
        "--resposta",
        help="Texto da resposta qualitativa do participante.",
    )
    parser.add_argument(
        "--arquivo",
        type=Path,
        help="Arquivo UTF-8 com a resposta qualitativa (preferível para textos longos).",
    )
    args = parser.parse_args()

    if args.arquivo:
        resposta = args.arquivo.read_text(encoding="utf-8").strip()
    elif args.resposta:
        resposta = args.resposta.strip()
    else:
        parser.error("Informe --resposta ou --arquivo.")

    registrar(
        args.sessao,
        args.perguntaId,
        args.configuracao,
        args.escolha,
        args.categoria,
        args.sondaId,
        resposta,
    )
    print("ok")


if __name__ == "__main__":
    main()
