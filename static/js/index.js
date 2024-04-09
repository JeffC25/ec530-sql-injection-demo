function getUser() {
    let results = document.getElementById("results");
    let username = document.getElementById("username").textContent; // Don't question why the username is grabbed this way...
    fetch("/api/user", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username: username })
    })
    .then(response => {
        results.innerHTML = `<div class="p-1 text-center text-orange-500">Fetching user data...</div>`;
        if (response.status == 404) {
            throw new Error("Failed to fetch user data");
        }
        return response.json();
    })
    .then(data => {
        results.innerHTML = `
            <div class="p-1">
                <div class="text-orange-500 text-sm">ID</div>
                <div class="text-neutral-800 ">${data.id}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">UserName</div>
                <div class="text-neutral-800 ">${data.username}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Name</div>
                <div class="text-neutral-800 ">${data.name}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Date of Birth</div>
                <div class="text-neutral-800 ">${data.birthday}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Secret</div>
                <div class="text-neutral-800 ">${data.secret}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Occupation</div>
                <div class="text-neutral-800 ">${data.occupation}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Email</div>
                <div class="text-neutral-800 ">${data.email}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Address</div>
                <div class="text-neutral-800 ">${data.address}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Favorite Color</div>
                <div class="text-neutral-800 ">${data.favorite_color}</div>
            </div>
            <div class="h-px bg-neutral-300 w-full"></div>
            <div class="p-1">
                <div class="text-orange-500 text-sm">Tacos Eaten in Lifetime</div>
                <div class="text-neutral-800 ">${data.total_tacos_eaten}</div>
            </div>
        `;
    }).catch(error => {
        results.innerHTML = `<div class="p-1 text-center text-red-500">Error fetching user data</div>`;
    });
}
