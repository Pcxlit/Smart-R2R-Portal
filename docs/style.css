:root {
  --forest: #142B21;
  --forest-soft: #1E3D2E;
  --moss: #3E7C56;
  --moss-deep: #2C5B3F;
  --amber: #E3A73E;
  --rust: #B5652E;
  --paper: #F6F3EA;
  --paper-dim: #ECE6D6;
  --white: #FFFFFF;
  --ink: #16241C;
  --ink-soft: #57685E;
  --line: rgba(22, 36, 28, 0.12);
  --line-dark: rgba(255, 255, 255, 0.12);

  --font-head: 'Space Grotesk', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --radius: 14px;
  --shadow: 0 20px 44px -24px rgba(20, 43, 33, 0.35);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 76px; }

body {
  margin: 0;
  font-family: var(--font-body);
  background: var(--white);
  color: var(--ink);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

a { color: inherit; text-decoration: none; }
h1, h2, h3 { font-family: var(--font-head); color: var(--forest); margin: 0; line-height: 1.1; letter-spacing: -0.01em; }
p { margin: 0; }
code { background: var(--paper-dim); padding: 1px 6px; border-radius: 5px; font-size: 0.9em; }

.container { max-width: 1080px; margin: 0 auto; padding: 0 28px; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .001ms !important; transition-duration: .001ms !important; }
}
:focus-visible { outline: 2px solid var(--moss); outline-offset: 3px; }

/* ============== Navbar ============== */
.navbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  background: rgba(246, 243, 234, 0.86);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}
.nav-inner {
  max-width: 1080px; margin: 0 auto; padding: 0 28px;
  height: 64px; display: flex; align-items: center; justify-content: space-between;
}
.nav-logo { font-family: var(--font-head); font-weight: 700; font-size: 1.05rem; color: var(--forest); }
.nav-links { display: flex; align-items: center; gap: 2px; list-style: none; margin: 0; padding: 0; flex-wrap: wrap; }
.nav-link { font-size: 0.82rem; font-weight: 500; color: var(--ink-soft); padding: 8px 10px; border-radius: 8px; transition: .18s ease; }
.nav-link:hover { color: var(--forest); background: var(--paper-dim); }
.nav-link-ext { color: var(--moss-deep); font-weight: 600; }

.nav-toggle { display: none; flex-direction: column; gap: 4px; background: none; border: none; cursor: pointer; padding: 8px; }
.nav-toggle span { width: 18px; height: 1.5px; background: var(--forest); }

/* ============== Buttons ============== */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 12px 24px; font-family: var(--font-body); font-weight: 600; font-size: 0.92rem;
  border-radius: 999px; border: none; cursor: pointer; transition: .18s ease; white-space: nowrap;
}
.btn-sm { padding: 10px 20px; font-size: 0.86rem; }
.btn-primary { background: var(--amber); color: var(--forest); }
.btn-primary:hover { background: #EFBB5E; }
.btn-outline { background: transparent; color: var(--white); border: 1.5px solid rgba(255,255,255,0.35); }
.btn-outline:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.6); }

/* ============== Hero ============== */
.hero {
  position: relative;
  overflow: hidden;
  background: var(--forest);
  padding: 132px 0 90px;
}
.hero-glow { position: absolute; border-radius: 50%; pointer-events: none; }
.hero-glow-a { width: 480px; height: 480px; background: var(--forest-soft); top: -220px; right: -120px; }
.hero-glow-b { width: 320px; height: 320px; background: var(--moss-deep); bottom: -180px; right: 8%; }

.hero-grid { position: relative; display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center; }

.eyebrow { font-size: 0.8rem; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: var(--amber); margin-bottom: 16px; }
.eyebrow-dark { color: var(--moss-deep); }

.hero h1 { font-size: clamp(2.3rem, 4.6vw, 3.4rem); font-weight: 700; color: #fff; margin-bottom: 20px; }

.hero-sub { font-size: 1.02rem; color: #CBD9CE; max-width: 46ch; line-height: 1.6; margin-bottom: 30px; }

.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px; }

.hero-trust { display: flex; flex-wrap: wrap; gap: 20px; font-size: 0.85rem; color: #ABC2AD; }
.hero-trust span { display: inline-flex; align-items: center; gap: 8px; }
.dot { width: 7px; height: 7px; border-radius: 50%; display: inline-block; }
.dot-moss { background: var(--moss); }
.dot-amber { background: var(--amber); }
.dot-white { background: #fff; }

/* --- Device diagnostic diagram (hero visual) --- */
.hero-visual { display: flex; align-items: center; justify-content: center; min-height: 320px; perspective: 1000px; }
.device-diagram { width: 100%; max-width: 360px; height: auto; transition: transform .15s ease-out; transform: rotateX(4deg) rotateY(-6deg); }

.diagram-ring { fill: none; stroke: rgba(255,255,255,0.12); stroke-width: 1.5; stroke-dasharray: 3 7; }

.laptop-screen { fill: var(--forest-soft); stroke: rgba(255,255,255,0.18); stroke-width: 1.5; }
.laptop-screen-inner { fill: var(--moss-deep); }
.laptop-base { fill: var(--moss); opacity: 0.9; }
.laptop-keys { fill: rgba(255,255,255,0.14); }

.scan-line { fill: var(--amber); opacity: 0.85; animation: scanMove 2.6s ease-in-out infinite; }
@keyframes scanMove {
  0%   { transform: translateY(0); opacity: 0.2; }
  50%  { transform: translateY(64px); opacity: 0.9; }
  100% { transform: translateY(0); opacity: 0.2; }
}

.callout-line { stroke: rgba(227,167,62,0.55); stroke-width: 1.5; stroke-dasharray: 2 4; }
.callout-dot { fill: var(--amber); }
.callout-chip { fill: rgba(255,255,255,0.06); stroke: rgba(227,167,62,0.5); stroke-width: 1.2; }
.callout-text { fill: #fff; font-family: var(--font-body); font-size: 12px; font-weight: 600; }

/* ============== Sections ============== */
.section { padding: 88px 0; }
.section-alt { background: var(--paper-dim); }
.section-dark { background: var(--forest); }

.section-title { font-size: 1.9rem; font-weight: 700; margin-bottom: 14px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.section-title-light { color: #fff; }
.section-desc { font-size: 0.98rem; color: var(--ink-soft); max-width: 60ch; line-height: 1.65; margin-bottom: 44px; }
.section-desc-light { color: #C9D6D2; }

/* ============== "Coming soon" pill ============== */
.soon-pill {
  display: inline-block; font-family: var(--font-body); font-size: 0.62rem; font-weight: 700;
  letter-spacing: .4px; text-transform: uppercase; color: var(--forest); background: var(--amber);
  padding: 4px 10px; border-radius: 999px; vertical-align: middle;
}
.soon-pill-sm { font-size: 0.58rem; padding: 2px 8px; margin-left: 8px; }

/* ============== Status tags ============== */
.status-tag {
  display: inline-block; margin-bottom: 12px; font-size: 0.68rem; font-weight: 700; letter-spacing: .4px;
  text-transform: uppercase; padding: 4px 10px; border-radius: 999px;
}
.status-done { background: rgba(62,124,86,0.15); color: var(--moss-deep); }
.status-progress { background: rgba(227,167,62,0.2); color: #8A6417; }
.status-planned { background: rgba(181,101,46,0.12); color: var(--rust); }

/* ============== Grid & cards ============== */
.grid { display: grid; gap: 18px; }
.grid-4 { grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); }
.grid-3 { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }

.card {
  background: var(--white); border: 1px solid var(--line); border-radius: var(--radius);
  padding: 26px; transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.card-icon {
  width: 42px; height: 42px; display: flex; align-items: center; justify-content: center;
  background: var(--paper-dim); border-radius: 10px; margin-bottom: 16px; color: var(--moss-deep);
}
.card-icon svg { width: 22px; height: 22px; }
.card-icon-lg { width: 52px; height: 52px; margin: 0 auto 16px; background: var(--forest); color: #fff; }
.card-icon-lg svg { width: 26px; height: 26px; }

.card h3 { font-size: 1.02rem; font-weight: 600; margin-bottom: 6px; }
.card p { font-size: 0.88rem; color: var(--ink-soft); line-height: 1.55; }

.card-link:hover { border-color: var(--moss); transform: translateY(-3px); box-shadow: var(--shadow); }
.card-center { text-align: center; }

.tag {
  display: inline-block; margin-top: 12px; font-size: 0.65rem; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; padding: 3px 9px; border-radius: 5px; background: rgba(62,124,86,0.12); color: var(--moss-deep);
}

.avatar {
  width: 56px; height: 56px; border-radius: 50%; background: var(--forest); color: #fff;
  display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.95rem;
  margin: 0 auto 14px;
}

/* ============== Demo ============== */
.demo-card {
  background: var(--forest-soft); border: 1px solid var(--line-dark); border-radius: var(--radius);
  padding: 28px; max-width: 760px;
}
.demo-search {
  display: flex; flex-direction: column; gap: 14px; background: rgba(255,255,255,0.05);
  border: 1px solid var(--line-dark); border-radius: 14px; padding: 18px 20px;
}
.demo-form { display: flex; gap: 10px; align-items: center; }
.demo-search-icon { width: 18px; height: 18px; color: #A9C2AC; flex-shrink: 0; }
.demo-form input {
  flex: 1; background: transparent; border: none; border-bottom: 1.5px solid var(--line-dark);
  outline: none; color: #fff; font-family: var(--font-body); font-size: 0.95rem; padding: 8px 4px; min-width: 0;
}
.demo-form input::placeholder { color: #8FA391; }
.demo-chip-row { display: flex; flex-wrap: wrap; gap: 10px; }
.demo-chip {
  font-family: var(--font-body); font-weight: 600; font-size: 0.82rem; padding: 8px 14px;
  border-radius: 999px; border: 1.5px solid var(--moss); background: transparent; color: #86D6A5;
  cursor: pointer; transition: .18s ease;
}
.demo-chip:hover { background: var(--moss); color: #fff; }

.demo-output { margin-top: 20px; display: flex; flex-direction: column; gap: 12px; }
.demo-meta { font-size: 0.8rem; color: #A9C2AC; margin-bottom: 4px; }
.demo-source {
  background: rgba(255,255,255,0.05); border: 1px solid var(--line-dark); border-radius: 10px;
  padding: 14px 18px;
}
.demo-source h4 { font-family: var(--font-head); font-size: 0.92rem; font-weight: 600; color: #fff; margin-bottom: 2px; }
.demo-source .section-label { font-size: 0.76rem; color: var(--amber); font-weight: 600; margin-bottom: 6px; display: block; }
.demo-source p { font-size: 0.85rem; color: #C9DACB; line-height: 1.5; }

.demo-generated {
  margin-top: 6px; border: 1.5px dashed rgba(227,167,62,0.5); border-radius: 10px; padding: 16px 18px;
  display: flex; align-items: center; gap: 12px; background: rgba(227,167,62,0.06);
}
.demo-generated p { font-size: 0.85rem; color: #E8D2A0; }

.demo-empty { color: #A9C2AC; font-size: 0.9rem; padding: 4px; }
.demo-note { margin-top: 18px; font-size: 0.78rem; color: #8FA391; }

/* ============== Pipeline ============== */
.flow-pipeline { max-width: 640px; }
.flow-step { display: flex; gap: 18px; align-items: flex-start; }
.flow-step-number {
  flex-shrink: 0; width: 36px; height: 36px; border-radius: 50%; background: var(--moss); color: #fff;
  display: flex; align-items: center; justify-content: center; font-family: var(--font-head); font-weight: 700; font-size: 0.9rem;
}
.flow-step-content { flex: 1; padding-bottom: 6px; }
.flow-step-content h3 { font-size: 1rem; font-weight: 600; margin-bottom: 5px; display: flex; align-items: center; }
.flow-step-content p { font-size: 0.88rem; color: var(--ink-soft); line-height: 1.55; }
.flow-connector { width: 1.5px; height: 24px; margin-left: 17px; background: var(--moss); opacity: 0.3; }

/* ============== Footer ============== */
.footer { background: var(--forest); padding: 46px 0; text-align: center; }
.footer-logo { font-family: var(--font-head); font-size: 1.05rem; font-weight: 700; color: #fff; }
.footer-text { font-size: 0.85rem; color: #ABC2AD; margin: 6px 0 18px; }
.footer-links { display: flex; gap: 22px; justify-content: center; flex-wrap: wrap; }
.footer-links a { font-size: 0.85rem; color: #8FA391; transition: .18s ease; }
.footer-links a:hover { color: #fff; }

/* ============== Fade-in ============== */
.fade-in { opacity: 0; transform: translateY(16px); transition: opacity .5s ease, transform .5s ease; }
.fade-in.visible { opacity: 1; transform: translateY(0); }

/* ============== Responsive ============== */
@media (max-width: 860px) {
  .hero-grid { grid-template-columns: 1fr; }
  .hero-visual { order: -1; min-height: 240px; }
  .device-diagram { max-width: 280px; }

  .nav-toggle { display: flex; }
  .nav-links {
    position: fixed; top: 0; right: -100%; width: 240px; height: 100vh;
    background: var(--paper); flex-direction: column; align-items: flex-start; gap: 2px;
    padding: 76px 24px 24px; border-left: 1px solid var(--line); transition: .3s ease;
    overflow-y: auto;
  }
  .nav-links.open { right: 0; }
  .nav-link { width: 100%; padding: 10px 12px; }
}

@media (max-width: 520px) {
  .demo-form { flex-wrap: wrap; }
  .demo-form input { width: 100%; order: 1; }
  .demo-search-icon { order: 0; }
  .demo-form .btn { order: 2; width: 100%; }
}
