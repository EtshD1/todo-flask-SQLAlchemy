(() => {
  // Add task form
  const form = document.querySelector("form");

  // On submit post to "/add"
  form.addEventListener("submit", async (e) => {
    // Disable refresh
    e.preventDefault();
    const desc = form["description"].value;

    const response = await fetch('/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `description=${desc}`
    });

    const result = await response.json();
    console.log(result);
  });
})()