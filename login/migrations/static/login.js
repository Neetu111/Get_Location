/**
 * Created by 15-r007tx on 10-Apr-17.
 */
function validateForm(){
    var uname = document.forms["myForm"]["username"].value;
    var pass = document.forms["myForm"]["password"].value;

    if((!isEmpty(uname, "Log In")) && (!isEmpty(pass, "Password"))){

        prompt("fine h...");
    }else{
        prompt("fine nhi h...");
    }
}
function isEmpty(elemValue, field){
    if((elemValue == "") || (elemValue == null)){
        alert("you can not have "+field+" field empty");
        return true;
    }else{
        return false;
    }
}

function form_fill(){
    window.location="http://www.tutorialspoint.com";
}