function validateEmail() {
    var inputText = document.getElementById('email').value;
    var error = document.getElementById('emailError');
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!inputText.match(mailformat)) {
        error.innerHTML = "You have entered an invalid email address!";
        document.form1.email.focus();
        return false;
    }
    else {
        return true;
    }
}
function validateForm() {
    var inputText = document.getElementById('email').value;
    var error = document.getElementById('emailError');
    var contact= document.getElementById('contact').value;
    var contactError= document.getElementById('contactError');
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!inputText.match(mailformat)) {
        error.innerHTML = "You have entered an invalid email address!";
        document.form1.email.focus();
        return false;
    }
    if (contact.length < 10|| contact.length > 10) {
        contactError.innerHTML="number should be only 10 digit";
        return false;

    }
    else {
        return true;
    }

}
let contact = document.getElementById('contact');
let defaultValue = contact.value;

contact.addEventListener('contact', checkInput);

function checkInput(e) {
  let currentInput = defaultValue;

  // check if the default part of the currentInput is invalid
  if (currentInput.substring(0, defaultValue.length) !== defaultValue) {

    // if it is then reset the input value to the default one
    this.value = defaultValue;
  }
}
