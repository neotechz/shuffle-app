const update_input_tag = async function(input, model, attr, id){
    const response = await fetch("/action/update_input_tag", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            model: model,
            attr: attr,
            value: input.value,
            id: id
        })
    });
    
    const data = await response.json();
    
    if(data["success"]){
        input.value = data["value"]
        input.placeholder = data["value"]
    };
}

const sync_deck_name = async function(id){
    const response = await fetch("/action/sync_deck_name", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: id
        })
    });

    const data = await response.json();

    if(data["success"]){
        document.title = `Shuffle: ${data["deck_name"]}`;
    };

}

const create_new_deck = async function(){
    const response = await fetch("/action/create_new_deck", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });
    
    const data = await response.json();
    return data;
}

const create_new_card = async function(deck_id){
    const response = await fetch("/action/create_new_card", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            deck_id: deck_id
        })
    });
    
    const data = await response.json();
    return data;
}

const delete_card = async function(deck_id, id){
    const response = await fetch("/action/delete_card", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            deck_id: deck_id,
            id: id
        })
    });
    
    const data = await response.json();
    return data;
}

const redirect = function(method, url){
    const form = document.createElement("form");
    form.method = method;
    form.action = url;

    document.body.appendChild(form);
    form.submit();
}

const update_card = async function(attr, value, id){
    const response = await fetch("/action/update_card", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            attr: attr,
            value: value,
            id: id
        })
    });
    
    const data = await response.json();
}