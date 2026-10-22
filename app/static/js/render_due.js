const cardAdminView = document.querySelector(".card-admin-view");

function stripSoundMarks(text){
    return text.replace(/\[sound:[^\]]*\]/g, "").trim();
}

async function getCards() {
    try{
        const res = await fetch("/due_cards");
        const data = await res.json();

        if(!res.ok || data.error){
            cardAdminView.innerHTML = `<p class="error">Error loading cards: ${data.error || res.statusText}</p>`;
            return;
        }

        if(!Array.isArray(data) || data.length === 0){
            cardAdminView.innerHTML = "<p>No cards due for review!</p>";   
            return;   
        }

        const rows = data.map((card, cardIndex) => {
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

    }catch(err){
        console.error("Failed to fetch cards:", err);
        cardAdminView.innerHTML = "<p>Could not connect to the server.</p>";
    }
}

getCards();
