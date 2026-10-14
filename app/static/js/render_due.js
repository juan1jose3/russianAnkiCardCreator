const cardAdminView = document.querySelector(".card-admin-view");

async function getCards() {
    const cards = await fetch("/due_cards");
    const response = await cards.json();

    if(!response){
        cardAdminView.textContent = "No cards to display";
        return;
    }

   response.forEach(card => {

    cardAdminView.innerHTML = `
        <div>${card.fields.Front}</div>
    
    `
   });

}

getCards();
