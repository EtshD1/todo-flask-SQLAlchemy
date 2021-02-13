(() => {
  // Add task form
  const form = document.querySelector("form");

  // On submit post to "/add"
  form.addEventListener("submit", (e) => {
    // Disable refresh
    e.preventDefault();
    const desc = form["description"].value;

    fetch('/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `description=${desc}`
    })
      .then(res => {
        return res.json();
      }).then(result => {
        if (result.status === true) {
          window.location.reload();
        } else {
          alert("Sorry and error occurred :(");
        }
      });
  });
})()