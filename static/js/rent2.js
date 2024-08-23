document.addEventListener('DOMContentLoaded', function(){
    var userName = localStorage.getItem('name');
    var userPhone = localStorage.getItem('phone');
    var userLicense = localStorage.getItem('license');
    var userEmail = localStorage.getItem('email');
    var userPickup = localStorage.getItem('pickup');
    var userDropOff = localStorage.getItem('dropOff');
    var userStart = localStorage.getItem('start');
    var userEnd = localStorage.getItem('end');
  
    if (userName && userPhone && userLicense && userEmail && userPickup && userDropOff && userStart && userEnd) {
     document.getElementById('savedInfo').innerHTML = "Name: " + userName + "<br> Mobile Number: " + userPhone + "<br> User License: " + userLicense
     + "<br> User Email: " + userEmail + "<br> User PickUp: " + userPickup + "<br> User DropOff: " + userDropOff + "<br> Starting Date:" + userStart + "<br> Ending Date:" + userEnd;
    }
 });
 
 document.getElementById('arrivalForm').addEventListener('submit', function(event){
   event.preventDefault();
 
   var name = document.getElementById('name').value;
   var phone = document.getElementById('phone').value;
   var license = document.getElementById('license').value;
   var email = document.getElementById('email').value;
   var pickup = document.getElementById('pickup').value;
   var dropOff = document.getElementById('dropOff').value;
   var start = document.getElementById('start').value;
   var end = document.getElementById('end').value;
 
   localStorage.setItem('name' , name);
   localStorage.setItem('phone',phone);
   localStorage.setItem('license',license);
   localStorage.setItem('email',email);
   localStorage.setItem('pickup',pickup);
   localStorage.setItem('dropOff',dropOff);
   localStorage.setItem('start',start);
   localStorage.setItem('end',end);
 
   document.getElementById('savedInfo').innerHTML = "Name: " + name + "<br> Mobile Number: " + phone + "<br> User License: " + license 
     + "<br> User Email: " + email + "<br> User PickUp: " + pickup + "<br> User DropOff: " + dropOff + "<br> Starting Date:" + start + "<br> Ending Date:" + end;
 
   document.getElementById('name').value = '';
   document.getElementById('phone').value = '';
   document.getElementById('license').value = '';
   document.getElementById('email').value = '';
   document.getElementById('pickup').value = '';
   document.getElementById('dropOff').value = '';
   document.getElementById('start').value = '';
   document.getElementById('end').value = '';
 
   alert('Form submitted successfully!');
 });
 
 function showPage(pageId){
   var pages = document.getElementsByClassName('page');
   for (var i = 0; i<pages.length;i++){
     pages[i].style.display = 'none';
   }
   document.getElementById(pageId).style.display = 'block';
 }