document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("prediction-form");
    form.addEventListener("submit", function(event) {
        const yearInput = document.getElementById("year");
        if (yearInput.value === "") {
            event.preventDefault();
            alert("Please enter a year.");
        }
    });
});