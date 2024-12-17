const deck = document.getElementsByClassName("deck")[0];
const deck_name = deck.querySelector(".name")
deck_name.addEventListener("focusout", async function(event){
    await update_input_tag(event.currentTarget, "Deck", "name", deck.id);
    sync_deck_name(deck.id);
});

const cards = document.getElementsByClassName("card");
for(let card of cards){
    let card_front = card.querySelector(".front");
    card_front.addEventListener("focusout", async function(event){
        update_input_tag(event.currentTarget, "Card", "front", card.id)
    });

    let card_back = card.querySelector(".back");
    card_back.addEventListener("focusout", async function(event){
        update_input_tag(event.currentTarget, "Card", "back", card.id)
    });

    let card_delete = card.querySelector(".delete");
    card_delete.addEventListener("click", async function(event){
        await delete_card(deck.id, card.id);
        redirect("POST", `/deck/${deck.id}`);
    });
};

const new_card = document.getElementById("new_card");
new_card.addEventListener("click", async function(event){
    let card = await create_new_card(deck.id)
    redirect("POST", `/deck/${deck.id}`);
});