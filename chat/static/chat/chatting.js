        const roomName = JSON.parse(document.getElementById('room-name').textContent);
        const chatLog = document.querySelector('#chat-log');

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
            const timestamp = new Date(data.timestamp);

            console.log("Timestamp from server:", data.timestamp);  // 확인용 로그

            if (!isNaN(timestamp.getTime())) {
            }

            // 받은 메시지를 chat-log에 추가 (스타일 정보를 적용)
       //     chatLog.innerHTML += `<div class="chat-message">${message}</div>`;
            chatLog.innerHTML += `<div class="d-flex flex-row justify-content-start"><p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">${message}
            </p>
            <!-- <span class="text-muted">${timestamp.toLocaleString()}</span>  -->
<!--                 <span class="text-muted">{{chatmessage.timestamp}}</span> -->
                 </div>`;
            //message 구조

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
                'message': message
            }));
            messageInputDom.value = '';
        };


