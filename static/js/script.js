const publicaciones = [
  { titulo: "Proyecto: Sendero 'Sembremos Vida'", fecha: "19/12/2025 19:15" },
  { titulo: "Proyecto: Plaza de los Abuelos", fecha: "19/12/2025 19:07" },
  { titulo: "Proyecto: Parque Urbano Il de Febrero", fecha: "19/12/2025 19:00" },
  { titulo: "Proyecto: Plazoleta Gral. San Martín", fecha: "18/12/2025 18:30" },
  { titulo: "Proyecto: Recuperación de Espacios Verdes", fecha: "17/12/2025 16:45" },
  { titulo: "Proyecto: Jardín Botánico Municipal", fecha: "16/12/2025 14:20" },
  { titulo: "Proyecto: Ronda Verde Norte", fecha: "15/12/2025 12:10" },
  { titulo: "Proyecto: Huerta Comunitaria Sur", fecha: "14/12/2025 10:00" },
  { titulo: "Proyecto: Paseo del Arroyo", fecha: "13/12/2025 09:30" },
  { titulo: "Proyecto: Bosque de los Niños", fecha: "12/12/2025 08:15" },
  { titulo: "Proyecto: Mirador Ecológico", fecha: "11/12/2025 07:45" },
  { titulo: "Proyecto: Senda de los Juegos", fecha: "10/12/2025 06:30" }
];

const cardsPorPagina = 6;
let paginaActual = 1;

const container = document.getElementById('cards-container');
const paginationControls = document.getElementById('pagination-controls');

function mostrarPagina(pagina) {
  container.innerHTML = "";
  const inicio = (pagina - 1) * cardsPorPagina;
  const fin = inicio + cardsPorPagina;
  const publicacionesPagina = publicaciones.slice(inicio, fin);

  publicacionesPagina.forEach(pub => {
    const card = document.createElement('div');
    card.className = 'tarjeta';
    card.innerHTML = `
      <h3>${pub.titulo}</h3>
      <p><strong>Fecha:</strong> ${pub.fecha}</p>
    `;
    container.appendChild(card);
  });

  renderizarPaginacion();
}

function renderizarPaginacion() {
  paginationControls.innerHTML = "";
  const totalPaginas = Math.ceil(publicaciones.length / cardsPorPagina);

  for (let i = 1; i <= totalPaginas; i++) {
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

mostrarPagina(paginaActual);