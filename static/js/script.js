document.getElementById("reportForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const issue = document.getElementById("issue").value;
  const lat = document.getElementById("latitude").value;
  const lng = document.getElementById("longitude").value;
  const photoFile = document.getElementById("photo").files[0];

  // Convert photo to Base64
  const reader = new FileReader();
  reader.readAsDataURL(photoFile);

  reader.onload = async () => {
    const photoBase64 = reader.result;

    const report = {
      label: issue,
      location: { latitude: lat, longitude: lng },
      photoUrl: photoBase64,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/submit_report", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(report),
      });

      const data = await response.json();
      console.log("Server response:", data);
      alert("Report submitted successfully!");
    } catch (err) {
      console.error("Error submitting:", err);
    }
  };
});

// Initialize map
var map = L.map("map").setView([20.5937, 78.9629], 5);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap contributors",
}).addTo(map);

var marker;
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function (pos) {
    var lat = pos.coords.latitude;
    var lng = pos.coords.longitude;
    document.getElementById("latitude").value = lat;
    document.getElementById("longitude").value = lng;
    map.setView([lat, lng], 15);
    marker = L.marker([lat, lng])
      .addTo(map)
      .bindPopup("Your Location")
      .openPopup();
  });
}

// Credit Conversion
function convertCredits() {
  let credits = parseInt(document.getElementById("credits").innerText);
  let rupees = credits * 10; // Example: 1 credit = ₹10
  document.getElementById("rupees").innerText = rupees;
  document.getElementById("conversion-rate").style.display = "block";
}
