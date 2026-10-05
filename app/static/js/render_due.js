const cardAdminView = document.querySelector(".card-admin-view");

async function getCards() {
    const cards = await fetch("/due_cards");
    const response = await cards.json();
    console.log(response);
}

getCards();
