const title = document.getElementById("main-title"), body = document.getElementById("main-paragraph"),
 employBtn = document.getElementById("emp"), cliBtn = document.getElementById("cli");

function changeEN () {
  title.innerHTML = 'Welcome';
  body.innerHTML = 'Alias Embroidery! Each thread, a blank canvas for our creativity. Our team of experts transforms fabric into exceptional embroidered works. Explore art at Alias Broderie, where every stitch tells a story of passion.';
  employBtn.innerHTML = 'Employee';
  cliBtn.innerHTML = 'Adherent';
}

function changeFR () {
  title.innerHTML = 'Bienvenu';
  body.innerHTML = "Alias Broderie ! Chaque fil, une toile vierge pour notre créativité. Notre équipe d'experts transforme le tissu en œuvres brodées d'exception. Explorez l'art chez Alias Broderie, où chaque point conte une passion.";
  employBtn.innerHTML = 'Employé';
  cliBtn.innerHTML = 'Adhérent';
}

function changeAR () {
  title.innerHTML = 'مرحباً';
  body.innerHTML = ' كل خيط ، قماش فارغ لإبداعنا. يقوم فريق الخبراء لدينا بتحويل القماش إلى أعمال مطرزة استثنائية. استكشف الفن في Alias Broderie ، حيث تحكي كل غرزة قصة شغف.';
  employBtn.innerHTML = 'موظف';
  cliBtn.innerHTML = 'عضو';
}

