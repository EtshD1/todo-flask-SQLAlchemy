"use strict";
(() => {
  // Remove task function
  const removeTask = (id, li) => {
    fetch('/delete', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `id=${id}`
    })
      .then(res => {
        return res.json();
      }).then(result => {
        if (result.status === true) {
          li.remove();
        } else {
          alert("Sorry, an error occurred :(");
        }
      });
  };
  // Update task function
  const updateTask = (id, change, target) => {
    fetch('/update', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `id=${id}&data=${change}`
    })
      .then(res => {
        return res.json();
      }).then(result => {
        if (result.status !== true) {
          alert("Sorry, an error occurred :(");
          target.checked = !change;
        }
      });
  }
  // For creating HTML task
  const createTask = (data, id) => {
    const li = document.createElement("li");
    // Add task and class name
    const task = document.createElement("div");
    task.classList.add("task");
    // Add description field and class
    const description = document.createElement("div");
    description.classList.add("description");
    const input = document.createElement("input");
    input.classList.add("completed");
    input.setAttribute("type", "checkbox");
    input.setAttribute("name", "completed");
    input.addEventListener("change", e => updateTask(id, e.target.checked, e.target));
    const p = document.createElement("p");
    p.textContent = data;
    description.appendChild(input);
    description.appendChild(p);
    // Add remove button
    const remove = document.createElement("div");
    remove.classList.add("remove");
    // Add svg to button
    remove.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"> <!-- Font Awesome Free 5.15.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --> <path d="M32 464a48 48 0 0 0 48 48h288a48 48 0 0 0 48-48V128H32zm272-256a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zm-96 0a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zm-96 0a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zM432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z" /></svg>`;
    remove.dataset.id = id;
    remove.addEventListener("click", () => {
      removeTask(id, li);
    });
    // Append all
    li.appendChild(task);
    task.appendChild(description);
    task.appendChild(remove);
    document.querySelector(".taskList").appendChild(li);
  }
  // Add task form
  const taskForm = document.querySelector(".taskList form");

  // On submit post to "/add"
  try {
    taskForm.addEventListener("submit", (e) => {
      // Disable refresh
      e.preventDefault();
      const desc = taskForm["description"].value;

      fetch(window.location.pathname, {
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
            createTask(result.description, result.id);
          } else {
            alert("Sorry, an error occurred :(");
          }
        });
    });
  } catch (error) {
    if (taskForm === null) {
      console.log("No lists");
    } else {
      console.log(error);
    }
  }

  // Delete/Update tasks
  document.querySelectorAll(".task").forEach(task => {
    const id = task.dataset.id;
    // Delete
    const deleteBtn = task.querySelector(".remove");
    deleteBtn.addEventListener("click", () => {
      removeTask(id, deleteBtn.parentNode.parentNode);
    });
    // Update
    const completedCheckbox = task.querySelector(".completed");
    completedCheckbox.addEventListener("change", e => {
      const change = e.target.checked;
      updateTask(id, change, e.target);
    });
  });
  // Delete lists
  document.querySelectorAll(".todoList").forEach(list => {
    const id = list.dataset.id;
    list.querySelector(".delete-list").addEventListener("click", () => {
      fetch("/delete-list", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `id=${id}`
      })
        .then(res => res.json())
        .then(
          res => {
            if (res.status) {
              window.location.replace("/");
            } else {
              alert("Something went wrong :(");
            }
          }
        );
    })
  });
})();