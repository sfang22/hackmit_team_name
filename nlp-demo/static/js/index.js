fetch('/article/-LolLHKU3eaMHDENwiXh')
.then(resp => 
    {
        console.log(resp)
        return resp.json();
    })
.then(
    resp => {
        $("#text").html("hello");
        $("#blob").html(JSON.stringify(resp["entity_sentiment"], null, 4));
        $("#url").html(resp["url"]);
        $("#source").html("Source: " + resp["source"] + " News");

        console.log(JSON.stringify(resp["entity_sentiment"], null, 4));
    }
)