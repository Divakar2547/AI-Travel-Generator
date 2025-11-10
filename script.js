document.getElementById("itineraryForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const destination = document.getElementById("destination").value;
  const days = document.getElementById("days").value;
  const interests = document.getElementById("interests").value;

  document.getElementById("result").innerText = "Generating itinerary... please wait ⏳";

  const response = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ destination, days, interests }),
  });

  const data = await response.json();
  document.getElementById("result").innerText = data.itinerary;
});
