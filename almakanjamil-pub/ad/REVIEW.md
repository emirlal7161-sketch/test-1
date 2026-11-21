# REVIEW — publicité almakanjamil 9:16 (27 s)

## Choix créatifs

- **L'app est le décor.** Aucune maquette de téléphone, aucun écran inventé quand l'écran réel existe : l'accueil, la recherche, les catégories, les cartes d'annonces, la fiche, le formulaire et les boutons de contact sont reconstruits d'après les captures et calés au pixel (superposition 50 % contre la capture de l'accueil).
- **Hook = un résultat réel.** Image 0 : la vraie photo du salon East Park, la question « Un T3 meublé au Caire ? » et la fiche « 320 € / mois ». Le prix est surligné quand la voix dit « trois cent vingt euros ».
- **Sous-titres = titres.** Panneaux #281C13, Poppins 800 54 px, un seul mot en orange logo ; en haut du cadre sur les scènes d'interface, en bas sur l'accueil (pour ne pas masquer le logotype).
- **Achat & Vente** passe dans l'orange de la bannière « Commerces locaux » (#D74800) : changement de chapitre lisible, matériau de la marque.
- **Fin performée** : « PUBLICATION GRATUITE » (texte réel du formulaire) → « Gratuit. » → logotype tracé lettre à lettre puis rempli par le bas, barre d'adresse **almakanjamil.com** tapée, baseline réelle « Petites annonces en Égypte », rappel des 4 catégories.
- Transitions, chacune causée à l'écran : balayage vertical, zoom à travers le bouton « Carte », la photo de l'aperçu qui devient la grille, aplat orange au glissement, iris depuis le bouton Telegram touché.
- Lockup final à ~70 % de la largeur (au lieu de 15–30 % recommandés en paysage) : nom long, lu sur téléphone, c'est l'information à retenir.

Pistes non construites : (1) « le chaos des groupes Telegram » → almakanjamil comme solution ; (2) témoignage d'un expatrié qui s'installe. La consigne imposait l'ordre des 8 fonctionnalités : j'ai construit la démonstration produit.

## Mesuré / regardé / non vérifié

- `npx hyperframes check` : 0 erreur (lint, runtime, layout, motion, contraste, audio).
- Fichier rendu (`renders/almakanjamil-pub-9x16.mp4`) : H.264 1080×1920, 30 fps, yuv420p, 27,0 s, AAC 48 kHz stéréo, 11,5 Mo. Audio mesuré par `npx hyperframes audio` : −15,9 LUFS intégré, crête vraie −1,4 dBTP, 0 écrêtage ; silences uniquement aux respirations prévues.
- Positions des cibles des taps mesurées dans le navigateur (getBoundingClientRect), pas estimées.
- Couleurs mesurées en sRGB sur les captures (les captures Safari étaient en Display P3 : converties avant mesure).
- Revue `snapshot --review` (temps forts, 8 coutures, planche téléphone 360 px) lue en entier ; corrections appliquées (décalage dû au zoom CSS, aperçu carte visible trop tôt, sous-titre sur le bouton « Carte », doigt masquant les libellés, inversion de mouvement carte → photos).
- **Voix et sons mesurés, pas écoutés** (aucune écoute possible ici). V2 : voix d'homme Kokoro-82M, timbre `pm_alex` + 22 % de prosodie française, F0 médiane 138 Hz, débit 1,14. Choisie parmi 18 variantes par transcription Whisper small (français) : 0 erreur sur le texte test ; voix off complète retranscrite mot pour mot (marque comprise « Al-Makan Jamil », « Al-MakanJamil.com »). Prononciations forcées : /almakandʒamˈil/, /watsˈap/, /liˈa/.
- Musique V2 : composition originale (FluidSynth + FluidR3_GM, MIT), 122,45 BPM pour que la mesure 13 tombe sur le logotype (attaque mesurée à 23,52 s) ; égalisée pour libérer 150–500 Hz (zone de la voix) et éclaircir le haut du spectre ; atténuée automatiquement sous la voix (compression déclenchée par la voix, ratio 3) : ≈ 14 dB sous la voix pendant la parole, ≈ 8 dB dans les respirations. Mix final retranscrit par Whisper : « Almakanjamil.com » reconnu en toutes lettres ; −15,9 LUFS, crête −1,4 dBTP.

## Plan le plus faible

S2 (recherche) : quatre gestes en 3,5 s (Logements, ville, Appliquer, Carte). Lisible mais dense. Avec l'écran réel des filtres de la page Logements, je le remplacerais par un seul geste fort.
S6 (IA) : le panneau « Avec l'IA » et les champs Catégorie/Prix sont reconstitués ; à valider sur l'écran réel.

## Avertissements gardés volontairement

- `outside_safe_zone` : interface de contexte (en-tête, barre de navigation, textes secondaires des cartes) hors zone sûre TikTok/Reels ; tous les messages clés (sous-titres, prix du hook, logotype, URL) sont dedans.
- `text_below_floor` : faux positif en majorité — le contrôle lit la taille CSS avant le zoom ×2,52 de l'interface. Restent réellement petits les micro-libellés de l'app (« COMMERCES LOCAUX », libellés de navigation), gardés à leur taille réelle par fidélité.
- `line_unread` : défilement « Alexandrie / Gizeh » volontairement rapide (roulette), textes de transition.
- `contrast_aa_failure` sur le logotype : orange de marque #F27528 sur #FCFBF9 (2,76:1) ; un logotype n'est pas modifié.
