$(document).ready(function() {
    
    // Function to send a message
    function sendMessage() {
        const userMessage = $('#user-message').val().trim(); // Get input value and trim any whitespace
        if (userMessage === "") return;  // Don't send empty messages

        // Append the user's message to the chat box
        $('#chat-box').append(`<div class="user-message"><strong>You:</strong> ${userMessage}</div>`);

        // Show the typing indicator while waiting for a response
        $('#typing-indicator').show();

        // Scroll to the bottom of the chat box to show new messages
        $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);

        // Send the user's message to the Flask server
        $.ajax({
            url: '/chat',  // Flask route that handles the chat
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: userMessage }),
            success: function(data) {
                // Hide the typing indicator once the response is ready
                $('#typing-indicator').hide();

                // Display the bot's response in the chat box
                const botReply = data.reply || "Sorry, I couldn't process your message.";
                $('#chat-box').append(`<div class="bot-message"><strong>Assistant:</strong> ${botReply}</div>`);

                // Scroll to the bottom to show the latest message
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
            error: function(error) {
                // Hide the typing indicator in case of an error
                $('#typing-indicator').hide();

                // Display error message
                $('#chat-box').append(`<div class="bot-message"><strong>Assistant:</strong> Sorry, something went wrong.</div>`);

                // Scroll to the bottom to show the latest message
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            }
        });

        // Clear the input field after sending the message
        $('#user-message').val("");
    }

    // Send message when the "Research" button is clicked
    $('#send-message').click(function() {
        sendMessage();
    });

    // Send message when Enter is pressed in the input field
    $('#user-message').keypress(function(e) {
        if (e.which === 13) {  // Check for Enter key
            e.preventDefault();  // Prevent form submission (if inside a form)
            sendMessage();
        }
    });
});


