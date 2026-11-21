import sys, json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
model, voices_npz, chunks_path, outdir, speed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5])
REPL = [("almakɑ̃ʒamˈil", "almakandʒamˈil"), ("uatsˈap", "watsˈap"), ("ljˈa", "liˈa")]
k = Kokoro(model, voices_npz)
out = []
for c in json.load(open(chunks_path)):
    ph = k.tokenizer.phonemize(c["text"], "fr-fr")
    for a, b in REPL: ph = ph.replace(a, b)
    audio, sr = k.create(ph, voice="ff_siwis", speed=speed, lang="fr-fr", is_phonemes=True)
    a = np.asarray(audio, dtype=np.float32)
    thr = 0.01 * np.max(np.abs(a)); idx = np.where(np.abs(a) > thr)[0]
    s0 = max(0, idx[0] - int(0.02*sr)); s1 = min(len(a), idx[-1] + int(0.06*sr))
    a = a[s0:s1]
    sf.write(f"{outdir}/{c['id']}.wav", a, sr, subtype="PCM_16")
    out.append({"id": c["id"], "text": c["text"], "phonemes": ph, "dur": round(len(a)/sr, 3), "peak": round(float(np.max(np.abs(a))), 3)})
    print(f"{c['id']}  {len(a)/sr:5.2f}s  peak={np.max(np.abs(a)):.2f}  {ph}")
json.dump(out, open(f"{outdir}/chunks-measured.json", "w"), ensure_ascii=False, indent=1)
print("TOTAL speech: %.2fs" % sum(o["dur"] for o in out))
