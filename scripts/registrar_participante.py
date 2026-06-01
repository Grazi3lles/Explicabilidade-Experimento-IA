import argparse
import csv
import uuid
from datetime import datetime

from _paths import PARTICIPANTES_CSV


def registrar(nome: str, idade: str, profissao: str, escolaridade: str) -> tuple[str, str]:
    participante_id = str(uuid.uuid4())
    sessao = str(uuid.uuid4())
    data_hora = datetime.now().isoformat()

    PARTICIPANTES_CSV.parent.mkdir(parents=True, exist_ok=True)
    novo_arquivo = not PARTICIPANTES_CSV.exists() or PARTICIPANTES_CSV.stat().st_size == 0

    with PARTICIPANTES_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if novo_arquivo:
            writer.writerow(
                ["id", "sessao", "nome", "idade", "profissao", "escolaridade", "dataHora"]
            )
        writer.writerow(
            [participante_id, sessao, nome, idade, profissao, escolaridade, data_hora]
        )

    return participante_id, sessao


def main() -> None:
    parser = argparse.ArgumentParser(description="Registra participante do experimento.")
    parser.add_argument("nome")
    parser.add_argument("idade")
    parser.add_argument("profissao")
    parser.add_argument("escolaridade")
    args = parser.parse_args()

    participante_id, sessao = registrar(
        args.nome, args.idade, args.profissao, args.escolaridade
    )
    print(f"id={participante_id}")
    print(f"sessao={sessao}")


if __name__ == "__main__":
    main()
