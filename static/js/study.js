document.addEventListener("DOMContentLoaded", function(){
    const cards = document.getElementsByClassName("card hidden");
    let index = Math.floor(Math.random() * cards.length);

    const board = document.getElementById("board");
    const board_question = board.querySelector(".question");
    
    board_question.value = cards[index].querySelector(".front").value;
});