import sys, numpy as np, soundfile as sf
vodir, out = sys.argv[1], sys.argv[2]
starts = {"l01":0.15,"l02":1.70,"l03":5.15,"l04":8.60,"l05":10.80,"l06":12.80,"l07":14.60,"l08":16.60,"l09":19.97,"l10":22.77,"l11":24.10}
sr = 24000; total = 28.0
buf = np.zeros(int(total*sr), np.float32); prev = 0
for k, t in starts.items():
    a, r = sf.read(f"{vodir}/{k}.wav", dtype="float32"); i = int(round(t*sr)); assert i >= prev, k
    buf[i:i+len(a)] += a; prev = i + len(a); print(f"{k} {t:.2f} -> {t+len(a)/sr:.2f}")
sf.write(out, buf, sr, subtype="PCM_16")
