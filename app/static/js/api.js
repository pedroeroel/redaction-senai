const essayTextArea = document.getElementById("text");
const essayTitle = document.getElementById("title");
const essayTheme = document.getElementById("theme");
const senderButton = document.getElementById("send-button");

async function fetchEssay() {
    const response = await fetch("https://the-learners-dream.vercel.app/api/redaction", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            essay: essayTextArea.value,
            title: essayTitle.value,
            theme: essayTheme.value
        })
    });
    if (!response.ok) {
        throw new Error("Network response was not ok");
    }
    return response.json();
}

senderButton.addEventListener('click', async (event) => {
    event.preventDefault();
    try {
        const results = await fetchEssay();
        sessionStorage.setItem('essayResults', JSON.stringify(results))
        window.location.assign('/essay_results');
    } catch (error) {
        console.error('Error fetching essay:', error);
    }
});