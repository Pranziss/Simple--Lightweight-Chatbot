function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  appendMessage("You", message);
  input.value = "";

  const loading = document.getElementById("loading");
  if (loading) loading.style.display = "block";

  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  })
  .then(res => res.json())
  .then(data => {
    appendMessage("Nova", data.response || "Nova had no response this time.");
    console.log("Nova replied:", data.response);
  })
  .catch(err => {
    console.error("Fetch error:", err);
    appendMessage("Nova", "There was an error talking to Nova.");
  })
  .finally(() => {
    if (loading) loading.style.display = "none";
  });
}

function appendMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("div");
  msg.className = sender === "You" ? "user-msg" : "nova-msg";

  if (sender === "Nova") {
    msg.innerHTML = `<strong>${sender}:</strong><pre>${text}</pre>`;
  } else {
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
  }

  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById("user-input").addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});