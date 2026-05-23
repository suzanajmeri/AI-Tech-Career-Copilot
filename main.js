function renderCards(containerId, items, titleKey = "title", descKey = "desc") {
  const el = document.getElementById(containerId);
  if (!el) return;
  el.innerHTML = (items || []).map(item => `
    <div class="card">
      <div class="card-title">${item[titleKey] ?? ""}</div>
      <div class="card-sub">${item[descKey] ?? ""}</div>
    </div>
  `).join("") || `<div class="empty">No results.</div>`;
}

// Career recommender
async function getCareer() {
  const skills = document.getElementById("skillInput").value.trim();
  const res = await fetch("/api/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ skills })
  });
  const { careers } = await res.json();
  const items = (careers || []).map(c => ({
    title: c.career,
    desc: c.feature || ""
  }));
  renderCards("result", items);
}

// Roadmap
async function getRoadmap() {
  const career = document.getElementById("careerInput").value.trim();
  const res = await fetch("/api/roadmap", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ career })
  });
  const { steps } = await res.json();
  const items = (steps || []).map((s, i) => ({
    title: `Step ${i + 1}`,
    desc: s.step
  }));
  renderCards("roadmapBox", items);
}

// Skill explorer
async function exploreSkill() {
  const skill = document.getElementById("explorerInput").value.trim();
  const res = await fetch("/api/explore", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ skill })
  });
  const { careers = [], resources = [] } = await res.json();

  const careerItems = careers.map(name => ({ title: name, desc: "Relevant role" }));
  renderCards("explorerResult", careerItems);

  const resultEl = document.getElementById("explorerResult");
  if (resources.length) {
    const links = resources.map(r => `<li><a href="${r.url}" target="_blank">${r.title}</a></li>`).join("");
    resultEl.innerHTML += `
      <div class="card">
        <div class="card-title">Learning Resources</div>
        <ul class="link-list">${links}</ul>
      </div>
    `;
  }
}

// Chat
let voiceEnabled = false;

function pushChat(role, text) {
  const box = document.getElementById("chatBox");
  if (!box) return;
  const cls = role === "user" ? "bubble user" : "bubble ai";
  box.innerHTML += `<div class="${cls}">${(text || "").replace(/\n/g, "<br>")}</div>`;
  box.scrollTop = box.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("userMessage");
  const message = input.value.trim();
  if (!message) return;

  pushChat("user", message);
  input.value = "";

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const { reply } = await res.json();
    pushChat("ai", reply);

    if (voiceEnabled && "speechSynthesis" in window) {
      const utter = new SpeechSynthesisUtterance(reply);
      speechSynthesis.speak(utter);
    }
  } catch (err) {
    pushChat("ai", "Sorry, something went wrong. Please try again.");
    console.error(err);
  }
}

function toggleVoice() {
  voiceEnabled = !voiceEnabled;
  const btn = document.getElementById("voiceToggleBtn");
  if (btn) {
    btn.textContent = `Voice: ${voiceEnabled ? "On" : "Off"}`;
  }
}

// ----- Universal Enter Key Support -----
document.addEventListener("DOMContentLoaded", () => {
  // Career Recommender
  const skillInput = document.getElementById("skillInput");
  if (skillInput) {
    skillInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") getCareer();
    });
  }

  // Roadmap
  const careerInput = document.getElementById("careerInput");
  if (careerInput) {
    careerInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") getRoadmap();
    });
  }

  // Skill Explorer
  const explorerInput = document.getElementById("explorerInput");
  if (explorerInput) {
    explorerInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") exploreSkill();
    });
  }

  // Chatbot
  const userMessage = document.getElementById("userMessage");
  if (userMessage) {
    userMessage.addEventListener("keydown", (event) => {
      if (event.key === "Enter") sendMessage();
    });
  }
});