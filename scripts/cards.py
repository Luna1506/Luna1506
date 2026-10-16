"""Erzeugt die Projektkarten für das GitHub-Profil: python3 scripts/cards.py assets"""
import sys
from html import escape

OUT = sys.argv[1]
MONO = "ui-monospace, 'JetBrains Mono', SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, 'Helvetica Neue', Arial, sans-serif"

FLAKE = """
  <g transform="translate(505 92)">
    <g font-family="{mono}" font-size="44" font-weight="800" fill="url(#accent-{ID})" text-anchor="middle">
      <text y="-17">λ</text><text y="-17" transform="rotate(60)">λ</text><text y="-17" transform="rotate(120)">λ</text>
      <text y="-17" transform="rotate(180)">λ</text><text y="-17" transform="rotate(240)">λ</text><text y="-17" transform="rotate(300)">λ</text>
    </g>
    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite" additive="sum"/>
  </g>""".replace("{mono}", MONO)

FLASHCARDS = """
  <rect x="452" y="52" width="104" height="70" rx="10" fill="#2e2a52" stroke="#a89bff" stroke-opacity="0.7" transform="rotate(-8 504 87)"/>
  <g transform="translate(505 96)">
    <g>
      <animateTransform attributeName="transform" type="scale" dur="6s" repeatCount="indefinite"
        values="1 1;1 1;0 1;1 1;1 1;0 1;1 1" keyTimes="0;0.4;0.45;0.5;0.9;0.95;1"/>
      <rect x="-54" y="-36" width="108" height="72" rx="10" fill="#1e1e22" stroke="#ececf0" stroke-opacity="0.8" stroke-width="1.5"/>
      <g>
        <animate attributeName="opacity" dur="6s" repeatCount="indefinite" calcMode="discrete" values="1;0;1" keyTimes="0;0.45;0.95"/>
        <text y="6" font-family="{sans}" font-size="26" font-weight="800" fill="#a89bff" text-anchor="middle">?</text>
      </g>
      <g opacity="0">
        <animate attributeName="opacity" dur="6s" repeatCount="indefinite" calcMode="discrete" values="0;1;0" keyTimes="0;0.45;0.95"/>
        <line x1="-36" y1="-12" x2="30" y2="-12" stroke="#ececf0" stroke-opacity="0.6" stroke-width="3" stroke-linecap="round"/>
        <line x1="-36" y1="0" x2="36" y2="0" stroke="#ececf0" stroke-opacity="0.4" stroke-width="3" stroke-linecap="round"/>
        <line x1="-36" y1="12" x2="14" y2="12" stroke="#ececf0" stroke-opacity="0.4" stroke-width="3" stroke-linecap="round"/>
      </g>
    </g>
  </g>
  <g font-family="{sans}" font-size="9" fill="#141416" font-weight="700">
    <rect x="452" y="140" width="24" height="12" rx="4" fill="#ff7b7b"/><rect x="479" y="140" width="24" height="12" rx="4" fill="#e3b04b"/>
    <rect x="506" y="140" width="24" height="12" rx="4" fill="#5fd08f"/><rect x="533" y="140" width="24" height="12" rx="4" fill="#6ea0ff"/>
  </g>""".replace("{sans}", SANS)

KICKER = """
  <rect x="444" y="38" width="122" height="112" rx="10" fill="#1f3a24" stroke="#9ece6a" stroke-opacity="0.7"/>
  <line x1="505" y1="38" x2="505" y2="150" stroke="#fff" stroke-opacity="0.25"/>
  <circle cx="505" cy="94" r="14" fill="none" stroke="#fff" stroke-opacity="0.25"/>
  <rect x="440" y="80" width="5" height="28" rx="1" fill="#fff" fill-opacity="0.5"/>
  <rect x="565" y="80" width="5" height="28" rx="1" fill="#fff" fill-opacity="0.5"/>
  <g stroke="#c0caf5" stroke-opacity="0.55" stroke-width="2">
    <line x1="470" y1="32" x2="470" y2="156"/><line x1="540" y1="32" x2="540" y2="156"/>
  </g>
  <g fill="#7aa2f7"><rect x="465" y="56" width="10" height="14" rx="3"/><rect x="465" y="118" width="10" height="14" rx="3"/>
    <animateTransform attributeName="transform" type="translate" dur="3s" repeatCount="indefinite" values="0 0;0 10;0 -6;0 0"/></g>
  <g fill="#f7768e"><rect x="535" y="56" width="10" height="14" rx="3"/><rect x="535" y="118" width="10" height="14" rx="3"/>
    <animateTransform attributeName="transform" type="translate" dur="3s" repeatCount="indefinite" values="0 0;0 -8;0 8;0 0"/></g>
  <circle r="5" fill="#fff">
    <animateMotion dur="3s" repeatCount="indefinite" path="M478 70 L532 124 L478 112 L532 60 Z" rotate="0"/>
  </circle>"""

CALENDAR = """
  <rect x="448" y="40" width="114" height="108" rx="12" fill="#1e1a22" stroke="#ff9e64" stroke-opacity="0.7"/>
  <path d="M448 52 a12 12 0 0 1 12 -12 h90 a12 12 0 0 1 12 12 v12 h-114 z" fill="#ff9e64" fill-opacity="0.85"/>
  <rect x="470" y="34" width="4" height="12" rx="2" fill="#ececf0"/><rect x="536" y="34" width="4" height="12" rx="2" fill="#ececf0"/>
  {cells}
  <circle cx="{hx}" cy="{hy}" r="8" fill="#f7768e">
    <animate attributeName="r" values="7;10;7" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.6;1" dur="2s" repeatCount="indefinite"/>
  </circle>"""


def calendar() -> str:
    cells = []
    for row in range(4):
        for col in range(5):
            x, y = 466 + col * 19.5, 80 + row * 18
            cells.append(f'<rect x="{x - 4}" y="{y - 4}" width="8" height="8" rx="2" fill="#ececf0" fill-opacity="0.22"/>')
    return CALENDAR.replace("{cells}", "\n  ".join(cells)).replace("{hx}", str(466 + 3 * 19.5)).replace("{hy}", str(80 + 2 * 18))


CARDS = [
    dict(
        file="card-nixos.svg", title="nixos", repo="Luna1506/nixos", c1="#7aa2f7", c2="#bb9af7",
        lang=("Nix", "#7e7eff"),
        desc=["Mein ganzer Laptop als Flake: Hyprland", "mit Lua-Config, Glas &amp; Blur, vela und ein", "rebuild, das Claude committen lässt."],
        chips=["Nix", "Hyprland", "Home Manager"], art=FLAKE,
    ),
    dict(
        file="card-naklearn.svg", title="NAKLearn", repo="Luna1506/naklearn", c1="#c9c0ff", c2="#8f7dff",
        lang=("TypeScript", "#3178c6"),
        desc=["Aus Vorlesungsfolien werden Lernkarten.", "Claude schreibt sie, FSRS plant sie: im", "Browser, auf Android und auf dem iPhone."],
        chips=["React", "Capacitor", "Claude", "FSRS"], art=FLASHCARDS,
    ),
    dict(
        file="card-kicker.svg", title="Kickerturnier", repo="Luna1506/Kickerturnier", c1="#9ece6a", c2="#73daca",
        lang=("Java", "#b07219"),
        desc=["Turniere für Tischkicker (2v2): Elo pro", "Person, Spielplan nach Verfügbarkeit und", "eine KO-Phase, in die alle einziehen."],
        chips=["Spring Boot", "React", "PostgreSQL", "Docker"], art=KICKER,
    ),
    dict(
        file="card-freiraum.svg", title="Freiraumbande", repo="Luna1506/Freiraumbande", c1="#ff9e64", c2="#f7768e",
        lang=("TypeScript", "#3178c6"),
        desc=["Website mit Kalender, Kontaktseite und", "einem eigenen Admin-Bereich, in dem sich", "die Inhalte ohne Code pflegen lassen."],
        chips=["Spring Boot", "React", "Tailwind", "JWT"], art=calendar(),
    ),
]


def chip_row(chips: list[str], color: str) -> str:
    out, x = [], 28
    for c in chips:
        w = 20 + sum(8.2 if ch.isupper() else 3.6 if ch == " " else 6.6 for ch in c)
        out.append(
            f'<rect x="{x}" y="174" width="{w:.1f}" height="24" rx="12" fill="{color}" fill-opacity="0.10" stroke="{color}" stroke-opacity="0.55"/>'
            f'<text x="{x + w / 2:.1f}" y="190" text-anchor="middle">{escape(c)}</text>'
        )
        x += w + 8
    return "\n    ".join(out)


for c in CARDS:
    desc = "\n    ".join(f'<text x="28" y="{108 + i * 22}">{line}</text>' for i, line in enumerate(c["desc"]))
    lang_name, lang_color = c["lang"]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="212" viewBox="0 0 600 212" role="img" aria-label="{escape(c['title'])}: {escape(' '.join(c['desc']).replace('&amp;', '&'))}">
  <defs>
    <clipPath id="clip-{{ID}}"><rect width="600" height="212" rx="20"/></clipPath>
    <linearGradient id="accent-{{ID}}" x1="0" y1="0" x2="1" y2="0.3"><stop offset="0" stop-color="{c['c1']}"/><stop offset="1" stop-color="{c['c2']}"/></linearGradient>
    <filter id="soft-{{ID}}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="45"/></filter>
  </defs>
  <g clip-path="url(#clip-{{ID}})">
    <rect width="600" height="212" fill="#0b0b12"/>
    <g filter="url(#soft-{{ID}})" opacity="0.45">
      <circle cx="520" cy="40" r="110" fill="{c['c1']}">
        <animateTransform attributeName="transform" type="translate" dur="14s" repeatCount="indefinite" values="0 0;-50 40;0 0"/>
      </circle>
      <circle cx="470" cy="220" r="90" fill="{c['c2']}">
        <animateTransform attributeName="transform" type="translate" dur="18s" repeatCount="indefinite" values="0 0;40 -30;0 0"/>
      </circle>
    </g>
    <rect x="0.5" y="0.5" width="599" height="211" rx="19.5" fill="none" stroke="#fff" stroke-opacity="0.13"/>
    {c['art']}
    <g font-family="{SANS}" fill="#ececf0">
      <text x="28" y="70" font-size="30" font-weight="800" letter-spacing="-0.5" fill="url(#accent-{{ID}})">{escape(c['title'])}</text>
      <text x="28" y="32" font-family="{MONO}" font-size="11.5" fill-opacity="0.45">{c['repo']}</text>
      <g font-size="14.5" fill-opacity="0.82">
    {desc}
      </g>
      <g font-size="11.5" fill="#ececf0">
    {chip_row(c['chips'], c['c1'])}
      </g>
      <circle cx="{572 - len(lang_name) * 5.8 - 10:.1f}" cy="186" r="5.5" fill="{lang_color}"/>
      <text x="572" y="190.5" font-size="12" fill-opacity="0.6" text-anchor="end">{lang_name}</text>
    </g>
  </g>
</svg>
"""
    svg = svg.replace("{ID}", c["file"][5:-4])
    open(f"{OUT}/{c['file']}", "w").write(svg)
    print(c["file"])
