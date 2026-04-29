async function callAPI() {
    const apiUrl = "https://api.yourdomain.com"; // 🔥 replace after deployment

    try {
        const res = await fetch(apiUrl);
        const data = await res.json();

        document.getElementById("response").innerText =
            "Response: " + data.message;

    } catch (error) {
        document.getElementById("response").innerText =
            "Error calling API";
        console.error(error);
    }
}
