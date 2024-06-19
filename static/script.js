document.addEventListener('DOMContentLoaded', function () {
    // Check if the 'viewVotes' button exists in the DOM
    if (document.getElementById('viewVotes')) {
        // Add an event listener to the 'viewVotes' button
        document.getElementById('viewVotes').addEventListener('click', function () {
            // Fetch the votes from the server
            fetch('/api/admin/votes', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    // Check if the response is ok
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    // Parse the JSON response
                    return response.json();
                })
                .then(data => {
                    // Get the 'votesList' element
                    const votesList = document.getElementById('votesList');
                    // Clear any existing content in the 'votesList'
                    votesList.innerHTML = '';
                    // Check if the data is empty
                    if (data.length === 0) {
                        votesList.textContent = 'No votes found.';
                    } else {
                        // Iterate through the data and create elements for each vote
                        data.forEach(vote => {
                            const voteItem = document.createElement('div');
                            voteItem.textContent = `User ID: ${vote.user_id}, Candidate ID: ${vote.candidate_id}, Timestamp: ${vote.timestamp}`;
                            votesList.appendChild(voteItem);
                        });
                    }
                })
                .catch(error => {
                    // Log the error and display a message
                    console.error('Error:', error);
                    const votesList = document.getElementById('votesList');
                    votesList.textContent = 'Failed to load votes.';
                });
        });
    }

    // Registration form submission
    if (document.getElementById('registerForm')) {
        document.getElementById('registerForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const fingerprint = document.getElementById('fingerprint').value;

            fetch('/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, fingerprint })
            })
                .then(response => response.json())
                .then(data => alert(data.message))
                .catch(error => console.error('Error:', error));
        });
    }

    // Authentication form submission
    if (document.getElementById('authenticateForm')) {
        document.getElementById('authenticateForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const fingerprint = document.getElementById('fingerprint').value;

            fetch('/api/authenticate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, fingerprint })
            })
                .then(response => response.json())
                .then(data => alert(data.message))
                .catch(error => console.error('Error:', error));
        });
    }

    // Vote form submission
    if (document.getElementById('voteForm')) {
        document.getElementById('voteForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const fingerprint = document.getElementById('fingerprint').value;
            const candidate_id = document.getElementById('candidate_id').value;

            fetch('/api/vote', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, fingerprint, candidate_id })
            })
                .then(response => response.json())
                .then(data => alert(data.message))
                .catch(error => console.error('Error:', error));
        });
    }
});




