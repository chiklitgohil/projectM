fetch("http://127.0.0.1:5000/submit_report", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    user_id: "12345",
    label: "Plastic Waste",
    location: { lat: 19.076, lng: 72.8777 },
    photo_url: "https://example.com/photo.jpg",
  }),
})
  .then((res) => res.json())
  .then((data) => console.log(data));
