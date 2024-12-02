let update_input_tag = function(input, model, attr, id){
    fetch("/action/update_input_tag", {
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
    }).then(response => response.json())
    .then(data => {
        if(data["success"]){
            input.value = data["value"]
            input.placeholder = data["value"]
        }
    });
}