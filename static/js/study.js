const cards = document.getElementsByClassName("card hidden");

const board = document.getElementById("board");
const board_question = board.querySelector(".question");
const board_answer = board.querySelector(".answer");
const board_reveal = board.querySelector(".reveal");
const board_next = board.querySelector(".next");

const user_score = document.getElementById("user_score");

let index = 0;

document.addEventListener("DOMContentLoaded", function(){
    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;

    if (index >= cards.length - 1){
        board_next.disabled = true;
    }
});


board_reveal.addEventListener("click", function(){
    board_answer.type = "text";
    user_score.hidden = false;
});


board_next.addEventListener("click", function(){
    index += 1;

    if (index >= cards.length - 1){
        board_next.disabled = true;
    }

    board_question.value = cards[index].querySelector(".front").value;
    board_answer.value = cards[index].querySelector(".back").value;
    board_answer.type = "hidden";
    user_score.hidden = "true";
});
