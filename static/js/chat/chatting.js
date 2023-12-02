const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatLog = document.querySelector('#chat-log');
const username = JSON.parse(document.getElementById('user_name').textContent);  // 현재 사용자의 username

if (chatLog.childNodes.length<=1) {
    const emptyText = document.createElement('h3')
    emptyText.id = 'emptyText'
    emptyText.className ='emptyText'
    chatLog.appendChild(emptyText)
}

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data.message;
    const userId = data["user_id"];
    const userName = data["user_name"];
    const messageElement = document.createElement('div')



    const loggedInUserId = JSON.parse(document.getElementById("user_id").textContent)
    const loggedInUserName = JSON.parse(document.getElementById("user_name").textContent)

    const timestamp = new Date(data.timestamp);



    // 메시지가 접속한 유저가 보낸 메시지이면
    if (userId === loggedInUserId) {
        messageElement.innerHTML = `<div id="send_message" class="d-flex flex-row justify-content-end" ><p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">
          ${message} </p>
         </div>`;
        messageElement.classList.add('message', 'sender')
    }

    // 메시지가 다른 유저가 보낸 것이면...
    else {
        messageElement.innerHTML = `<div id="receive_message" class="d-flex flex-row justify-content-start" ><p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">
         <strong>${userName}> </strong> ${message} </p>
         </div>`;
        messageElement.classList.add('message', 'receiver')
    }

    chatLog.appendChild(messageElement)


    //메시지 전송 시 스크롤 내리기
        var element = document.getElementById("chatroom_box");
        element.scrollIntoView(false);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
    }));
    messageInputDom.value = '';
};

