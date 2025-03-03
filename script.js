WebChat.default.init({
    selector: "#webchat",
    initPayload: "/greet",
    customData: {"language": "en"},
    socketUrl: "http://localhost:5005",
    title: "GovCert Chatbot",
    showMessageDate: true,
    openLauncherImage: "https://cdn-icons-png.flaticon.com/512/561/561127.png"
});

// Typing Indicator Simulation
function showTypingIndicator() {
    document.getElementById("typing").style.display = "block";
    setTimeout(() => {
        document.getElementById("typing").style.display = "none";
    }, 2000);
}

// Send Button Click Event
document.getElementById("send-button").addEventListener("click", function() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        showTypingIndicator();
        document.getElementById("user-input").value = "";
    }
});

// Press Enter to Send Message
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        document.getElementById("send-button").click();
    }
});
