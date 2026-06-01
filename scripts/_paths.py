from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DADOS = ROOT / "dados"

PARTICIPANTES_CSV = DADOS / "participantes.csv"
RESPOSTAS_CSV = DADOS / "respostas.csv"
BANCO_QUESTOES_JSON = DADOS / "banco_questoes.json"
