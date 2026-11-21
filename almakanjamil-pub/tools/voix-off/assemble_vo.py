import sys, json, numpy as np, soundfile as sf
vodir, out = sys.argv[1], sys.argv[2]
starts = {"v1a":0.20,"v1b":1.70,"v2a":3.55,"v2b":5.40,"v2c":6.95,"v3a":9.20,"v3b":10.25,"v4a":12.45,
          "v5a":14.80,"v5b":16.70,"v6a":18.60,"v6b":19.80,"v7a":21.65,"v7b":23.10}
sr = 24000; total = 27.0
buf = np.zeros(int(total*sr), np.float32)
meas = {m["id"]: m for m in json.load(open(f"{vodir}/chunks-measured.json"))}
prev_end = 0
rows = []
for k, t in starts.items():
    a, r = sf.read(f"{vodir}/{k}.wav", dtype="float32"); assert r == sr
    i = int(round(t*sr)); assert i >= prev_end, (k, "overlap")
    buf[i:i+len(a)] += a; prev_end = i + len(a)
    rows.append((k, t, round(t+len(a)/sr, 3)))
sf.write(out, buf, sr, subtype="PCM_16")
for r in rows: print("%s %.2f -> %.2f" % r)
