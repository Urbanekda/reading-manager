document.addEventListener('DOMContentLoaded', function() {
    const listEditButton = document.querySelector('.list-edit-button');
    const editButtons = document.querySelectorAll('.edit-button');
    const deleteButtons = document.querySelectorAll('.delete-button');
    
    listEditButton.addEventListener('click', function() {
        this.classList.toggle('active');
        editButtons.forEach(button => {
            button.style.display = button.style.display === 'none' ? 'inline-block' : 'none';
        });
        deleteButtons.forEach(button => {
            button.style.display = button.style.display === 'none' ? 'inline-block' : 'none';
        });
    });
});