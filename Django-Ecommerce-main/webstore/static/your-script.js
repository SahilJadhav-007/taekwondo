const form = document.querySelector('form');
const fullName = document.getElementById('Name');
const email = document.getElementById('Email');
const contact = document.getElementById('Contact');
const problem = document.getElementById('problem');

function sendEmail() {

    const bodyMessage = `Full Name: ${fullName.value}<br>
                         Email: ${email.value}<br>
                         Contact: ${contact.value}<br>
                         Message: ${problem.value}`;
    

    Email.send({
        Host: "smtp.elasticemail.com",
        Username: "sahilavinashjadhav2003@gmail.com",
        Password: "F85BE669DA2D2BA2B2F76557E1252EF5B577",
        To: 'sahilavinashjadhav2003@gmail.com',
        From: "sahilavinashjadhav2003@gmail.com",
        Subject: "New enquire mail",
        Body: bodyMessage
    }).then(
        message =>{
            if(message == "OK"){
                Swal.fire({
                    title: "Success",
                    text: "Message sent successfully!",
                    icon: "success"
                  });
            }
        }
    )
}

function checkInputs(){
    const items = document.querySelectorAll(".item");

    for(const item of items){
        if (item.value == ""){
            item.classList.add("error");
            item.parentElement.classList.add("error");
        }
    }
}

form.addEventListener("submit",(e) => {
    e.preventDefault();
    //sendEmail();
    checkInputs();
})




document.addEventListener('DOMContentLoaded', function () {
    const barsIcon = document.querySelector('.checkbtn');
    const navList = document.getElementById('navList');

    barsIcon.addEventListener('click', function () {
        navList.classList.toggle('show');
    });
});


const menuIcon = document.getElementById('menuIcon');
const navList = document.querySelector('.navdiv ul');

menuIcon.addEventListener('click', () => {
    // Toggle the visibility of the navigation list
    navList.classList.toggle('show');
});

// Get reference to the button and the divs to be toggled
const minorButton = document.getElementById('minorButton');
const divsToToggle = document.querySelectorAll('#minorButton ~ div');

// Add click event listener to the button
minorButton.addEventListener('click', function() {
    // Loop through the divs and toggle their visibility
    divsToToggle.forEach(div => {
        div.style.display = div.style.display === 'none' ? 'block' : 'none';
    });
});




// nav{
//     width: 100%;
//     height: 80px;
//     background-color: #F4F4F4;

// }

// #logo{
//     height: 3rem;
//     width: 3rem;
//     border-radius: 50%;
//     padding-left: 1rem ;
//     padding-top: 1rem;
//     padding-bottom: 1rem;
// }

// nav ul{
//     float: right;
//     margin-right: 20px;
// }

// nav ul li{
//     display: inline-block;
//     line-height: 80px;
//     margin: 0 5px;
// }

// nav ul li a{
//     color: black;
//     text-transform: uppercase;
// }

// .checkbtn{
//     font-size: 30px;
//     color: #19204E;
//     float: right;
//     line-height: 80px;
//     margin-right: 20px;
//     cursor: pointer;
//     display: none;
// }

// #check{
//     display: none;
// }

// @media screen and (max-width:952px) {
//     .checkbtn{
//         display: block;
//     }

//     ul{
//         position: fixed;
//         background: #DF1B3F;
//         width: 100%;
//         height: 100vh;
//         top: 80px;
//         left: -100%;
//         text-align: center;
//         transition: all 0.5s;
//     }

//     nav ul li{
//         display: block;
//     }
//     nav ul li a{
//         font-size: 20px;
//     }

//     #check:checked ~ ul{
//         left: 0;
//     }
// }