# Fond de plan ILLUSTRATIF (aucune donnée géographique réelle), style OSM Carto clair.
import math, random, sys
W, H = 1200, 2100
rnd = random.Random(7)
out = []
A = out.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
A('<defs><clipPath id="c"><rect width="%d" height="%d"/></clipPath></defs>' % (W, H))
A(f'<rect width="{W}" height="{H}" fill="#f2efe9"/>')
A('<g clip-path="url(#c)">')
# Grille de rues tournée (comme les quartiers en diagonale de la capture).
ang = -27
cx, cy = W / 2, H / 2
A(f'<g transform="rotate({ang} {cx} {cy})">')
xs = [-600]
while xs[-1] < W + 600: xs.append(xs[-1] + rnd.choice([150, 170, 190, 210]))
ys = [-600]
while ys[-1] < H + 600: ys.append(ys[-1] + rnd.choice([130, 150, 170, 200]))
# Îlots : zone résidentielle + bâtiments.
for i in range(len(xs) - 1):
    for j in range(len(ys) - 1):
        x0, x1, y0, y1 = xs[i] + 12, xs[i + 1] - 12, ys[j] + 12, ys[j + 1] - 12
        r = rnd.random()
        if r < 0.07:
            A(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="6" fill="#cdebb0"/>')
            continue
        A(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{"#e6e1da" if r < 0.6 else "#ebe7e1"}"/>')
        bx = x0 + 10
        while bx < x1 - 30:
            bw = rnd.randint(26, 58)
            if bx + bw > x1 - 8: break
            by = y0 + 10
            while by < y1 - 26:
                bh = rnd.randint(22, 48)
                if by + bh > y1 - 8: break
                if rnd.random() < 0.82:
                    A(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#d9d0c9" stroke="#c9bdb3" stroke-width="1.5"/>')
                by += bh + rnd.randint(8, 16)
            bx += bw + rnd.randint(8, 16)
# Rues blanches avec liseré.
for x in xs:
    A(f'<line x1="{x}" y1="-800" x2="{x}" y2="{H+800}" stroke="#d6cfc6" stroke-width="20"/><line x1="{x}" y1="-800" x2="{x}" y2="{H+800}" stroke="#ffffff" stroke-width="16"/>')
for y in ys:
    A(f'<line x1="-800" y1="{y}" x2="{W+800}" y2="{y}" stroke="#d6cfc6" stroke-width="20"/><line x1="-800" y1="{y}" x2="{W+800}" y2="{y}" stroke="#ffffff" stroke-width="16"/>')
# Deux axes principaux (style route primaire OSM).
for x in (xs[5], xs[9]):
    A(f'<line x1="{x}" y1="-800" x2="{x}" y2="{H+800}" stroke="#d9a86a" stroke-width="34"/><line x1="{x}" y1="-800" x2="{x}" y2="{H+800}" stroke="#fcd6a4" stroke-width="28"/>')
A(f'<line x1="-800" y1="{ys[8]}" x2="{W+800}" y2="{ys[8]}" stroke="#d9a86a" stroke-width="34"/><line x1="-800" y1="{ys[8]}" x2="{W+800}" y2="{ys[8]}" stroke="#fcd6a4" stroke-width="28"/>')
A('</g>')
# Fleuve schématique avec une île.
A('<path d="M-60,-40 C 120,300 40,620 150,980 C 250,1320 120,1640 210,2160 L -60,2160 Z" fill="#aad3df"/>')
A('<path d="M30,520 C 70,600 85,700 60,800 C 40,720 20,620 30,520 Z" fill="#cdebb0"/>')
# Voie rapide en arc.
A('<path d="M1300,260 C 900,520 760,900 860,1300 S 1150,1900 1320,2000" fill="none" stroke="#e8a08a" stroke-width="40"/>')
A('<path d="M1300,260 C 900,520 760,900 860,1300 S 1150,1900 1320,2000" fill="none" stroke="#f9b29c" stroke-width="32"/>')
A('</g></svg>')
open(sys.argv[1], "w").write("\n".join(out))
print("ok", len(out))
