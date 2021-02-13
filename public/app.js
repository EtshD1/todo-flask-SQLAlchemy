"use strict";
(() => {
  // For creating HTML task
  const createTask = (data) => {
    const li = document.createElement("li");
    // Add task and class name
    const task = document.createElement("div");
    task.classList.add("task");
    // Add description field and class
    const description = document.createElement("div");
    description.classList.add("description");
    description.textContent = data;
    // Add remove button
    const remove = document.createElement("div");
    remove.classList.add("remove");
    // Add svg to button
    remove.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"> <!-- Font Awesome Free 5.15.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --> <path d="M32 464a48 48 0 0 0 48 48h288a48 48 0 0 0 48-48V128H32zm272-256a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zm-96 0a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zm-96 0a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zM432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z" /></svg>`;
    // Append all
    li.appendChild(task);
    task.appendChild(description);
    task.appendChild(remove);
    document.querySelector(".taskList").appendChild(li);
  }
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
          createTask(result.description);
        } else {
          alert("Sorry and error occurred :(");
        }
      });
  });
})();