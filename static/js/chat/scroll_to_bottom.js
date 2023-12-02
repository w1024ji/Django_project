
window.onload =function() {

    var element = document.getElementById("chatroom_box");
    element.scrollIntoView(false);

}


function calcTextareaHeight(e) {
    e.style.height = 'auto'
    e.style.height = `${e.scrollHeight}px`
}







