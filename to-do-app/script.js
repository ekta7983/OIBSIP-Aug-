// Function to add a task
function addTask() {
  let taskInput = document.getElementById("taskInput");
  let taskValue = taskInput.value;

  if (taskValue === "") {
    alert("Please enter a task.");
    return;
  }

  let taskList = document.getElementById("taskList");

  // Create a new task item
  let li = document.createElement("li");

  li.innerHTML = `<span>${taskValue}</span>
                    <div>
                        <button class="complete-btn" onclick="markComplete(this)">✔️</button>
                        <button class="delete-btn" onclick="deleteTask(this)">❌</button>
                    </div>`;

  taskList.appendChild(li);
  taskInput.value = "";

  // Function to mark a task as complete
  function markComplete(button) {
    let taskItem = button.parentElement.parentElement;
    taskItem.classList.toggle("completed");
  }

  // Function to delete a task
  function deleteTask(button) {
    let taskItem = button.parentElement.parentElement;
    taskItem.remove();
  }
}
