import sys, json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
model, vdir, siwis, segs_path, outdir = sys.argv[1:6]
base = np.fromfile(f"{vdir}/pm_alex.bin", dtype=np.float32).reshape(510,1,256)
fr = np.fromfile(siwis, dtype=np.float32).reshape(510,1,256)
voice = base.copy(); voice[:,:,128:] = 0.78*base[:,:,128:] + 0.22*fr[:,:,128:]
np.savez(f"{outdir}/voix-homme.npz", homme=voice)
k = Kokoro(model, f"{outdir}/voix-homme.npz")
REPL = [("almakɑ̃ʒamˈil", "almakandʒamˈil"), ("uatsˈap", "watsˈap"), ("ljˈa", "liˈa")]
out = []
for c in json.load(open(segs_path)):
    ph = k.tokenizer.phonemize(c["text"], "fr-fr")
    for a, b in REPL: ph = ph.replace(a, b)
    speed = 1.14
    while True:
        audio, sr = k.create(ph, voice="homme", speed=speed, lang="fr-fr", is_phonemes=True)
        a = np.asarray(audio, dtype=np.float32)
        thr = 0.01 * np.max(np.abs(a)); idx = np.where(np.abs(a) > thr)[0]
        a = a[max(0, idx[0]-int(0.02*sr)): min(len(a), idx[-1]+int(0.06*sr))]
        if len(a)/sr <= c["slot"] or speed >= 1.4: break
        speed = round(speed + 0.04, 2)
    sf.write(f"{outdir}/{c['id']}.wav", a, sr, subtype="PCM_16")
    out.append({"id": c["id"], "text": c["text"], "phonemes": ph, "speed": speed, "dur": round(len(a)/sr, 3)})
    print(f"{c['id']} speed={speed:.2f} dur={len(a)/sr:.2f}/{c['slot']:.2f}  {ph}")
json.dump(out, open(f"{outdir}/chunks-measured.json", "w"), ensure_ascii=False, indent=1)
