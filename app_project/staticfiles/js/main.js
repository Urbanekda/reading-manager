document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.querySelector('.list-edit-button');
    const editButtons = document.querySelectorAll('.edit-button');
    const deleteButtons = document.querySelectorAll('.delete-button');
    
    editButton.addEventListener('click', function() {
        editButtons.forEach(button => {
            button.style.display = button.style.display === 'none' ? 'inline-block' : 'none';
        });
        deleteButtons.forEach(button => {
            button.style.display = button.style.display === 'none' ? 'inline-block' : 'none';
        });
        
        // Toggle button text
        editButton.textContent = editButton.textContent === 'Edit' ? 'Done' : 'Edit';
    });
});