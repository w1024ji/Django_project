
window.onload =function() {

    var element = document.getElementById("chatroom_box");
    element.scrollIntoView(false);

}



//
// const scrollToBottom = () => {
//     window.scrollTo(0, document.body.scrollHeight);
// };
//
// // 페이지가 로드될 때 스크롤을 하단으로 이동
// window.onload = scrollToBottom;
//
// setTimeout(function() {
//                 window.scrollTo(0, document.body.scrollHeight);
//             }, 500);
//
// // 일정 시간 간격으로 페이지를 스크롤
// setInterval(() => {
//     scrollToBottom();
// }, 3000); // 예: 3초마다 스크롤





//
//
// window.onload = function() {
//             window.scrollTo(0, document.body.scrollHeight);
//         };
//
// setTimeout(function() {
//                 window.scrollTo(0, document.body.scrollHeight);
//             }, 500);
//
//
// // const scrollToBottom = () => {
// //     window.scrollTo(0, document.body.scrollHeight);
// // };
//
// // 페이지가 로드될 때 스크롤을 하단으로 이동
// //window.onload = scrollToBottom;
//
//
// function scrollToBottoms() {
//     let objDiv = document.getElementsByClassName("chat-log-container");
//     objDiv.scrollTop = objDiv.scrollHeight;
// }
//
// // Add this below the function to trigger the scroll on load.
// scrollToBottoms();