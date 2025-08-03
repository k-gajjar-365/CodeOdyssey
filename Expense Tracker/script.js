document.addEventListener("DOMContentLoaded", () => {
  const expenseForm = document.getElementById("form");
  const expenseName = document.getElementById("expense-name");
  const expenseAmt = document.getElementById("amt");
  const expenseList = document.getElementById("expense-list");
  const totalAmtDisplay = document.getElementById("total-amount");

  let expenses = JSON.parse(localStorage.getItem('expenses')) || [];
  let totalAmt = calculateTotal();

  renderExpensed();
  expenseForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = expenseName.value.trim();
    const amount = parseFloat(expenseAmt.value.trim());

    if (name !== "" && !isNaN(amount) && amount > 0) {
      const newExpense = {
        id: Date.now(),
        name,
        amount,
      };

      expenses.push(newExpense);
      saveExpensestoLocal();
      renderExpensed();
      updateTotal();

      // clear input
      expenseName.value = "";
      expenseAmt.value = "";

      expenseName.focus();
    }
  });

  function calculateTotal() {
    
    return expenses.reduce((sum, current) => (sum + current.amount) , 0);
    
  }

  function updateTotal() {
    totalAmt = calculateTotal();
    totalAmtDisplay.textContent = `$${totalAmt.toFixed(2)}`;
  }

  function saveExpensestoLocal() {
    localStorage.setItem("expenses", JSON.stringify(expenses));
  }

  function renderExpensed () {
    expenseList.innerHTML = "";

    expenses.forEach((exp) => {
        const li = document.createElement('li')
        li.innerHTML = `
        <div class="i">
        ${exp.name} - $${exp.amount}
        <button data-id="${exp.id}" class="btn btn-danger">Delete</Delete>
        </div>
        `
        li.classList.add("item");
        // Attach child...
        expenseList.appendChild(li);
    })
  }

  expenseList.addEventListener('click',((e) => {
    if(e.target.tagName === "BUTTON"){
        const expenseId = parseInt(e.target.getAttribute('data-id'))

        expenses = expenses.filter(exp => exp.id != expenseId)

        saveExpensestoLocal();
        renderExpensed();
        updateTotal();
    }
  }))

});
