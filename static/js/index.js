const new_deck = document.getElementById("new_deck");
new_deck.addEventListener("click", async function(event){
    const deck = await create_new_deck();
    await create_new_card(deck.id);
    redirect("POST", `/deck/${deck.id}`);
});