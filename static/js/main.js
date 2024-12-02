let update_input = function(input, type){
    fetch(`/${type}/rename`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: input.id,
            name: input.value

        })
    }).then(response => response.json())
    .then(data => {
        if(data["success"]){
            input.value = data["name"]
            input.placeholder = data["name"]
        }
    });
}