"""Gera assets/stack.svg (pilha de tecnologias do README de perfil).

Uso: python scripts/gerar_stack.py
Para mudar a pilha, edite AREAS abaixo e rode de novo. "usado" = já usado em projeto
publicado; "estudando" = em aprendizado (borda tracejada).
"""

from pathlib import Path

# (nome, cor da tecnologia, largura do chip, usado em projeto?)
AREAS = [
    ("Dados", "análise, modelagem e pipelines", [
        ("SQL", "#14b8a6", 80, True),
        ("PostgreSQL", "#4169e1", 150, True),
        ("Python", "#facc15", 110, True),
        ("Pandas", "#a78bfa", 110, True),
        ("NumPy", "#4dabcf", 100, True),
        ("Power BI", "#f2c811", 125, True),
        ("dbt", "#ff694b", 70, True),
        ("Excel", "#22c55e", 95, True),
    ]),
    ("IA aplicada", "LLM em produção, com limites", [
        ("LLM + tool calling", "#22d3ee", 215, True),
        ("Saída estruturada (zod)", "#a5b4fc", 265, True),
        ("Avaliação de IA", "#34d399", 190, True),
    ]),
    ("Backend", "APIs e servidores", [
        ("Node.js", "#5fa04e", 120, True),
        ("Express", "#9ca3af", 120, True),
        ("TypeScript", "#3178c6", 150, True),
        ("APIs REST", "#60a5fa", 140, True),
    ]),
    ("Front-end", "interfaces e painéis", [
        ("React", "#61dafb", 100, True),
        ("Vite", "#a855f7", 80, True),
        ("Tailwind CSS", "#38bdf8", 170, True),
        ("HTML · CSS · JS", "#f59e0b", 190, True),
    ]),
    ("Infra e ferramentas", "ambiente, CI e deploy", [
        ("Docker", "#2496ed", 110, True),
        ("GitHub Actions", "#2088ff", 180, True),
        ("Git & GitHub", "#f05032", 170, True),
        ("Render", "#a78bfa", 105, True),
        ("pytest · node:test", "#0ea5e9", 205, True),
        ("AWS", "#ff9900", 80, False),
    ]),
]

LARGURA = 1200
MARGEM = 28
COL = (LARGURA - 2 * MARGEM - 16) // 2  # 564
CHIP_ALTURA = 38
CHIP_ESPACO = 12
LINHA_ESPACO = 10


def chips_em_linhas(chips: list, largura: int) -> list[list]:
    linhas, atual, usado = [], [], 0
    for chip in chips:
        w = chip[2]
        if atual and usado + w > largura:
            linhas.append(atual)
            atual, usado = [], 0
        atual.append(chip)
        usado += w + CHIP_ESPACO
    if atual:
        linhas.append(atual)
    return linhas


def esc(texto: str) -> str:
    return texto.replace("&", "&amp;").replace("<", "&lt;")


def area(x: int, y: int, w: int, titulo: str, sub: str, chips: list, atraso: list[float], destaque: bool) -> tuple[str, int]:
    linhas = chips_em_linhas(chips, w - 40)
    h = 70 + len(linhas) * (CHIP_ALTURA + LINHA_ESPACO) + 12
    borda = 'stroke="url(#borda)" stroke-opacity=".75"' if destaque else 'stroke="#ffffff" stroke-opacity=".08"'
    partes = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#ffffff" fill-opacity=".025" {borda}/>',
        f'<text x="{x + 20}" y="{y + 34}" font-size="20" font-weight="700" fill="#ffffff">{esc(titulo)}</text>',
        f'<text x="{x + w - 16}" y="{y + 33}" font-size="14" text-anchor="end" fill="#a1a1b5">{esc(sub)}</text>',
    ]
    cy = y + 59
    for linha in linhas:
        cx = x + 20
        for nome, cor, cw, usado in linha:
            atraso[0] += 0.045
            if usado:
                corpo = f'<rect x="{cx}" y="{cy}" width="{cw}" height="{CHIP_ALTURA}" rx="19" fill="#13101f" stroke="{cor}" stroke-opacity=".6"/>'
                ponto, texto = "1", "#f1f5f9"
            else:
                corpo = f'<rect x="{cx}" y="{cy}" width="{cw}" height="{CHIP_ALTURA}" rx="19" fill="none" stroke="{cor}" stroke-opacity=".65" stroke-dasharray="4 4"/>'
                ponto, texto = "0.7", "#a1a1b5"
            partes.append(
                f'<g class="c" style="animation-delay:{atraso[0]:.2f}s">{corpo}'
                f'<circle cx="{cx + 20}" cy="{cy + 19}" r="5.5" fill="{cor}" fill-opacity="{ponto}"/>'
                f'<text x="{cx + 34}" y="{cy + 25}" font-size="17" font-weight="600" fill="{texto}">{esc(nome)}</text></g>'
            )
            cx += cw + CHIP_ESPACO
        cy += CHIP_ALTURA + LINHA_ESPACO
    return "".join(partes), h


def gerar() -> str:
    atraso = [0.0]
    corpo, y = [], 80
    # Dados ocupa a largura toda; o resto em pares.
    dados, *resto = AREAS
    trecho, h = area(MARGEM, y, LARGURA - 2 * MARGEM, *dados, atraso, True)
    corpo.append(trecho)
    y += h + 16
    for i in range(0, len(resto), 2):
        par = resto[i : i + 2]
        alturas = []
        for j, a in enumerate(par):
            trecho, h = area(MARGEM + j * (COL + 16), y, COL, *a, atraso, a[0] == "IA aplicada")
            corpo.append(trecho)
            alturas.append(h)
        y += max(alturas) + 16
    altura = y + 12
    usados = [n for _, _, cs in AREAS for n, _, _, u in cs if u]
    estudando = [n for _, _, cs in AREAS for n, _, _, u in cs if not u]
    desc = f"Usados em projetos: {', '.join(usados)}. Em estudo: {', '.join(estudando)}."
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{LARGURA}" height="{altura}" viewBox="0 0 {LARGURA} {altura}" role="img" aria-labelledby="t d">
  <title id="t">Stack de tecnologias</title>
  <desc id="d">{esc(desc)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#09090f"/><stop offset="1" stop-color="#170d2b"/></linearGradient>
    <linearGradient id="borda" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2dd4bf"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/></linearGradient>
  </defs>
  <style>
    text {{ font-family: 'Segoe UI', system-ui, -apple-system, Roboto, 'Helvetica Neue', Arial, sans-serif; }}
    .c {{ animation: in .6s ease-out both; }}
    @keyframes in {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <rect width="{LARGURA}" height="{altura}" rx="18" fill="url(#bg)"/>
  <rect x=".5" y=".5" width="{LARGURA - 1}" height="{altura - 1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity=".08"/>
  <text x="40" y="50" font-size="14" font-weight="700" letter-spacing="3" fill="#2dd4bf">STACK POR ÁREA</text>
  <g transform="translate(790 32)">
    <rect x="0" y="0" width="34" height="20" rx="10" fill="#13101f" stroke="#a78bfa" stroke-opacity=".9"/>
    <text x="44" y="16" font-size="14" fill="#d4d4e0">usado em projetos</text>
    <rect x="190" y="0" width="34" height="20" rx="10" fill="none" stroke="#a1a1b5" stroke-opacity=".9" stroke-dasharray="4 4"/>
    <text x="234" y="16" font-size="14" fill="#d4d4e0">aprofundando</text>
  </g>
  {"".join(corpo)}
</svg>
"""


if __name__ == "__main__":
    destino = Path(__file__).resolve().parents[1] / "assets" / "stack.svg"
    destino.write_text(gerar(), encoding="utf-8", newline="\n")
    print(f"{destino.name} gerado")
