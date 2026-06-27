// Put the Irodori mark next to the book title in the top bar.
// Reuse mdBook's own favicon <link> href so the path is correct at any depth.
(function () {
  function addLogo() {
    var title = document.querySelector(".menu-title");
    if (!title || title.querySelector(".irodori-logo")) return;
    var fav =
      document.querySelector('link[rel="icon"]') ||
      document.querySelector('link[rel="shortcut icon"]');
    var src = fav ? fav.getAttribute("href") : "favicon.svg";
    var img = new Image();
    img.className = "irodori-logo";
    img.src = src;
    img.alt = "";
    title.prepend(img);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addLogo);
  } else {
    addLogo();
  }
})();
