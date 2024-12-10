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
    
    data = await response.json();
    
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

    data = await response.json();

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
    
    data = await response.json();
    return data;
}

const redirect = function(method, url){
    form = document.createElement("form");
    form.method = method;
    form.action = url;

    document.body.appendChild(form);
    form.submit();
}