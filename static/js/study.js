const cards = document.getElementsByClassName("card hidden");

const board = document.getElementById("board");
const board_question = board.querySelector(".question");
const board_answer = board.querySelector(".answer");

let index = 0;

document.addEventListener("DOMContentLoaded", function(){
    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;
});

const board_reveal = board.querySelector(".reveal");
board_reveal.addEventListener("click", function(){
    board_answer.type = "text";
});

const board_next = board.querySelector(".next");
board_next.addEventListener("click", function(){
    index += 1;
    index %= cards.length;

    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;
    board_answer.type = "hidden";
});
