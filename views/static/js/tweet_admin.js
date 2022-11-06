
async function populateTweetEditForm(id){
    localStorage.setItem("tweet_id", id);
    const connection = await fetch("/api-get-tweet-by-id?id=" + id.toString())
    
    if( ! connection.ok ){
        return
      }

    const response = await connection.text()
    const parsedResponse = JSON.parse(response)
    const date = parsedResponse['date']
    const text = parsedResponse['text']
    const likes = parsedResponse['likes']

    let myModal = new bootstrap.Modal(document.getElementById('tweetEditModal'))

    form = myModal._element.getElementsByClassName('modal-body').mbody.getElementsByClassName("mb-3")
    
    form.item(0).getElementsByClassName("form-control").item(0).setAttribute('value', date);
    form.item(1).getElementsByClassName("form-control").item(0).innerHTML = text;
    form.item(2).getElementsByClassName("form-control").item(0).setAttribute('value', likes);

    myModal.show()
}

async function editTweetAdmin(element){
    event.preventDefault()
    const id = localStorage.getItem("tweet_id");
    let f = document.getElementById("mForm");
    const fd = new FormData(f);
    fd.append("tweet_id", id);

    const connection = await fetch("/api-update-tweet-admin", {
        method : "POST",
        body : fd
    })
    
    if( ! connection.ok ){
        return
    }

    // SPA
    let row = document.getElementById("table_row"+id.toString()).children
    row.item(1).innerHTML = fd.get("date", "");
    row.item(3).innerHTML = fd.get("text", "");
    row.item(4).innerHTML = fd.get("likes", "");

    var myModalEl = document.getElementById('tweetEditModal')
    var modal = bootstrap.Modal.getInstance(myModalEl)
    modal.hide()

}

async function showModal(tweet_id){
    localStorage.setItem("tweet_id", tweet_id);
    let myModal = new bootstrap.Modal(document.getElementById('tweetDeleteModal'))
    myModal.show()
}

async function deleteTweetAdmin(){
    const tweet_id = localStorage.getItem("tweet_id");
    
    const connection = await fetch(`/api-delete-tweet/${tweet_id}`, {
        method : "DELETE"
      })
      if( ! connection.ok ){
        alert("oppps... try again")
        return
      }

    // SPA
    let row = document.getElementById("table_row"+tweet_id.toString()).remove()

    var myModalEl = document.getElementById('tweetDeleteModal')
    var modal = bootstrap.Modal.getInstance(myModalEl)
    modal.hide()

}