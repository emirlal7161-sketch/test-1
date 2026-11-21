# SPEC — Publicité almakanjamil (9:16)

GOAL:    à la fin, le spectateur francophone installé (ou qui s'installe) en Égypte retient « almakanjamil.com »
         et sait qu'il y trouve un logement, vend ses objets, publie avec l'IA et contacte en direct, gratuitement.
OUTPUT:  HyperFrames 0.9.75, 1080 × 1920, 30 fps, MP4 H.264 + AAC.
TIME:    27,0 s × 30 = 810 frames. Pas de musique (aucune source de musique licenciée accessible) :
         la voix off est l'horloge ; effets sonores HyperFrames (licence Pixabay) sur les actions visibles.

## LOOK — l'app elle-même est le décor

- Sol : #FCFBF9 (fond réel de l'app). Surfaces : #FFFFFF. Bordures : #E9E2DB (champs), #EDE7E2 (boutons).
- Encres : #101C29 (contenus : prix, titres, catégories), #281C13 (interface : nav, formulaires), gris #675B52.
- Accent unique : #C84606 (primaire réel, mesuré en sRGB sur 5 captures). Il ne marque que l'élément actif du plan
  (contrôle touché, repère sélectionné). Orange vif #D74800 : bouton alerte et bannière, comme dans l'app.
  Orange logo #F27528 : uniquement le logotype.
- Pastilles : fond #DFEDF9, icône #C84606, texte #101C29. Tuiles catégories et barre de recherche : #F1F3F5.
- Typo : Poppins 800 (titres, prix), 700 (surtitres en capitales), 600 (logotype) ; Inter 400/500/600 (texte).
  Sous-titres : Poppins 800, 58 px, blanc, sur panneau #281C13 à 94 %, rayon 26 px, marge 20/34 px.
- Matière : l'UI réelle reconstruite en HTML à l'échelle téléphone (zoom CSS 2,2 à 2,6 px par pt),
  icônes Lucide v1.77 (celles de l'app), photos réelles d'annonces (rayon 12 pt).
- Profondeur : ombres de l'app 0 1px 2px rgba(16,28,41,.06) ; carte soulevée 0 22px 48px rgba(40,28,19,.18).
- Doigt : disque blanc 78 px (7 % de la largeur), bord 2 px rgba(40,28,19,.14), ombre 0 10px 24px rgba(40,28,19,.25),
  appui = échelle 1 → 0,84 en 0,08 s puis retour 0,14 s. Pas d'anneau de clic.

## OBJETS (tous issus des captures de l'app, sauf mention)

- Logotype « elmakanjamil » (orthographe exacte du header de l'app), Poppins 600, #F27528.
- Barre de recherche « Rechercher sur almakanjamil » + bouton flèche #C84606.
- Catégories : Logements, Achat & Vente, Véhicules, Électroménager, Autres (tuiles 38 pt, icônes Lucide).
- Filtre réel : « Toute l'Égypte » (fond #DFEDF9, chevron) + bouton « Appliquer » (#FFE9D9 / texte #953208).
- Cartes annonces : photo, prix Poppins 800, titre, catégorie, pastilles (Meublé, 3 pièces, Balcon, 185 m², tag),
  lieu (map-pin), date grise. Bouton flottant « Carte » + cloche orange.
- Fiche annonce : photo + carte blanche, « 320 € / mois », « 110 € / semaine », boutons Telegram / Telegram Femme /
  Telegram Homme / WhatsApp Femme (send / message-circle).
- Formulaire « PUBLICATION GRATUITE — Déposer une annonce », bascule « À la main » / « Avec l'IA ».
- Photos réelles : salon East Park, chambre Toub Ramli, iPhone 16 Pro Max, vignettes vidéo (porte, couloir, compound).
- RECONSTITUÉ (non accessible, à valider) : la carte (fond de plan illustratif façon OSM, sans rue réelle),
  le menu déroulant des villes, le panneau « Avec l'IA » (zone de texte + bouton), le formulaire Achat & Vente
  (Catégorie, Prix), les bulles de message. Aucun numéro, pseudo, e-mail ou adresse réelle n'apparaît.

## MOTION

- Arrivées : expo.out / power4.out, 0,35–0,6 s. Caméra : power2.inOut, 0,5–0,9 s. Sorties : power3.in, 0,18–0,3 s.
- Ressorts UI interdits (pas de rebond sur l'UI). Pop des prix/repères : back.out(1.4) sur l'échelle seulement.
- Titres : flou 8 px → 0 + opacité en 0,16 s, mot à mot 0,07 s. Un titre posé ne bouge plus.
- Chevauchement : l'élément suivant démarre à 40 % du précédent. Stagger listes 0,06 s, repères 0,09 s.
- Transitions (5 sortes, chacune causée à l'écran) : balayage vertical (S1→S2), zoom à travers le bouton « Carte »
  (S2→S3), l'objet devient le monde (aperçu → grille, S3→S4), aplat de couleur qui se contracte dans la tuile
  « Achat & Vente » (S4→S5), iris depuis le bouton touché (S7→S8). Balayages internes ailleurs.

## SHOTS (temps globaux ; voix = horloge)

| Plan | Frames | Héros | Lecture (fenêtre) | Son | Passage |
|---|---|---|---|---|---|
| S1 Hook | 0–103 | Photo salon plein cadre, poussée 1,00→1,07 | « Un T3 meublé / au Caire ? » + fiche réelle « 320 € / mois » visibles dès f0 ; surligneur pêche tracé sous le prix à 1,75 s | v1a 0,20 / v1b 1,70 ; pop 1,75 | balayage vers le haut |
| S2 Recherche | 104–207 | Accueil réel : logotype, recherche, catégories → tap Logements (4,95) → liste ; filtre Toute l'Égypte → Le Caire (5,9) → Appliquer (6,2) | ST « Il est sur almakanjamil. » 3,55–5,33 ; « Filtrez par ville, » 5,40–6,93 | v2a 3,55 / v2b 5,40 ; clics 4,92 · 5,47 · 6,09 · 6,55 | caméra ×1,3 centrée sur « Carte », puis zoom à travers |
| S3 Carte | 208–272 | Fond de plan + 6 repères de prix réels, cercle 1 km, tap 320 € (8,05) → aperçu chambre | ST « et repérez chaque annonce » 6,95–7,95 ; « sur la carte. » 7,95–9,05 | v2c 6,95 ; pops 7,10→7,55 ; clic 8,05 · 8,75 | l'aperçu devient la grille |
| S4 Photos | 273–369 | Grande photo de la chambre tenue 0,15 s (« Photos »), rangée dans la grille 2 colonnes de vraies annonces (3 rangées), défilement −1000 px, tap vidéo compound (11,15) → agrandie ×1,5 | ST « Photos, vidéos : » 9,20–10,20 ; « visitez avant même de vous déplacer. » 10,25–12,30 | v3a 9,20 / v3b 10,25 ; whoosh 9,10 ; clic 11,0 | aplat orange |
| S5 Achat & Vente | 370–440 | Aplat #C84606 qui se contracte dans la tuile Achat & Vente ; carte iPhone 39 000 EGP ; tap Véhicules (13,85) | ST « Vous vendez un téléphone, » 12,45–13,55 ; « une voiture ? » 13,55–14,70 | v4a 12,45 ; pop 12,95 ; clic 13,85 | balayage vers le haut |
| S6 IA | 441–553 | Formulaire réel ; tap « Avec l'IA » (14,95) ; message Telegram glisse dans la zone (15,55–16,0) ; tap Remplir (16,45) ; 5 champs remplis (16,75→17,75) | ST « Collez votre message Telegram : » 14,80–16,65 ; « l'IA remplit l'annonce pour vous. » 16,70–18,45 | v5a 14,80 / v5b 16,70 ; clics ; frappe | balayage vers le haut |
| S7 Contact | 554–644 | Fiche salon, rangée de boutons réels ; tap Telegram (18,85) → bulle ; tap WhatsApp Femme (19,95) → réponse | ST « Contact direct, » 18,60–19,75 ; « sur WhatsApp ou Telegram. » 19,80–21,50 | v6a 18,60 / v6b 19,80 ; clics ; pops | iris depuis WhatsApp |
| S8 Fin | 639–809 | Iris depuis Telegram (21,30–21,56) ; « PUBLICATION GRATUITE » + « Gratuit. » (21,54–22,9) ; logotype tracé puis rempli par le bas (22,80–23,52) ; barre d'adresse « almakanjamil.com » tapée (23,40–23,97) ; « Petites annonces en Égypte » (24,25) ; rappel des 4 catégories réelles (24,55) | tenue finale 2,5 s | v7a 21,65 / v7b 23,10 ; montée + impact 23,53 | fin |

## VOIX OFF (Kokoro-82M, voix ff_siwis, vitesse 1,06 ; prononciations forcées en phonèmes)

| id | début | durée | texte |
|---|---|---|---|
| v1a | 0,20 | 1,39 | Un T3 meublé au Caire, |
| v1b | 1,70 | 1,49 | à trois cent vingt euros par mois ? |
| v2a | 3,55 | 1,48 | Il est sur almakanjamil. (/almakandʒamˈil/) |
| v2b | 5,40 | 1,06 | Filtrez par ville, |
| v2c | 6,95 | 1,89 | et repérez chaque annonce sur la carte. |
| v3a | 9,20 | 0,93 | Photos, vidéos : |
| v3b | 10,25 | 1,83 | visitez avant même de vous déplacer. |
| v4a | 12,45 | 1,99 | Vous vendez un téléphone, une voiture ? |
| v5a | 14,80 | 1,77 | Collez votre message Telegram : |
| v5b | 16,70 | 1,44 | l'IA remplit l'annonce pour vous. (/liˈa/) |
| v6a | 18,60 | 1,09 | Contact direct, |
| v6b | 19,80 | 1,41 | sur WhatsApp ou Telegram. (/watsˈap/) |
| v7a | 21,65 | 0,89 | Et c'est gratuit. |
| v7b | 23,10 | 1,42 | almakanjamil point com. |

## BANNED

Fond sombre vide ; lueurs, néons, particules ; dégradés violets ; cartes de verre ; tout qui entre en fondu-montée ;
titres qui dérivent ; logo dans un coin ; maquette de téléphone inclinée en 3D ; tableau de bord inventé ;
« almakanjamil.lovable.app » (où que ce soit) ; toute donnée personnelle (nom, numéro, pseudo, e-mail, adresse exacte) ;
le repère de localisation exacte de la capture du formulaire ; anneaux de clic ; bip/carillon synthétiques.

## QA

- f0 : photo + « Un T3 meublé au Caire ? » lisibles (miniature).
- 4,4 s : logotype « elmakanjamil » + « Rechercher sur almakanjamil » nets.
- 5,95 s : sélecteur affiche « Le Caire ». 7,7 s : 6 repères lisibles. 8,4 s : aperçu chambre 320 €.
- 11,6 s : vignette vidéo compound grande. 13,2 s : carte iPhone 39 000 EGP. 17,9 s : 5 champs remplis.
- 20,5 s : bulle de réponse. 25,5 s : logotype + almakanjamil.com + baseline, centrés.
- Recherche texte : 0 occurrence de « lovable » dans compositions/ et index.html.
- Audio : voix présente de 0,2 à 24,5 s, crête ≤ −1 dBTP, intégré ≈ −16 LUFS.
