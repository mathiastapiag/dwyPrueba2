$(document).ready(function() {
    $("#panel-admin").css("display", "none");

    $('.open').click(function() {
        $("#panel-admin").animate({ width: 'toggle' }, 100);
    });

    if (!document.getElementById('wrapper').className && !localStorage.getItem("selectedColor")) {
        console.log('in if');
        document.getElementById('wrapper').classList.add('blue');
    } else {
        console.log('else');
        var colorClass = localStorage.getItem("selectedColor");
        document.getElementById('wrapper').classList.add(colorClass);
    }


    $('.panel-group').on('hidden.bs.collapse', toggleIcon);
    $('.panel-group').on('shown.bs.collapse', toggleIcon);

});


//Función para que el header baje con el Scroll 

$(window).scroll(function() {

    if ($(this).scrollTop() > 50) {
        $('header').addClass("sticky");
    } else {
        $('header').removeClass("sticky");
    }
});


function toggleIcon(e) {
    $(e.target)
        .prev('.panel-heading')
        .find(".more-less")
        .toggleClass('fa-plus fa-minus');
}


//Función para cambiar el "Tema" de la página. 

function mytheme(index) {
    switch (index) {
        case 0:
            changeColor('cyan');
            break;
        case 1:
            changeColor('orange');
            break;
        case 2:
            changeColor('lightgreen');
            break;
        case 3:
            changeColor('red');
            break;
        case 4:
            changeColor('green');
            break;
        case 5:
            changeColor('blue');
            break;
        default:
            changeColor('blue');
    }
    var selectedClass = document.getElementById('wrapper').className;
    localStorage.setItem("selectedColor", selectedClass);
}

function changeColor(color) {
    $('#wrapper').removeClass();
    $('#wrapper').addClass(color);
}


//Funciones propias
function onClickRegistro() { 

    name=document.getElementById('idNombre').value;
    lastName=document.getElementById('idApellido').value;
    telefono=document.getElementById('idTelefono').value;
    password=document.getElementById('idPass').value;
    email=document.getElementById('idEmail').value;

    //masculino=document.getElementById('masculino').value;
    //femenino=document.getElementById('femenino').value;
    //otro=document.getElementById('otro').value;





    if(name.toLowerCase() != ""){
        if(lastName.toLowerCase() != ""){
            if(telefono.toLowerCase() != ""){
                if(password.toLowerCase() != ""){
                    if(email.toLowerCase() != ""){

                            alert("Tu cuenta ha sido creada correctamente.");

                    }else{
                        alert("Debes ingresar un Email.");
                    }

                }else{
                    alert("Debes ingresar una Contraseña.");
                }

            }else{
                alert("Debes ingresar un Teléfono.");
            }

        }else{
            alert("Debes ingresar un Apellido.");
        }

    }else{
        alert("Debes ingresar un Nombre.");
    }
 
}

function onClickContact(){
    nameContact = document.getElementById('idNombreContact');
    emailContact = document.getElementById('idEmailContact');
    telefonoContact = document.getElementById('idTelefonoContact');
    asuntoContact = document.getElementById('idAsuntoContact');
    mensajeContact = document.getElementById('idMensajeContact');

    if(nameContact.toLowerCase() != ""){
        if(emailContact.toLowerCase() != ""){
            if(telefonoContact.toLowerCase() != ""){
                if(asuntoContact.toLowerCase() != ""){
                    if(mensajeContact.toLowerCase() != ""){
                        alert("Tu mensaje fue enviado correctamente.");
                    }else{
                        alert("Debes adjuntar un mensaje.");
                    }
                }else{
                    alert("Debes adjuntar un asunto.");
                }
            }else{
                alert("Debes escribir un teléfono.");
            }
        }else{
            alert("Debes escribir un Email.");
        }
    }else{
        alert("Debes escribir un Nombre.");
    }


}

function onClickLogin(){
    emailLogin=document.getElementById('idEmailLogin').value;
    passLogin=document.getElementById('idPassLogin').value;

    if(emailLogin.toLowerCase() != ""){
        if(passLogin.toLowerCase() != ""){
            alert("Has iniciado sesión como: "+emailLogin);
        }else{
            alert("Debes ingresar una contraseña.");
        }
    }else{
        alert("Debes ingresar un Email.");
    }
}