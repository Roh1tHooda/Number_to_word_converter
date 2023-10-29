document.addEventListener("DOMContentLoaded", function () {
    const numberForm = document.getElementById("numberForm");
    const numberInput = document.getElementById("numberInput");
    const convertButton = document.getElementById("convertButton");
    const resultDiv = document.getElementById("result");
    const resultText = document.getElementById("resultText");

    convertButton.addEventListener("click", function () {
        const number = numberInput.value;

        // Validate the input (we can add more validation)
        if (/^\d+$/.test(number)) {
            // Send the number to a server-side script (e.g., using AJAX or fetch)
            fetch('/convert', {
                method: 'POST',
                body: JSON.stringify({ number: number }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultText.textContent = data.words;
                    resultDiv.classList.remove("hidden");
                } else {
                    alert("Error: " + data.error);
                }
            })
            .catch(error => console.error(error));
        } else {
            alert("Please enter a valid number.");
        }
    });
});
