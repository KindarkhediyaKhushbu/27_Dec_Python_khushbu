// static/js/form_validation.js
$(document).ready(function() {
    $("#contact-form").on("submit", function(event) {
        var isValid = true;
        $("#form-error").hide(); // Hide previous error message

        // Validate the name field
        var name = $("input[name='name']").val();
        if (name.trim() === "") {
            isValid = false;
            alert("Name is required.");
        }

        // Validate the email field
        var email = $("input[name='email']").val();
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            isValid = false;
            alert("Please enter a valid email address.");
        }

        // Validate the message field
        var message = $("textarea[name='message']").val();
        if (message.trim() === "") {
            isValid = false;
            alert("Message is required.");
        }

        if (!isValid) {
            event.preventDefault(); // Prevent the form from submitting if validation fails
            $("#form-error").show(); // Show error message
        }
    });
});
