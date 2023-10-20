export function formatDate(inputDate) {
    const months = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ];

    const dateParts = inputDate.split(" ")[0].split("-");
    const year = dateParts[0];
    const month = parseInt(dateParts[1], 10) - 1;
    const day = parseInt(dateParts[2], 10);

    return `${day} de ${months[month]} de ${year}`;
}