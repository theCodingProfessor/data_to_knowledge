// Function to set date in footer of flask templates

function setDate() {
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    document.getElementById('insert_date').innerHTML = String(currentYear);
    }

// module.exports = {
//     setDate: setDate
// };

