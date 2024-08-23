document.addEventListener('DOMContentLoaded', function() {
    // Retrieve saved data from localStorage
    var savedDestination = localStorage.getItem('destination');
    var savedArrival = localStorage.getItem('arrival');
    var pickUp = localStorage.getItem('pickup');
    var departuredate = localStorage.getItem('departuredate');
    var time = localStorage.getItem('departuretime');
    var id = localStorage.getItem('carid');
    var availability = localStorage.getItem('seats');
    var number = localStorage.getItem('contactnumber');
    // Display saved data on the webpage
    if (savedDestination && savedArrival && pickUp && departuredate && time && id && availability && number) {
        document.getElementById('savedInfo').innerHTML = "Destination: " + savedDestination + "<br> Arrival: " + savedArrival + "<br> Pickup Point: " + pickUp
        + "<br> Date: " + departuredate + "<br> Time: " + time + "<br> Car-Id: " + id + "<br> Seats Available: " + availability + "<br> contact Number: " + number;
    }
});

document.getElementById('arrivalForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    var destination = document.getElementById('destination').value;
    var arrival = document.getElementById('arrival').value;
    var pickup = document.getElementById('pickup').value;
    var departuredate = document.getElementById('departuredate').value;
    var departuretime = document.getElementById('departuretime').value;
    var carid = document.getElementById('carid').value;
    var seats = document.getElementById('seats').value;
    var contactnumber = document.getElementById('contactnumber').value;

    // Save form data
    localStorage.setItem('destination', destination);
    localStorage.setItem('arrival', arrival);
    localStorage.setItem('pickup', pickup);
    localStorage.setItem('departuredate', departuredate);
    localStorage.setItem('departuretime', departuretime);
    localStorage.setItem('carid', carid);
    localStorage.setItem('seats', seats);
    localStorage.setItem('contactnumber', contactnumber);

    // Display saved data on the webpage
    document.getElementById('savedInfo').innerHTML = "Destination: " + destination + "<br> Arrival: " + arrival + "<br> Pickup Point: " + pickup 
    + "<br> Date: " + departuredate + "<br> Time: " + departuretime + "<br> Car-Id: " + carid + "<br> Seats Available: " + seats + "<br> contact Number: " + contactnumber;

    // Clear form inputs
    document.getElementById('destination').value = '';
    document.getElementById('arrival').value = '';
    document.getElementById('pickup').value = '';
    document.getElementById('departuredate').value = '';
    document.getElementById('departuretime').value = '';
    document.getElementById('carid').value = '';
    document.getElementById('seats').value = '';
    document.getElementById('contactnumber').value = '';

    // Optionally, you can display a success message or redirect the user
    alert('Form submitted successfully!');
});

function showPage(pageId) {
    // Hide all pages
    var pages = document.getElementsByClassName('page');
    for (var i = 0; i < pages.length; i++) {
        pages[i].style.display = 'none';
    }

    // Show the selected page
    document.getElementById(pageId).style.display = 'block';
}
