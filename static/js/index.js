const decks = document.getElementsByClassName("deck");
for(let deck of decks){
    let deck_view = deck.querySelector(".view");
    deck_view.addEventListener("click", function(){
        deck.action = `/deck/${deck.id}`;
        deck.submit()
    });
}

const new_deck = document.getElementById("new_deck");
new_deck.addEventListener("click", async function(event){
    const deck = await create_new_deck();
    await create_new_card(deck.id);
    redirect("POST", `/deck/${deck.id}`);
});