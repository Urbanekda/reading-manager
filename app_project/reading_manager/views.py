from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def delete_book(request, pk):
    if request.method == "POST":
        try:
            book = get_object_or_404(Book, pk=pk)
            book_name = book.name
            book.delete()
            messages.success(request, f"Successfully deleted '{book_name}'")
        except Exception as e:
            messages.error(request, f"Error deleting book: {str(e)}")
    
    return redirect("index")

def add_book(request):
    if request.method == "POST":
        try:
            # Extract form data
            new_book = Book(
                name=request.POST["name"],
                author=request.POST["author"],
                topic=request.POST["topic"],
                status=request.POST["status"],
                notes=request.POST.get("notes", "")  # Optional field
            )
            
            # Handle optional rating
            rating = request.POST.get("rating")
            if rating:
                new_book.rating = int(rating)
            
            # Handle optional cover image
            if "cover" in request.FILES:
                new_book.cover = request.FILES["cover"]
            
            # Save the book
            new_book.save()
            
            messages.success(request, f"Successfully added '{new_book.name}'")
            return redirect('index')  # Or wherever you want to redirect after success
            
        except Exception as e:
            messages.error(request, f"Error adding book: {str(e)}")
            return render(request, "book_add.html", {
                "topic_choices": Book.TOPIC_CHOICES,
                "status_choices": Book.STATUS_CHOICES,
            })
    
    # If GET request, just show the form
    return render(request, "book_add.html", {
        "topic_choices": Book.TOPIC_CHOICES,
        "status_choices": Book.STATUS_CHOICES,
    })


# Sjednotit edit_page_view a edit_book do jedný funkce
def edit_page_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
         
    return render(request, "book_edit.html", {
        "book": book,
        "topic_choices": Book.TOPIC_CHOICES,
        "status_choices": Book.STATUS_CHOICES,
    })

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "POST":
        try:
            # Update book data
            book.name = request.POST["name"]
            book.author = request.POST["author"]
            book.topic = request.POST["topic"]
            book.status = request.POST["status"]
            book.notes = request.POST.get("notes", "")
            
            # Handle optional rating
            rating = request.POST.get("rating")
            if rating:
                book.rating = int(rating)
            
            # Handle optional cover image
            if "cover" in request.FILES:
                book.cover = request.FILES["cover"]
            
            # Save the updated book
            book.save()
            
            messages.success(request, f"Successfully updated '{book.name}'")
            return redirect('index')
            
        except Exception as e:
            messages.error(request, f"Error updating book: {str(e)}")
            return render(request, "book_edit.html", {
                "book": book,
                "topic_choices": Book.TOPIC_CHOICES,
                "status_choices": Book.STATUS_CHOICES,
            })
    
    return redirect('index')
    