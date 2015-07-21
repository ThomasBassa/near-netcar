// separate into files
//START AUTOBAHN
var connection = new autobahn.Connection({
	url: 'ws://104.197.24.18:8080/ws',
	realm: 'realm1'
});
var mySession;
var mode = "Manual";
connection.onopen = function(session) {
	// Subscribe to interface topics-- object detect, speed, position
	session.subscribe('aero.near.detect', detected);
	session.subscribe('aero.near.carSpeed', speedUpdate);
	session.subscribe('aero.near.carPos', posUpdate);
	session.subscribe('aero.near.carHeading', headingUpdate);
	mySession = session;
}

connection.open();
//END AUTOBAHN

//START GOOGLE MAPS
var map;
var myLatLng = new google.maps.LatLng(29.1886, -81.0487);
var markListener;
var mark;

function initialize() {
	var mapOptions = {
		zoom: 18,
		center: myLatLng,
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};

	map = new google.maps.Map(document.getElementById('map-canvas'),
		mapOptions);
	icon = 'littlearrow.png';
	carMarker = new google.maps.Marker({
		position: myLatLng,
		map: map,
		title: 'Vehicle',
		icon: icon
	});

	markListener = new google.maps.event.addListener(map, 'click', function (e) {
		mark = new google.maps.Marker({
				position: e.latLng,
				map: map,
				title: 'Waypoint',
				animation: google.maps.Animation.DROP,
		});
		google.maps.event.removeListener(markListener);
		var delListener = new google.maps.event.addListener(mark, 'rightclick', function(e){
			mark.setMap(null);
			google.maps.event.removeListener(delListener);
			
		});
		markListener = new google.maps.event.addListener(map, 'click', function (e) {
			addMarker(e,mark);
		});
	});
}
function addMarker(e, markdel) {
	markdel.setMap(null);
	markdel = null;
	mark = new google.maps.Marker({
		position: e.latLng,
		map: map,
		title: 'Waypoint',
		animation: google.maps.Animation.DROP,
	});

	var delListener = new google.maps.event.addListener(mark, 'rightclick', function(e){
		mark.setMap(null);
		google.maps.event.removeListener(delListener);
		
	});
}
function loadScript() {
	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp' +
		'&signed_in=true&callback=initialize';
	document.body.appendChild(script);
}

function helloWorld() {
	console.log("Hello World");
}

//window.onload = loadScript;
google.maps.event.addDomListener(window, 'load', initialize);

window.setInterval(refresh, 33);
// window.setInterval(honk, 2000);        uncomment when honking exists
var objectAvoidanceOverride = false;
var timer;
var speed = 0;
var heading = "N&#176;0E";

var objWindow = new google.maps.InfoWindow({
	content: 'Object Detected!',
	position: myLatLng
});

function refresh() {
	console.log("refreshing");
	// $("#webcamimg").attr("src", "http://10.33.93.86/snapshot.cgi?"+new Date().getTime());
	//publishing object avoidance checkbox status
	if (document.getElementById("switch1").checked == true && objectAvoidanceOverride == false) {
		console.log("checked");
		mySession.publish('aero.near.override', [true]);
		objectAvoidanceOverride = true;
		console.log("making timer");
		timer = window.setTimeout(function() {
			objectAvoidanceOverride = false;
			mySession.publish('aero.near.override', [false]);
			document.getElementById("switch1").checked = false;
			console.log("time's up");
		}, 20000);

	} else if (document.getElementById("switch1").checked == false && objectAvoidanceOverride == true) {
		objectAvoidanceOverride = false;
		mySession.publish('aero.near.override', [false]);
		window.clearTimeout(timer);
	}

	document.getElementById("display").innerHTML =
		"Latitude: " + myLatLng.lat().toFixed(3) + "<br>Longitude: " + myLatLng.lng().toFixed(3) + "<br>Speed: " + speed.toFixed(1) + " mph<br>Heading: " + heading;
}

//Callback functions for subscribed topics
function detected(bool) { //bool is whether or not object is detected
	if (bool) {
		objWindow.open(map);
	} else if (bool == false) {
		objWindow.close();
  }
}

function speedUpdate(newSpeed) {
	speed = Number(newSpeed);
}

function posUpdate(newLat, newLng) {
	console.log(newLat + " " + newLng);
	console.log(newLat[0] + " " + newLat[1]);
	myLatLng = new google.maps.LatLng(newLat[0], newLat[1]);
	console.log(myLatLng.lat() + " " + myLatLng.lng());
	map.setCenter(myLatLng);
	carMarker = null;
	carMarker = new google.maps.Marker({
		position: myLatLng,
		map: map,
		title: 'Vehicle',
		icon: icon
	});
}
function headingUpdate(newHeading) {
	heading = newHeading;
}

function stop() {
	mySession.publish('aero.near.emergStop', []);
}
function honk() {
	mySession.publish('aero.near.honkHorn',[]);
}
//END GOOGLE MAPS