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
    var password= document.getElementById('passw').value;
    var passwordError= document.getElementById('passwordError');
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
    var re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    var x = document.forms["form1"]["passw"].value;
    if (x == "") {
        passwordError.innerHTML=("Password cannot be blank.");
    return false;
     }
       
     else if (!password.match(re)) {
        passwordError.innerHTML="Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)";
        return re.test(password);
    } else {
        document.write("valid")
    
    }

}



/*let contact = document.getElementById('contact');
let defaultValue = contact.value;

contact.addEventListener('contact', checkInput);

function checkInput(e) {
  let currentInput = defaultValue;

  // check if the default part of the currentInput is invalid
  if (currentInput.substring(0, defaultValue.length) !== defaultValue) {

    // if it is then reset the input value to the default one
    this.value = defaultValue;
  }
}*/
