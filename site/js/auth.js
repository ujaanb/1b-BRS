/* BRS Study Hub — client-side access gate.
   This is a convenience lock only: the site is static, so anyone who reads the
   page source or requests a file directly can still reach the content. */
(function () {
  "use strict";

  var USER_HASH = "ccd4e04a";
  var PASS_HASH = "5569c1a5";
  var SALT = "brs1b::";

  function hash(value) {
    var h = 5381;
    for (var i = 0; i < value.length; i++) {
      h = ((h << 5) + h + value.charCodeAt(i)) >>> 0;
    }
    return h.toString(16);
  }

  /* Nothing is remembered between page loads: every load, refresh, and
     navigation asks for the credentials again. */
  try {
    window.localStorage.removeItem("brs-access");
  } catch (err) {
    /* storage blocked — nothing to clean up */
  }

  /* A page restored from the back/forward cache does not re-run scripts, so it
     would come back already unlocked. Force a real load instead. */
  window.addEventListener("pageshow", function (event) {
    if (event.persisted) window.location.reload();
  });

  var root = document.documentElement;
  root.className += " brs-locked";

  var style = document.createElement("style");
  style.textContent = [
    "html.brs-locked, html.brs-locked body { overflow: hidden; height: 100%; }",
    "html.brs-locked body > *:not(#brs-gate) { display: none !important; }",
    "#brs-gate { position: fixed; inset: 0; z-index: 2147483647; display: flex;",
    "  align-items: center; justify-content: center; padding: 1.5rem;",
    "  font-family: 'DM Sans', system-ui, sans-serif; color: #0c1f2e;",
    "  background: radial-gradient(1200px 600px at 10% -10%, #c8ebe9 0%, transparent 55%),",
    "    radial-gradient(900px 500px at 100% 0%, #f8d9cf 0%, transparent 45%),",
    "    linear-gradient(180deg, #eef4f6 0%, #f2f6f8 40%, #e8f0f2 100%); }",
    "#brs-gate form { width: 100%; max-width: 21rem; background: #fff; border: 1px solid #d0dde6;",
    "  border-radius: 14px; box-shadow: 0 12px 40px rgba(12,31,46,.08); padding: 1.75rem; }",
    "#brs-gate .brs-mark { font-family: 'Fraunces', Georgia, serif; font-size: 1.5rem; font-weight: 700;",
    "  letter-spacing: .04em; margin: 0; }",
    "#brs-gate .brs-sub { margin: .2rem 0 1.4rem; font-size: .84rem; color: #5a7385; }",
    "#brs-gate label { display: block; font-size: .78rem; font-weight: 600; text-transform: uppercase;",
    "  letter-spacing: .08em; color: #5a7385; margin-bottom: .35rem; }",
    "#brs-gate input { width: 100%; margin-bottom: 1rem; padding: .65rem .75rem; font: inherit;",
    "  font-size: .95rem; color: #0c1f2e; background: #f2f6f8; border: 1px solid #d0dde6;",
    "  border-radius: 9px; }",
    "#brs-gate input:focus { outline: 2px solid #0e7c7b; outline-offset: 1px; background: #fff; }",
    "#brs-gate button { width: 100%; padding: .7rem 1rem; font: inherit; font-size: .95rem;",
    "  font-weight: 600; color: #fff; background: #0e7c7b; border: 0; border-radius: 9px;",
    "  cursor: pointer; }",
    "#brs-gate button:hover { background: #095958; }",
    "#brs-gate .brs-error { min-height: 1.2rem; margin: .7rem 0 0; font-size: .84rem; color: #c44536; }"
  ].join("\n");
  (document.head || root).appendChild(style);

  function build() {
    var gate = document.createElement("div");
    gate.id = "brs-gate";
    gate.innerHTML =
      '<form autocomplete="off">' +
      '<p class="brs-mark">BRS</p>' +
      '<p class="brs-sub">Phase 1B · Imperial — sign in to continue</p>' +
      '<label for="brs-user">Username</label>' +
      '<input id="brs-user" name="brs-user" type="text" autocapitalize="none" spellcheck="false" autofocus />' +
      '<label for="brs-pass">Password</label>' +
      '<input id="brs-pass" name="brs-pass" type="password" />' +
      "<button type=\"submit\">Unlock</button>" +
      '<p class="brs-error" role="alert"></p>' +
      "</form>";
    document.body.appendChild(gate);

    var form = gate.querySelector("form");
    var user = gate.querySelector("#brs-user");
    var pass = gate.querySelector("#brs-pass");
    var error = gate.querySelector(".brs-error");

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var okUser = hash(SALT + user.value.trim().toLowerCase()) === USER_HASH;
      var okPass = hash(SALT + pass.value) === PASS_HASH;
      if (okUser && okPass) {
        root.className = root.className.replace(/\s*brs-locked/, "");
        gate.parentNode.removeChild(gate);
        return;
      }
      error.textContent = "Incorrect username or password.";
      pass.value = "";
      pass.focus();
    });

    user.focus();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();
