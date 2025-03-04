document.getElementById("send-icon").addEventListener("click", function() {
    let userInput = document.getElementById("user-input").value.trim();
    if (userInput !== "") {
        console.log("User message:", userInput); // Replace with your chatbot function
        document.getElementById("user-input").value = ""; // Clear input
    }
});


function addToHistory(query) {
    let historyList = document.getElementById("history-list");
    if (historyList.children[0].textContent === "No previous queries") {
        historyList.innerHTML = "";
    }
    let newHistoryItem = document.createElement("li");
    newHistoryItem.textContent = query;
    historyList.appendChild(newHistoryItem);
}
