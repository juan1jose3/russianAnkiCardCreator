const cardAdminView = document.querySelector(".card-admin-view");

function stripSoundMarks(text){
    return text.replace(/\[sound:[^\]]*\]/g, "").trim();
}

async function get_cards(state="due"){
    try{
        const res = await fetch(`/request_cards?status=${state}`);
        const data = await res.json();

        if(!res.ok || data.error){
            cardAdminView.innerHTML = `<p class="error">Error loading cards: ${data.error || res.statusText}</p>`;
            return;
        }
        
        renderInfo(data);

    }catch(err){
        console.error("Failed to fetch cards:", err);
        cardAdminView.innerHTML = "<p>Could not connect to the server.</p>";
    }
}

function renderInfo(cardData){
    if(!Array.isArray(cardData) || cardData.length === 0){
        cardAdminView.innerHTML = "<p>No cards due for review!</p>";   
        return;   
    }

    const rows = cardData.map((card, cardIndex) => {
        const front = card.fields?.Front?.value || "(No front)";
        const back = card.fields?.Back?.value || "(No back)";
        return `
            <tr>
                <td>${cardIndex}</td>
                <td>${stripSoundMarks(front)}</td>
                <td>${stripSoundMarks(back)}</td>
                <td>
                    <div class="button-action-container">
                        <button class="edit-btn">Edit</button>
                        <button class="delete-btn">Delete</button>
                    </div>
                </td>
            </tr>
        `;
    }).join("");

    cardAdminView.innerHTML = `
        <table class="due-cards-table">
            <thead>
                <tr>
                    <th>Entry</th>
                    <th>Front</th>
                    <th>Back</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                ${rows}
            </tbody>
        </table>
    `;
}


function getButtonStatus(){
    const filterControls = document.querySelector(".filter-controls");

    filterControls.addEventListener("click", async event => {
        const btn = event.target.closest("button");
        const status = btn.dataset.status;
        const cardData = await get_cards(status);
    });
}

get_cards("due")
getButtonStatus();