function showModal(leaveid, matricule, firstName, lastName, reason, submitted, start, end) {
  var modal = document.getElementById("myModal");
  var id = document.getElementById("requestid");
  var fullname = document.getElementById("name");
  var matri = document.getElementById("matricule");
  var days = document.getElementById("days");
  var motif = document.getElementById("motif");
  var sub = document.getElementById("submitted");

  id.innerHTML = `Leave Request #${leaveid}`;
  fullname.innerHTML = `<b>Full Name</b> ${firstName} ${lastName}`;
  matri.innerHTML = `<b>Matricule</b> ${matricule} `;
  days.innerHTML = `<b>From</b> ${start} <b>to</b> ${end}`
  motif.innerHTML = `${reason}`;
  sub.innerHTML = `<i class="fa-solid fa-calendar-day" style="padding-right: 5px;"></i>date: ${submitted} `;
  modal.style.display = "block";
}

window.onclick = function(event) {
  var modal = document.getElementById("myModal");
  if (event.target == modal) {
      modal.style.display = "none";
  }
}

var closeButton = document.getElementsByClassName("close")[0];
closeButton.onclick = function() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
};