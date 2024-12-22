const cards = document.getElementsByClassName("card hidden");

const board = document.getElementById("board");
const board_question = board.querySelector(".question");
const board_answer = board.querySelector(".answer");
const board_next = board.querySelector(".next");

let index = 0;

document.addEventListener("DOMContentLoaded", function(){
    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;

    if (index >= cards.length - 1){
        board_next.disabled = true;
    }
});

const board_reveal = board.querySelector(".reveal");
board_reveal.addEventListener("click", function(){
    board_answer.type = "text";
});


board_next.addEventListener("click", function(){
    index += 1;

    if (index >= cards.length - 1){
        board_next.disabled = true;
    }

    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;
    board_answer.type = "hidden";
});
