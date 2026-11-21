/* Petits gestes partagés par les scènes almakanjamil (déterministes, sans horloge). */
(function () {
  if (window.amj) return;
  var amj = {};

  /* Doigt : disque centré sur (x, y) en px de cadre via x/y GSAP. */
  amj.fingerIn = function (tl, f, t, x, y, fromX, fromY) {
    tl.fromTo(f, { x: fromX, y: fromY, opacity: 0, scale: 1 }, { x: x, y: y, opacity: 1, duration: 0.34, ease: "power3.out" }, t);
  };
  amj.moveTo = function (tl, f, t, x, y, d) {
    tl.to(f, { x: x, y: y, duration: d || 0.26, ease: "power2.inOut" }, t);
  };
  /* Appui : l'action se produit à t (doigt enfoncé au plus bas). */
  amj.press = function (tl, f, t) {
    tl.to(f, { scale: 0.82, duration: 0.08, ease: "power2.in" }, t - 0.08);
    tl.to(f, { scale: 1, duration: 0.16, ease: "power2.out" }, t);
  };
  amj.fingerOut = function (tl, f, t, x, y) {
    tl.to(f, { x: x, y: y, opacity: 0, duration: 0.24, ease: "power3.in" }, t);
  };

  /* Apparition floue (titres, valeurs). */
  amj.blurIn = function (tl, el, t, d, blur) {
    tl.fromTo(el, { opacity: 0, filter: "blur(" + (blur || 8) + "px)" }, { opacity: 1, filter: "blur(0px)", duration: d || 0.16, ease: "power2.out" }, t);
  };
  amj.blurOut = function (tl, el, t, d, blur) {
    tl.to(el, { opacity: 0, filter: "blur(" + (blur || 8) + "px)", duration: d || 0.14, ease: "power2.in" }, t);
  };
  amj.wordsIn = function (tl, els, t, gap, d) {
    for (var i = 0; i < els.length; i++) amj.blurIn(tl, els[i], t + i * (gap || 0.07), d);
  };

  window.amj = amj;
})();
