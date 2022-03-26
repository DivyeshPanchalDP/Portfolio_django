//   copy your firebase config informations

const firebaseConfig = {
    apiKey: "AIzaSyARFBw7SN5Glz5i-t0TmjDSRkVKLoIH0_A",
    authDomain: "portfolio-4fd1f.firebaseapp.com",
    databaseURL: "https://portfolio-4fd1f-default-rtdb.firebaseio.com",
    projectId: "portfolio-4fd1f",
    storageBucket: "portfolio-4fd1f.appspot.com",
    messagingSenderId: "71563837973",
    appId: "1:71563837973:web:1517b8e556ed04b90bc41c"
  };

// initialize firebase
firebase.initializeApp(firebaseConfig);

// reference your database
var contactFormDB = firebase.database().ref("contactForm");

document.getElementById("contactForm").addEventListener("submit", submitForm);

function submitForm(e) {
e.preventDefault();

var name = getElementVal("name");
var emailid = getElementVal("emailid");
var phone = getElementVal("phone");
var msgContent = getElementVal("msgContent");

saveMessages(name, emailid, phone, msgContent);

// //   enable alert
// document.querySelector(".alert").style.display = "block";

// //   remove the alert
// setTimeout(() => {
//   document.querySelector(".alert").style.display = "none";
// }, 3000);

//   reset the form
document.getElementById("contactForm").reset();
}

const saveMessages = (name, emailid, phone, msgContent) => {
var newContactForm = contactFormDB.push();

newContactForm.set({
  name: name,
  emailid: emailid,
  phone: phone,
  msgContent: msgContent,
});
};

const getElementVal = (id) => {
return document.getElementById(id).value;
};