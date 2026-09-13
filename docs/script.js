document.addEventListener("DOMContentLoaded", function () {

  /* ---------- Mobile rail toggle ---------- */
  const railToggle = document.getElementById("railToggle");
  const rail = document.getElementById("rail");
  if (railToggle && rail) {
    railToggle.addEventListener("click", () => {
      const open = rail.classList.toggle("open");
      railToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    rail.querySelectorAll(".rail-link").forEach((link) => {
      link.addEventListener("click", () => {
        rail.classList.remove("open");
        railToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- Active section highlight in rail ---------- */
  const railLinks = document.querySelectorAll(".rail-link[href^='#']");
  const sections = Array.from(railLinks)
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);
  if ("IntersectionObserver" in window && sections.length) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const id = `#${entry.target.id}`;
            railLinks.forEach((link) => {
              link.classList.toggle("active", link.getAttribute("href") === id);
            });
          }
        });
      },
      { rootMargin: "-40% 0px -55% 0px" }
    );
    sections.forEach((el) => sectionObserver.observe(el));
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

    let html = `<p class="demo-meta">query: "${escapeHtml(inputText)}" · retrieved in ${data.latency}ms</p>`;
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
