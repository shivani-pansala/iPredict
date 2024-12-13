$(document).ready(async function () {
     // Show the loading animation
     $("#loading").fadeIn();
 
     try {
         // Fetch and display location details
         const locationDetails = await fetchLocationDetails();
 
         // Hide the loading animation and show the results
         $("#loading").fadeOut(function () {
            
             $("#locationDetails").html(`
                 <p><strong>Your Location Details:</strong></p>
                 <p>City: ${locationDetails.city}</p>
                 <p>Region: ${locationDetails.region}</p>
                 <p>Country: ${locationDetails.country}</p>
             `).fadeIn();
         });
     } catch (error) {
          // Handle errors
          $("#loading").fadeOut(function () {
           
             $("#locationDetails").html("<p>Unable to fetch location details. Please try again.</p>").fadeIn();
          });
          console.error("Error fetching location details:", error);
      }
  });
 
 // Function to get user's latitude and longitude
 function getCoordinates() {
     return new Promise((resolve, reject) => {
         if (!navigator.geolocation) {
             reject(new Error("Geolocation is not supported by this browser."));
         }
 
         navigator.geolocation.getCurrentPosition(
             (position) => resolve(position.coords),
             (error) => reject(error)
         );
     });
 }
 
 // Function to fetch location details
 async function fetchLocationDetails() {
     const coords = await getCoordinates();
     const lat = coords.latitude;
     const lon = coords.longitude;
 
     const url = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${lon}&localityLanguage=en`;
 
     const response = await fetch(url);
     if (!response.ok) {
         throw new Error("Failed to fetch location data.");
     }
 
     return response.json();
 }
 