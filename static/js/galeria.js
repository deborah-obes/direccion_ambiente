const imagenes = [
  { titulo: "Nuevo Parque Urbano II de Febrero", img: "static/img/parque-feb.jpg" },
  { titulo: "Plaza de los Abuelos", img: "static/img/plaza-abuelos.jpg" },
  { titulo: "Plazoleta Provincias Unidas", img: "static/img/plazoleta.jpg" },
  { titulo: "Sendero Sembremos Vida", img: "static/img/sendero.jpg" },
  { titulo: "Dulces Sueños - Parque Urbano Laguna", img: "static/img/laguna.jpg" },
  { titulo: "Mirador Ecológico", img: "static/img/mirador.jpg" },
  { titulo: "Bosque de los Niños", img: "static/img/bosque.jpg" },
  { titulo: "Huerta Comunitaria Sur", img: "static/img/huerta.jpg" },
  { titulo: "Ronda Verde Norte", img: "static/img/ronda.jpg" },
  { titulo: "Senda de los Juegos", img: "static/img/senda.jpg" },
  { titulo: "Jardín Botánico", img: "static/img/jardin.jpg" },
  { titulo: "Paseo del Arroyo", img: "static/img/arroyo.jpg" },
  { titulo: "Plaza Centenario", img: "static/img/centenario.jpg" },
  { titulo: "Parque Lineal", img: "static/img/lineal.jpg" },
  { titulo: "Casona Verde", img: "static/img/casona.jpg" }
];

const porPagina = 15; // 3x5
let paginaActual = 1;

const container = document.getElementById('galeria-grid');
const paginationControls = document.getElementById('pagination-controls');

function mostrarPagina(pagina) {
  container.innerHTML = "";
  const inicio = (pagina - 1) * porPagina;
  const fin = inicio + porPagina;
  const items = imagenes.slice(inicio, fin);

  items.forEach(item => {
    const card = document.createElement('div');
    card.className = 'tarjeta-galeria';
    card.innerHTML = `
      <img src="${item.img}" alt="${item.titulo}" onerror="this.src='https://via.placeholder.com/400x200?text=Imagen+no+disponible'">
      <div class="info">
        <h3>${item.titulo}</h3>
        <button class="btn-ver" onclick="verImagen('${item.img}', '${item.titulo}')">Ver foto</button>
      </div>
    `;
    container.appendChild(card);
  });

  renderizarPaginacion();

  // ✅ Auto-salto a la siguiente página después de 2 segundos si hay más
  if (items.length === porPagina && paginaActual < Math.ceil(imagenes.length / porPagina)) {
    setTimeout(() => {
      paginaActual++;
      mostrarPagina(paginaActual);
    }, 2000);
  }
}

function verImagen(src, titulo) {
  let modal = document.getElementById('modal-imagen');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'modal-imagen';
    modal.className = 'modal';
    modal.innerHTML = `
      <span class="cerrar" onclick="cerrarModal()">&times;</span>
      <img id="modal-img" src="" alt="">
    `;
    document.body.appendChild(modal);
  }
  document.getElementById('modal-img').src = src;
  document.getElementById('modal-img').alt = titulo;
  modal.style.display = 'flex';
}

function cerrarModal() {
  document.getElementById('modal-imagen').style.display = 'none';
}

function renderizarPaginacion() {
  paginationControls.innerHTML = "";
  const total = Math.ceil(imagenes.length / porPagina);
  for (let i = 1; i <= total; i++) {
    const btn = document.createElement('button');
    btn.textContent = i;
    btn.disabled = i === paginaActual;
    btn.addEventListener('click', () => {
      paginaActual = i;
      mostrarPagina(paginaActual);
    });
    paginationControls.appendChild(btn);
  }
}

// Inicializar
mostrarPagina(paginaActual);