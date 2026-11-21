#!/usr/bin/env bash
# Pub explicative : voix off Google Gemini TTS -> calage dans les créneaux -> montage -> rendu HyperFrames (sans musique).
# Prérequis : la clé API Gemini enregistrée comme secret réseau de l'environnement
# (hôte generativelanguage.googleapis.com, en-tête x-goog-api-key). La valeur factice ci-dessous
# est remplacée par la vraie clé au passage du proxy : elle n'apparaît jamais ici.
# Usage (depuis almakanjamil-pub/) : bash tools/voix-off-explicatif/gemini/generer.sh [Voix]   (défaut : Puck)
set -euo pipefail
ROOT="${ALMA_ROOT:-$(cd "$(dirname "$0")/../../.." && pwd)}"   # SKIP_TTS=1 / SKIP_RENDER=1 pour tester
AD="$ROOT/explicatif"; G="$ROOT/tools/voix-off-explicatif/gemini"; WORK="$(mktemp -d)"
VOICE="${1:-Puck}"
export DO_NOT_TRACK=1 HYPERFRAMES_NO_TELEMETRY=1 HYPERFRAMES_NO_UPDATE_CHECK=1
export GEMINI_API_KEY="${GEMINI_API_KEY:-cle-factice-remplacee-par-le-proxy}"

# 1) Génération (moteur audio HyperFrames, fournisseur Gemini)
python3 - "$G/audio_request.json" "$WORK/audio_request.json" "$VOICE" <<'PY'
import json, sys
d = json.load(open(sys.argv[1])); d["voice"] = sys.argv[3]; json.dump(d, open(sys.argv[2], "w"), ensure_ascii=False)
PY
if [ "${SKIP_TTS:-0}" != 1 ]; then
  rm -rf "$AD/assets/voice"
  node "$ROOT/node_modules/hyperframes/dist/skills/media-use/audio/scripts/audio.mjs" \
    --request "$WORK/audio_request.json" --hyperframes "$AD" --out "$WORK/audio_meta.json" --only tts | tail -8
fi
n=$(ls "$AD"/assets/voice/l*.wav 2>/dev/null | wc -l)
[ "$n" -eq 11 ] || { echo "ÉCHEC : $n/11 phrases générées (voir anomalies ci-dessus)"; exit 1; }

# 2) Calage : silences retirés, puis léger accéléré (hauteur conservée) si une phrase dépasse son créneau
python3 - "$AD/assets/voice" "$WORK" <<'PY'
import subprocess, sys, json
vdir, work = sys.argv[1], sys.argv[2]
slots = {"l01": (0.15, 1.45), "l02": (1.70, 3.35), "l03": (5.15, 3.35), "l04": (8.60, 2.10), "l05": (10.80, 1.90),
         "l06": (12.80, 1.70), "l07": (14.60, 1.90), "l08": (16.60, 3.27), "l09": (19.97, 2.70), "l10": (22.77, 1.23),
         "l11": (24.10, 3.50)}
def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())
trim = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,areverse"
plan = []
for k, (t, slot) in slots.items():
    src, mid, out = f"{vdir}/{k}.wav", f"{work}/{k}-trim.wav", f"{work}/{k}-fit.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-af", trim, "-ar", "48000", "-ac", "1", mid], check=True)
    d = dur(mid); f = max(1.0, d / slot)
    if f > 1.3:
        print(f"ATTENTION {k} : {d:.2f}s pour {slot:.2f}s (x{f:.2f}) — plafonné à x1.30"); f = 1.3
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mid, "-af", f"atempo={f:.4f}", out], check=True)
    plan.append((k, t, out)); print(f"{k}: {d:.2f}s -> créneau {slot:.2f}s (x{f:.2f})")
json.dump(plan, open(f"{work}/plan.json", "w"))
PY

# 3) Montage sur 27 s, normalisation à -16 LUFS (crête -1,5 dBTP)
python3 - "$WORK" <<'PY'
import json, subprocess, sys
work = sys.argv[1]; plan = json.load(open(f"{work}/plan.json"))
args = ["ffmpeg", "-v", "error", "-y"]; flt = []
for i, (k, t, f) in enumerate(plan):
    args += ["-i", f]; ms = int(round(t * 1000)); flt.append(f"[{i}:a]adelay={ms}|{ms}[a{i}]")
flt.append("".join(f"[a{i}]" for i in range(len(plan))) + f"amix=inputs={len(plan)}:normalize=0,apad=whole_dur=28,atrim=0:28[o]")
subprocess.run(args + ["-filter_complex", ";".join(flt), "-map", "[o]", "-ar", "48000", f"{work}/vo-raw.wav"], check=True)
PY
ffmpeg -v error -y -i "$WORK/vo-raw.wav" -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -ac 2 -c:a pcm_s16le "$AD/assets/audio/voix-off.wav"

# 4) Pas de musique (demande du client).

# 5) Contrôle et rendu HyperFrames
[ "${SKIP_RENDER:-0}" = 1 ] && { echo "montage OK (rendu sauté)"; exit 0; }
cd "$AD"
npx hyperframes check --json > "$WORK/check.json" 2>&1 || true
python3 -c "import json,sys; r=open(sys.argv[1]).read(); d=json.loads(r[r.index('{'):r.rindex('}')+1]); print('check ok' if all(v.get('ok', True) for k, v in d.items() if isinstance(v, dict) and k in ('lint','runtime','audio')) else 'check: voir le rapport')" "$WORK/check.json"
npx hyperframes render -o renders/elmakanjamil-explicatif-9x16.mp4 --quality delivery --fps 30 --workers auto | tail -3
npx hyperframes audio renders/elmakanjamil-explicatif-9x16.mp4 --json 2>/dev/null | python3 -c "import sys,json; l=json.load(sys.stdin)['items'][0]['loudness']; print('mix', l['lufsIntegrated'], 'LUFS, crête', l['truePeakDb'], 'dBTP')"
echo "OK : $AD/renders/elmakanjamil-explicatif-9x16.mp4 (voix Gemini $VOICE)"
