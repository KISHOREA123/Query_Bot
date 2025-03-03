document.getElementById("send-button").addEventListener("click", function() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        addToHistory(userInput);
        document.getElementById("user-input").value = "";
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
