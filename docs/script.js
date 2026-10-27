document.addEventListener("DOMContentLoaded", function () {

  /* ---------- Mobile menu toggle ---------- */
  const menuToggle = document.getElementById("menuToggle");
  const topnav = document.getElementById("topnav");
  if (menuToggle && topnav) {
    menuToggle.addEventListener("click", () => {
      const open = topnav.classList.toggle("open");
      menuToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    topnav.querySelectorAll(".topnav-link").forEach((link) => {
      link.addEventListener("click", () => {
        topnav.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
      });
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
    },
    {
      keys: ["class", "diagram", "model", "object"],
      query: "class diagram / object model",
      latency: 142,
      sources: [
        { title: "Class Diagram", section: "Domain entities", snippet: "Defines the core classes including User, Shop, RepairRequest, Guide, and VectorStore." },
        { title: "Class Diagram", section: "Relationships", snippet: "Models associations between registered repair shops, submitted requests, and RAG retrieval logs." }
      ]
    },
    {
      keys: ["deployment", "server", "host", "infrastructure"],
      query: "deployment architecture",
      latency: 165,
      sources: [
        { title: "Deployment Diagram", section: "System topology", snippet: "Illustrates the client browser interacting with the web server, application container, and vector database." },
        { title: "Deployment Diagram", section: "CI/CD execution", snippet: "Shows GitHub Actions runner executing ruff linting and pytest validation on push." }
      ]
    },
    {
      keys: ["sequence", "flow", "interaction", "step"],
      query: "sequence diagram interaction",
      latency: 174,
      sources: [
        { title: "Sequence Diagram", section: "Query handling flow", snippet: "Details the step-by-step message passing between User, Web UI, RAG module, and ChromaDB." },
        { title: "Sequence Diagram", section: "Retrieval latency", snippet: "Tracks synchronous timing constraints for embedding generation and vector similarity search." }
      ]
    },
    {
      keys: ["collaboration", "actor", "component"],
      query: "collaboration diagram",
      latency: 159,
      sources: [
        { title: "Collaboration Diagram", section: "Object interactions", snippet: "Highlights structural organization and object collaborations during repair request processing." },
        { title: "Collaboration Diagram", section: "Shop verification", snippet: "Maps out interactions between admin, shop registry, and verification status updates." }
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
      out.innerHTML = `<p class="demo-empty">No indexed guide matches that yet — try searching for "hinge", "battery", "class diagram", "deployment", "sequence", or "collaboration".</p>`;
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
