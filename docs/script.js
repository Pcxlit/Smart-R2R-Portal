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

  /* ---------- Hero laptop diagram parallax ---------- */
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

  /* ---------- Assistant demo ----------
     These are saved example outputs. Replace the answer, chunk text and
     timings below with real results from your pipeline for best accuracy. */
  const RAG_DEMO = [
    {
      keys: ["hinge", "creak", "loose", "wobbl"],
      retrieveMs: 187,
      totalSec: 1.9,
      answer:
        "A loose, creaking hinge usually means worn screws or a damaged bracket. First, check the screw holes in the hinge bracket for damage. If tightening the screws does not hold, the bracket most likely needs to be replaced.",
      sources: ["Hinge Repair Guide"],
      chunks: [
        { title: "Hinge Repair Guide", section: "Diagnosing hinge play", snippet: "Check for stripped screw holes in the hinge bracket before ordering a replacement part." },
        { title: "Hinge Repair Guide", section: "Tightening vs. replacing", snippet: "If tightening the hinge screws doesn't hold, the bracket most likely needs replacing." }
      ]
    },
    {
      keys: ["battery", "swell", "drain", "charge"],
      retrieveMs: 152,
      totalSec: 1.7,
      answer:
        "Stop using the laptop right away if the battery looks swollen or the trackpad is being pushed up. Before you take out anything else inside the laptop, disconnect the battery connector. Then follow the safe removal steps in the guide.",
      sources: ["Battery Replacement Guide"],
      chunks: [
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
      out.innerHTML = `<p class="demo-empty">No matching guide found for that question. Only the hinge and battery guides are included in this demo, so try one of those.</p>`;
      return;
    }

    let html = `<p class="demo-meta">Question: "${escapeHtml(inputText)}" &middot; found in ${data.retrieveMs}ms &middot; answered in ${data.totalSec}s</p>`;

    html += `
      <div class="demo-answer">
        <span class="demo-label">Answer</span>
        <p>${data.answer}</p>
      </div>`;

    html += `<div class="demo-sources-row"><span class="demo-label">Sources</span>`;
    data.sources.forEach((s) => {
      html += `<span class="source-chip">${s}</span>`;
    });
    html += `</div>`;

    html += `<span class="demo-label demo-chunks-title">Text the answer was based on</span>`;
    data.chunks.forEach((c) => {
      html += `
        <div class="demo-source">
          <h4>${c.title}</h4>
          <span class="section-label">${c.section}</span>
          <p>${c.snippet}</p>
        </div>`;
    });

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

  // show the first example on load
  renderDemo("hinge is loose and creaking");
});
