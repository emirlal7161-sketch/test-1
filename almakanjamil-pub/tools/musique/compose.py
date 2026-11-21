# Musique originale de la pub (composée par programme, rendue avec FluidSynth + FluidR3_GM, licence MIT).
# 122,449 BPM : 1 mesure = 1,96 s, donc la mesure 13 commence à 23,52 s = atterrissage du logotype.
import sys
import mido

out_mid = sys.argv[1]
TPB = 480
BPM = 60 / (1.96 / 4)
mid = mido.MidiFile(ticks_per_beat=TPB)
events = []  # (tick, channel, type, note, vel)


def note(beat, dur, ch, n, vel):
    t0 = int(round(beat * TPB)); t1 = int(round((beat + dur) * TPB))
    events.append((t0, ch, "on", n, vel)); events.append((t1, ch, "off", n, 0))


# Canaux / programmes GM
PIANO, BASS, MARIMBA, STRINGS, PLUCK, DRUM = 0, 1, 2, 3, 4, 9
programs = {PIANO: 1, BASS: 33, MARIMBA: 12, STRINGS: 48, PLUCK: 45}

C, G, Am, F = "C", "G", "Am", "F"
prog = [C, G, Am, F] * 3  # mesures 1 à 12, puis mesure 13 = accord final (Do)
piano = {C: [64, 67, 72], G: [62, 67, 71], Am: [64, 69, 72], F: [65, 69, 72]}
root = {C: 36, G: 43, Am: 45, F: 41}
pad = {C: [48, 55, 64], G: [47, 55, 62], Am: [45, 52, 60], F: [45, 53, 60]}
arp = {C: [72, 76, 79, 84, 79, 76, 84, 79], G: [71, 74, 79, 83, 79, 74, 83, 79],
       Am: [72, 76, 81, 84, 81, 76, 84, 81], F: [72, 77, 81, 84, 81, 77, 84, 81]}

for bar, ch in enumerate(prog):  # bar 0..11
    b0 = bar * 4
    build = bar >= 10  # mesures 11-12 : montée sans grosse caisse
    # Batterie
    for beat in range(4):
        if not build and beat in (0, 2):
            note(b0 + beat, 0.25, DRUM, 36, 112)            # grosse caisse
        if not build and beat == 3 and bar % 2 == 1:
            note(b0 + 3.5, 0.25, DRUM, 36, 90)               # relance
        if beat in (1, 3):
            note(b0 + beat, 0.25, DRUM, 39, 96 if not build else 84)  # clap
            note(b0 + beat, 0.25, DRUM, 38, 70 if not build else 60)  # caisse claire en doublure
        for half in (0, 0.5):
            v = 58 if half == 0 else 76
            note(b0 + beat + half, 0.2, DRUM, 42, v)         # charleston fermé
    if bar % 4 == 3 and not build:
        note(b0 + 3.5, 0.45, DRUM, 46, 70)                   # charleston ouvert fin de phrase
    if bar == 11:                                            # roulement montant vers le logo
        for i in range(8):
            note(b0 + 2 + i * 0.25, 0.2, DRUM, 38, 60 + i * 8)
    if bar in (0, 4, 8):
        note(b0, 1.5, DRUM, 49, 92)                          # cymbale de début de phrase
    # Basse en octaves (rebond « joyeux »)
    r = root[ch]
    if not build:
        for i in range(8):
            note(b0 + i * 0.5, 0.42, BASS, r if i % 2 == 0 else r + 12, 96 if i % 2 == 0 else 80)
    else:
        note(b0, 3.9, BASS, r, 92)
    # Piano : rythme 3-3-2 (1, et du 2, 4)
    for pos in (0, 1.5, 3):
        for n in piano[ch]:
            note(b0 + pos, 0.35, PIANO, n, 84)
    # Marimba en arpèges dès la mesure 3
    if 2 <= bar <= 9:
        for i, n in enumerate(arp[ch]):
            note(b0 + i * 0.5, 0.4, MARIMBA, n, 74 if i % 2 == 0 else 62)
    # Nappe de cordes discrète
    if bar >= 4:
        for n in pad[ch]:
            note(b0, 3.95, STRINGS, n, 46 if not build else 60)
    # Pizzicati en montée sur les mesures 11-12
    if build:
        for i in range(8):
            note(b0 + i * 0.5, 0.3, PLUCK, piano[ch][i % 3] + (12 if bar == 11 and i >= 4 else 0), 70 + i * 4)

# Mesure 13 : accord final sur le logo (23,52 s), qui résonne jusqu'à la fin
b13 = 48
note(b13, 0.3, DRUM, 36, 120); note(b13, 3.0, DRUM, 49, 110); note(b13, 0.3, DRUM, 39, 100)
for n in [36, 48]:
    note(b13, 5.6, BASS, n, 100)
for n in [60, 64, 67, 72, 76]:
    note(b13, 5.6, PIANO, n, 92)
for n in [48, 55, 64, 72]:
    note(b13, 5.6, STRINGS, n, 74)
for i, n in enumerate([72, 76, 79, 84]):
    note(b13 + i * 0.25, 0.6, MARIMBA, n, 80)

track = mido.MidiTrack(); mid.tracks.append(track)
track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM), time=0))
for ch, p in programs.items():
    track.append(mido.Message("program_change", channel=ch, program=p, time=0))
track.append(mido.Message("control_change", channel=STRINGS, control=7, value=86, time=0))
track.append(mido.Message("control_change", channel=PIANO, control=7, value=100, time=0))
track.append(mido.Message("control_change", channel=MARIMBA, control=7, value=96, time=0))
track.append(mido.Message("control_change", channel=BASS, control=7, value=108, time=0))
events.sort(key=lambda e: (e[0], 0 if e[2] == "off" else 1))
now = 0
for t, ch, kind, n, v in events:
    msg = mido.Message("note_on" if kind == "on" else "note_off", channel=ch, note=n, velocity=v, time=t - now)
    track.append(msg); now = t
mid.save(out_mid)
print(f"{BPM:.3f} BPM, {len(events)//2} notes, durée {mido.MidiFile(out_mid).length:.2f} s")
