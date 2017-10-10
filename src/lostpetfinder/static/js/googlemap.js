/*
  JavaScript function to display the location of a pet in google map.
  The latitude and longitude values are retrivied via google geocoding
  web service api using pet's location.
*/
function initMap() {
  var petLat = parseFloat(document.getElementById('petLat').getAttribute('value'));
  var petLng = parseFloat(document.getElementById('petLng').getAttribute('value'));

  var petLatLng = {lat: petLat, lng: petLng};

  // Create new map
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: petLatLng
  });

  // Add map marker
  var marker = new google.maps.Marker({
    position: petLatLng,
    map: map
  });
}
