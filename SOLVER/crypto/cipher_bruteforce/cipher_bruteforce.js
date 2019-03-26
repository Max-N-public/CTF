function decodeCiphers(input)
{
    //Ajax call
    //Allows python scripts to interact with the webpage
    var xhttp = new XMLHttpRequest();
    
    //There are two functions to call from the xhttp object
    //xhttp.open("method", "url", "sync or async")
    xhttp.open("GET", "cipher_lib.py?text=" + input, true);
    xhttp.responseType = "text";

    //function call list
    xhttp.onload = function(e)
    {
        var base64_decoded = text.base64decode(xhttp.response);
        console.log(base64decode);
    }


    xhttp.send();
    
}

