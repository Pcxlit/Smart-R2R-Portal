document.addEventListener("DOMContentLoaded", function () {

  /* ---------- Mobile nav toggle ---------- */
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => navLinks.classList.toggle("open"));
    navLinks.querySelectorAll(".nav-link").forEach((link) => {
      link.addEventListener("click", () => navLinks.classList.remove("open"));
    });
  }

  /* ---------- Fade-in on scroll ---------- */
  const fadeEls = document.querySelectorAll(".fade-in");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    fadeEls.forEach((el) => observer.observe(el));
  } else {
    fadeEls.forEach((el) => el.classList.add("visible"));
  }

  /* ---------- Hero device diagram parallax ---------- */
  const diagram = document.getElementById("deviceDiagram");
  const visual = document.getElementById("heroVisual");
  if (diagram && visual && matchMedia("(prefers-reduced-motion: no-preference)").matches) {
    visual.addEventListener("pointermove", (e) => {
      const rect = visual.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width - 0.5;
      const py = (e.clientY - rect.top) / rect.height - 0.5;
      diagram.style.transform = `rotateX(${4 - py * 10}deg) rotateY(${-6 + px * 16}deg)`;
    });
    visual.addEventListener("pointerleave", () => {
      diagram.style.transform = "rotateX(4deg) rotateY(-6deg)";
    });
  }

  /* ---------- Retrieval demo (real retrieval behavior, mocked here) ---------- */
  const RAG_DEMO = [
    {
      keys: ["hinge", "creak", "loose", "wobbl"],
      query: "hinge is loose and creaking",
      latency: 187,
      sources: [
        { title: "Hinge Repair Guide", section: "Diagnosing hinge play", snippet: "Check for stripped screw holes in the hinge bracket before ordering a replacement part." },
        { title: "Hinge Repair Guide", section: "Tightening vs. replacing", snippet: "If tightening the hinge screws doesn't hold, the bracket most likely needs replacing." }
      ]
    },
    {
      keys: ["battery", "swell", "drain", "charge"],
      query: "battery drains fast / feels swollen",
      latency: 152,
      sources: [
        { title: "Battery Replacement Guide", section: "Signs of battery swelling", snippet: "Stop using the device immediately if the battery is visibly swollen or the trackpad is pushed up." },
        { title: "Battery Replacement Guide", section: "Safe removal steps", snippet: "Disconnect the battery connector before removing any other internal components." }
      ]
    }
  ];

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function matchDemo(text) {
    const q = text.toLowerCase();
    return RAG_DEMO.find((d) => d.keys.some((k) => q.includes(k)));
  }

  function renderDemo(inputText) {
    const out = document.getElementById("demoOutput");
    const data = matchDemo(inputText);

    if (!data) {
      out.innerHTML = `<p class="demo-empty">No indexed guide matches that yet — only "hinge" and "battery" topics are ingested so far. Try one of those.</p>`;
      return;
    }

    let html = `<p class="demo-meta">Query: "${escapeHtml(inputText)}" &middot; retrieved in ${data.latency}ms</p>`;
    data.sources.forEach((s) => {
      html += `
        <div class="demo-source">
          <h4>${s.title}</h4>
          <span class="section-label">${s.section}</span>
          <p>${s.snippet}</p>
        </div>`;
    });
    html += `
      <div class="demo-generated">
        <span class="soon-pill">Coming soon</span>
        <p>Generated answer synthesis is not wired in yet — this step is gated behind retrieval quality validation.</p>
      </div>`;
    out.innerHTML = html;
  }

  const demoForm = document.getElementById("demoForm");
  const demoInput = document.getElementById("demoInput");
  if (demoForm && demoInput) {
    demoForm.addEventListener("submit", (e) => {
      e.preventDefault();
      renderDemo(demoInput.value.trim() || "hinge is loose");
    });
  }

  document.querySelectorAll(".demo-chip").forEach((chip) => {
    chip.addEventListener("click", () => {
      const text = chip.dataset.demo;
      if (demoInput) demoInput.value = text;
      renderDemo(text);
    });
  });

  // seed with the first example on load
  renderDemo("hinge is loose and creaking");
});
