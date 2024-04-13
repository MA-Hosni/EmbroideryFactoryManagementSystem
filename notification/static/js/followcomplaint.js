function showModal(complaintText, complaintStatus) {
  var modal = document.getElementById("myModal");
  var content = document.getElementById("content");
  var respondMessage = document.getElementById("ijeba");
  var response = document.getElementById("pend");

  content.textContent = complaintText;
  modal.style.display = "block";
  if (complaintStatus === "pending") {
    response.style.display = "none";
    respondMessage.style.display = "block";
  } else {
    response.style.display = "block";
    respondMessage.style.display = "none";
  }
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