

// Basic JavaScript to interact with the API and display results
const output = document.getElementById("output");

function display(data) {
    output.textContent = JSON.stringify(data, null, 2);
}

async function apiCall(url, method="GET", body=null) {
    const options = { method, headers: { "Content-Type": "application/json" } };
    if (body) options.body = JSON.stringify(body);
    const res = await fetch(url, options);
    const data = await res.json();
    display(data);
}

/* USERS */
function getAllUsers(){ apiCall("/users"); }
function getUser(){ apiCall(`/users/${userId.value}`); }
function deleteUser(){ apiCall(`/users/${userId.value}`, "DELETE"); }
function createUser(){
    apiCall("/users","POST",{name:userName.value,email:userEmail.value});
}
function updateUser(){
    apiCall(`/users/${userId.value}`,"PUT",{name:userName.value,email:userEmail.value});
}

/* DREAMS */
function getAllDreams(){ apiCall("/dreams"); }
function getDream(){ apiCall(`/dreams/${dreamId.value}`); }
function deleteDream(){ apiCall(`/dreams/${dreamId.value}`,"DELETE"); }
function createDream(){
    apiCall("/dreams","POST",{
        user_id: dreamUserId.value,
        title: dreamTitle.value,
        description: dreamDescription.value,
        date: dreamDate.value,
        mood: dreamMood.value,
        vividness: dreamVividness.value
    });
}
function updateDream(){
    apiCall(`/dreams/${dreamId.value}`,"PUT",{
        user_id: dreamUserId.value,
        title: dreamTitle.value,
        description: dreamDescription.value,
        date: dreamDate.value,
        mood: dreamMood.value,
        vividness: dreamVividness.value
    });
}

/* SYMBOLS */
function getAllSymbols(){ apiCall("/symbols"); }
function getSymbol(){ apiCall(`/symbols/${symbolId.value}`); }
function deleteSymbol(){ apiCall(`/symbols/${symbolId.value}`,"DELETE"); }
function createSymbol(){
    apiCall("/symbols","POST",{name:symbolName.value,description:symbolDescription.value});
}
function updateSymbol(){
    apiCall(`/symbols/${symbolId.value}`,"PUT",{name:symbolName.value,description:symbolDescription.value});
}

/* POEMS */
function getAllPoems(){ apiCall("/poems"); }
function getPoem(){ apiCall(`/poems/${poemId.value}`); }
function deletePoem(){ apiCall(`/poems/${poemId.value}`,"DELETE"); }
function createPoem(){
    apiCall("/poems","POST",{author_id:poemAuthorId.value,dream_id:poemDreamId.value,content:poemContent.value});
}
function updatePoem(){
    apiCall(`/poems/${poemId.value}`,"PUT",{author_id:poemAuthorId.value,dream_id:poemDreamId.value,content:poemContent.value});
}

/* DREAMSYMBOLS */
function getAllDreamSymbols(){ apiCall("/dreamsymbols"); }
function getSymbolsForDream(){
    apiCall(`/dreamsymbols?dream_id=${filterDreamId.value}`);
}
function getDreamSymbol(){
    apiCall(`/dreamsymbols/${linkId.value}`);
}
function linkDreamSymbol(){
    apiCall("/dreamsymbols","POST",{dream_id:linkDreamId.value,symbol_id:linkSymbolId.value});
}
function updateDreamSymbol(){
    apiCall(`/dreamsymbols/${linkId.value}`,"PUT",{dream_id:linkDreamId.value,symbol_id:linkSymbolId.value});
}
function deleteDreamSymbol(){
    apiCall(`/dreamsymbols?dream_id=${linkDreamId.value}&symbol_id=${linkSymbolId.value}`,"DELETE");
}