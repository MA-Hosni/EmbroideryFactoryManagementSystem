function searchFunction() {
  let input, filter, table, tr, td, j;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  for (j = 0; j < tr.length; j++) {

    td = tr[j].getElementsByTagName("td");

    if (td.length > 0) {
      if (td[0].innerHTML.toLocaleUpperCase().indexOf(filter) > -1 ||
          td[1].innerHTML.toLocaleUpperCase().indexOf(filter) > -1 ||
          td[2].innerHTML.toLocaleUpperCase().indexOf(filter) > -1 ||
          td[3].innerHTML.toLocaleUpperCase().indexOf(filter) > -1) {
            tr[j].style.display = "";
      } else {
        tr[j].style.display = "none";
      }
       
    }
  }
}

function clearSearch() {
  document.getElementById("search").value = "";
  // Call the searchFunction here to reset the table
  searchFunction();
}





function showModal(firstName, lastName, email, phone, ville) {
  var modal = document.getElementById("myModal");
  var srch = document.getElementById("win-nekteb");
  srch.innerHTML =`${firstName} ${lastName}`;
  document.getElementById("first_name_input").value = `${firstName}`;
  document.getElementById("last_name_input").value = `${lastName}`;
  document.getElementById("email_input").value = `${email}`;
  document.getElementById("phone_input").value = `${phone}`;
  document.getElementById("ville_input").value = `${ville}`;
  modal.style.display = "block";
}

window.onclick = function(event) {
  var modal = document.getElementById("myModal");
  if (event.target == modal) {
      modal.style.display = "none";
  }
}

var closeButton = document.getElementsByClassName("noselect")[0];
closeButton.onclick = function() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
};