// Adding an event listener to the 'submit' event of the 'registerForm' form.
document.getElementById('registerForm').addEventListener('submit', function(e) {
    // Prevents the default form submission action.
    e.preventDefault();

    // Retrieves the values from the username and password input fields.
    const username = document.getElementById('regUsername').value;
    const password = document.getElementById('regPassword').value;

    // Sends a POST request to the '/api/register' endpoint.
    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Specifies that we're sending JSON data.
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => {
        // Checks if the response status indicates success.
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parses the JSON response.
        return response.json();
    })
    .then(data => {
        // Displays the message from the server using an alert.
        alert(data.message);
    })
    .catch(error => {
        // Logs any errors to the console and shows an alert to the user.
        console.error('There was a problem with the fetch operation:', error);
        alert('Registration failed. Please try again later.');
    });
});

// Adding an event listener to the 'submit' event of the 'loginForm' form.
document.getElementById('loginForm').addEventListener('submit', function(e) {
    // Prevents the default form submission action.
    e.preventDefault();

    // Retrieves the values from the username and password input fields.
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    // Sends a POST request to the '/api/login' endpoint.
    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Specifies that we're sending JSON data.
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => {
        // Checks if the response status indicates success.
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parses the JSON response.
        return response.json();
    })
    .then(data => {
        // Displays the message from the server using an alert.
        alert(data.message);
    })
    .catch(error => {
        // Logs any errors to the console and shows an alert to the user.
        console.error('There was a problem with the fetch operation:', error);
        alert('Login failed. Please check your credentials and try again.');
    });
});
