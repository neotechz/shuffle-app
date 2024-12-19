const board = document.getElementById("board");
const board_question = board.querySelector(".question");
const board_answer = board.querySelector(".answer");
const board_reveal = board.querySelector(".reveal");

document.addEventListener("DOMContentLoaded", function(){
    const cards = document.getElementsByClassName("card hidden");
    let index = Math.floor(Math.random() * cards.length);
    
    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;
});

board_reveal.addEventListener("click", function(){
    board_answer.type = "text";
})
