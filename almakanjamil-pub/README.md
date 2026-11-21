# almakanjamil — publicité verticale (HyperFrames)

Vidéo 9:16, 1080 × 1920, 30 fps, 27 s, voix off française. Projet HyperFrames dans `ad/`.

- Vidéo finale : `ad/renders/almakanjamil-pub-9x16.mp4`
- Brief chiffré : `ad/SPEC.md` · Revue et choix : `ad/REVIEW.md`

## Sources visuelles (honnêteté sur ce qui est réel)

| Élément | Origine |
|---|---|
| Photos d'annonces (salon East Park, chambre Toub Ramli, iPhone 16 Pro Max, 3 vignettes vidéo), bannière du Caire | Recadrées depuis les captures de l'app fournies (boutons incrustés retirés par inpainting) |
| Logotype « elmakanjamil », couleurs, Poppins/Inter, icônes Lucide, accueil, recherche, catégories, cartes d'annonces, fiche, boutons Telegram/WhatsApp, formulaire « Déposer une annonce », bascule « Avec l'IA », filtre « Toute l'Égypte / Appliquer », bouton « Carte » | Reconstruits en HTML d'après les captures ; l'accueil est calé au pixel par superposition |
| Carte (fond de plan), menu des villes, panneau IA (zone de texte + « Remplir avec l'IA »), champs Catégorie/Prix, bulles de discussion | **Reconstitués / illustratifs** : écrans non accessibles depuis cet environnement |

Aucune donnée personnelle (nom, numéro, pseudo, e-mail, adresse exacte) n'apparaît. Le domaine affiché et prononcé est uniquement `almakanjamil.com`.

## Régénérer

```bash
npm install                      # hyperframes, gsap, lucide-static
node tools/build.mjs ad/src ad/compositions   # intègre les icônes Lucide dans les scènes
cd ad && npx hyperframes check && npx hyperframes render -o renders/almakanjamil-pub-9x16.mp4 --quality delivery
```

Les scènes s'éditent dans `ad/src/*.html` (sources) ; `ad/compositions/` est généré.

Voix off : `tools/voix-off/` (Kokoro-82M, voix `ff_siwis`, vitesse 1,06, prononciations forcées en phonèmes pour almakanjamil, WhatsApp et IA). Le modèle (~325 Mo) n'est pas versionné.
