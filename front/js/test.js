var myXMLHttp=new XMLHttpRequest();      
para = location.search;
var uri="http://127.0.0.1:5000/login"+para; 
myXMLHttp.responseType = 'json';
/* J'envoie ma requête GET synchrone (false) */ 
myXMLHttp.open("get", uri, true);  /* envoi synchrone */
myXMLHttp.onload = function () {
  // Begin accessing JSON data here
  var data = myXMLHttp.response;
  console.log(data)
  if (myXMLHttp.status >= 200 && myXMLHttp.status < 400) { 
      document.getElementById("test").innerHTML = myXMLHttp.response[0];
      document.getElementById("test2").innerHTML = myXMLHttp.response[1]
  } else {
      console.log("Erreur: " + myXMLHttp.readyState +
          " " + myXMLHttp.status);
  }
}
myXMLHttp.send();