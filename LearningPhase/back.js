// function onMapClick(e) {
//     alert("You clicked the map at " + e.latlng);
// }

// map.on('click', onMapClick);


var map = L.map('map').setView([23.188408, 72.6279691], 13);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);



var marker = L.marker([23.188408, 72.6279691]).addTo(map);
marker.bindPopup("<b>Mangrove Report</b><br>Condition: healthy");




map.locate({setView: true, maxZoom: 16});
map.on('locationfound', function(e) {
    L.marker(e.latlng).addTo(map)
        .bindPopup("You are here").openPopup();
});
