function toggleDateField(statusField) {
    const datePostponedField = document.getElementById('id_date_postponed');
    datePostponedField.style.display = statusField.value === 'postponed' ? 'block' : 'none';
}

