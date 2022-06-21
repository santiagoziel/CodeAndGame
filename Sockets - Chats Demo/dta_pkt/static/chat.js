var socket = io();
//when new user conects it updates list of abailable users
socket.on('new active user', function(message){
  if (document.getElementsByTagName("title")[0].id == message){
    //alert(`no deberia mostrar el nombre de ${message}`)
    return;
  }
  var ul = document.getElementById("connected_users");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(message));
  li.setAttribute("class", "onlineUser")
  li.setAttribute("id", message);
  li.addEventListener("dblclick", event => {
    ClickUser(li)
  });
  ul.appendChild(li);
});

//when user doble clicks on onlineUserns namee it changes how it looks and lets server know
function ClickUser(element) {
  if (!element.classList.contains("talkingTo")){
    element.classList.add("talkingTo");
    socket.emit('whants to talk to', element.id);
  }
  else {
    element.classList.remove("talkingTo");
    socket.emit('whants to stop talking to', element.id);
  }
}

//when client types message it sends it to the server
function SendToServer() {
    socket.emit('new message',{message: document.getElementById("myText").value});
    document.getElementById("myText").value = ''
}

//displays incomingo message into the chatView
// TODO: make it diference betwen mesages sent by client or difeent user
socket.on('incoming message', function(data){
  console.log(data['message']);
  var ul = document.getElementById("chatView");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(data['message']));
  ul.appendChild(li);
});

// lets server know when cleint disconected
function Triger_disconect() {
  // TODO: send client room number so server knows its gone
  socket.emit('client_disconnecting', 'bye');
  window.location.replace("/");
}

socket.on('remove active user', function(data){
  var li = document.getElementById(data);
  li.remove()
});

//lets cleint know another usser whants to talk with them
socket.on('whants to talk', function(room){
  //lets the server know another user whants to talk to me
  socket.emit('talk to me', room);
})

socket.on('stop talk', function(room){
  socket.emit('stop talking to me', room);
})

socket.on('conection updated', function(data){
  //console.log(data['message']);
  var ul = document.getElementById("chatView");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(data));
  ul.appendChild(li);
})

for(element of document.querySelectorAll(".onlineUser")){
  element.addEventListener("dblclick", event => {
    ClickUser(element)
  });
}
