const cardAdminView = document.querySelector(".card-admin-view");

async function getCards() {
    const cards = await fetch("/due_cards");
    const response = await cards.json();

    if(!response){
        cardAdminView.textContent = "No cards to display";
        return;
    }

    const sampleFields = response[0].fields || response[0];
    const headers = Object.keys(sampleFields);

    cardAdminView.textContent = JSON.stringify(response, null, 2);

}

getCards();
