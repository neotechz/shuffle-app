let update_deck = function(deck){
    fetch("/deck/rename", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: deck.id,
            name: deck.value

        })
    }).then(response => response.json())
    .then(data => {
        if(data["success"]){
            deck.value = data["name"]
            deck.placeholder = data["name"]
        }
    });
}