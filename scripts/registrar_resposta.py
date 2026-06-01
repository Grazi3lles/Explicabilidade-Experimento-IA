import argparse
import csv
from datetime import datetime

from _paths import RESPOSTAS_CSV


def registrar(sessao: str, pergunta_id: str, configuracao: str, escolha: str) -> None:
    data_hora = datetime.now().isoformat()

    RESPOSTAS_CSV.parent.mkdir(parents=True, exist_ok=True)
    novo_arquivo = not RESPOSTAS_CSV.exists() or RESPOSTAS_CSV.stat().st_size == 0

    with RESPOSTAS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if novo_arquivo:
            writer.writerow(
                ["sessao", "perguntaId", "configuracao", "escolha", "dataHora"]
            )
        writer.writerow([sessao, pergunta_id, configuracao, escolha, data_hora])


def main() -> None:
    parser = argparse.ArgumentParser(description="Registra resposta do experimento.")
    parser.add_argument("sessao")
    parser.add_argument("perguntaId")
    parser.add_argument("configuracao", choices=["1", "2"])
    parser.add_argument("escolha", choices=["A", "B"])
    args = parser.parse_args()

    registrar(args.sessao, args.perguntaId, args.configuracao, args.escolha)
    print("ok")


if __name__ == "__main__":
    main()
