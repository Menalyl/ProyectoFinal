//https://www.eclipse.org/paho/clients/js/


function ACTIVAR() {
	
	console.log("ACTIVAR");
        message = new Paho.MQTT.Message("ACTIVADO");
        message.destinationName = "menalyluzuriaga@gmail.com/test1";
        client.send(message);
		document.getElementById("estado").innerHTML="Activado"
		        
  
}
function DESACTIVAR(){	
	
	
	console.log("DESACTIVAR");
        message = new Paho.MQTT.Message("DESACTIVADO");
        message.destinationName = "menalyluzuriaga@gmail.com/test1";
        client.send(message);
		document.getElementById("estado").innerHTML="Desactivado"
		
}
function ENVIAR(){	
	
		console.log("ENVIAR");
		H=document.getElementById("hora").value
        message = new Paho.MQTT.Message(H);
        message.destinationName = "menalyluzuriaga@gmail.com/test1";
        client.send(message);
		document.getElementById("estado").innerHTML="Activado"
		
}



// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  
  var options = {
   useSSL: false,
    userName: "menalyluzuriaga@gmail.com",
    password: "1600482853mena",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
    client.subscribe("menalyluzuriaga@gmail.com/test");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "menalyluzuriaga@gmail.com/test1";
    client.send(message);

	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    console.log("Nuevo mensaje:"+message.payloadString); 
    document.getElementById("estado").innerHTML=message.payloadString.split(" ")[0];
	document.getElementById("nivel").innerHTML=message.payloadString.split(" ")[1];
	document.getElementById("rp").innerHTML=message.payloadString.split(" ")[2];
  }

