const format = (value) => JSON.stringify(value, null, 2);

async function readJson(response) {
  const contentType = response.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    return response.json();
  }
  return { detail: await response.text() };
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const payload = await readJson(response);
  if (!response.ok) {
    throw new Error(payload.detail || `Request failed with ${response.status}`);
  }
  return payload;
}

document.getElementById("healthButton").addEventListener("click", async () => {
  const output = document.getElementById("healthOutput");
  output.textContent = "Checking...";
  try {
    output.textContent = format(await requestJson("/health"));
  } catch (error) {
    output.textContent = error.message;
  }
});

document.getElementById("agentButton").addEventListener("click", async () => {
  const output = document.getElementById("agentOutput");
  output.textContent = "Loading...";
  try {
    output.textContent = format(await requestJson("/api/v1/agent-card"));
  } catch (error) {
    output.textContent = error.message;
  }
});

document.getElementById("chatForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const output = document.getElementById("chatOutput");
  const message = document.getElementById("message").value.trim();
  output.textContent = "Sending...";
  try {
    const payload = await requestJson("/api/v1/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    output.textContent = payload.answer;
  } catch (error) {
    output.textContent = error.message;
  }
});

document.getElementById("transcribeForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const output = document.getElementById("transcribeOutput");
  const input = document.getElementById("audio");
  if (!input.files.length) {
    output.textContent = "Choose an audio file first.";
    return;
  }

  const body = new FormData();
  body.append("file", input.files[0]);
  output.textContent = "Uploading...";

  try {
    const payload = await requestJson("/api/v1/transcribe", {
      method: "POST",
      body,
    });
    output.textContent = payload.text;
  } catch (error) {
    output.textContent = error.message;
  }
});
