// Check if the browser supports the Notification API
if (!("Notification" in window)) {
  alert("This browser does not support desktop notification");
}

// Function to request notification permission
function requestNotificationPermission() {
  Notification.requestPermission().then(function (result) {
    if (result === "granted") {
      showNotification("Notification permission granted!");
    } else {
      showNotification("Notification permission denied.");
    }
  });
}

// Function to show a notification
function showNotification(message) {
  new Notification(message);
}

// Attach click event listener to the button
document.getElementById("notifyButton").addEventListener("click", function() {
  requestNotificationPermission();
});
