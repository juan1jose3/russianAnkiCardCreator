const cardAdminView = document.querySelector(".card-admin-view");

async function getCards() {
    const cards = await fetch("/due_cards");
    const response = await cards.json();

    if(!response){
        cardAdminView.textContent = "No cards to display";
        return;
    }

    console.log(response);

   response.forEach(card => {

    cardAdminView.innerHTML += `
    <tr>
        <td>Front: ${card.fields.Front.value}</td>
        <td>Back: ${card.fields.Back.value}</td>
    </tr>
    
    
    `

   });

}

getCards();
