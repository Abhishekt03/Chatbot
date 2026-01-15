function login() {
  const formData = new URLSearchParams();
  formData.append("username", document.getElementById("email").value);
  formData.append("password", document.getElementById("password").value);

  fetch("https://chatbot-platform-production-4786.up.railway.app/users/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    body: formData.toString()
  })
  .then(res => res.json())
  .then(data => {
    localStorage.setItem("token", data.access_token);
    window.location.href = "chat.html";
  })
  .catch(() => alert("Login failed"));
}
