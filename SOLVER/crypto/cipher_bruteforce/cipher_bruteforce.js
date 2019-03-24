function decodeCipher(input)
{
    //var encoded = window.btoa(input);
    //var decoded = window.atob(input);

    //Function call list
    decodeBase64(input)

    runRot(input)
    rot47(input)
    runCaesar(input)
    
}

function decodeBase64(input)
{
    document.getElementById("output_base64").innerHTML = 5 + 6;
}

