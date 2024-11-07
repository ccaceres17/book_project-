import tkinter as tk
from tkinter import messagebox, simpledialog

# Clases de datos y nodos
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class SimpleList:
    def __init__(self):
        self.head = None

    def add_book(self, book):
        new_node = Node(book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search_book(self, title):
        current = self.head
        while current:
            if current.book.title == title:
                return current.book
            current = current.next
        return None

    def delete_book(self, title):
        current = self.head
        previous = None
        while current:
            if current.book.title == title:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def show_books(self):
        current = self.head
        books = []
        while current:
            books.append(f"{current.book.title} by {current.book.author} ({current.book.year})")
            current = current.next
        return books

# Interfaz gráfica con tkinter
class BookManagerApp:
    def __init__(self, root):
        self.list = SimpleList()

        # Configuración de la ventana
        root.title("Gestión de Libros")
        root.geometry("400x300")

        # Entradas de datos
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)
        tk.Label(root, text="Título:").grid(row=0, column=0)

        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)
        tk.Label(root, text="Autor:").grid(row=1, column=0)

        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=2, column=1)
        tk.Label(root, text="Año:").grid(row=2, column=0)

        # Botones de acción
        tk.Button(root, text="Agregar Libro", command=self.add_book).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Buscar Libro", command=self.search_book).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Eliminar Libro", command=self.delete_book).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Mostrar Libros", command=self.show_books).grid(row=6, column=0, columnspan=2)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()

        if title and author and year:
            try:
                year = int(year)
                book = Book(title, author, year)
                self.list.add_book(book)
                messagebox.showinfo("Éxito", f"Libro '{title}' agregado.")
            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def search_book(self):
        title = self.title_entry.get()
        if title:
            book = self.list.search_book(title)
            if book:
                messagebox.showinfo("Libro Encontrado", f"Título: {book.title}\nAutor: {book.author}\nAño: {book.year}")
            else:
                messagebox.showinfo("No Encontrado", "El libro no existe en la lista.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduzca el título para buscar.")

    def delete_book(self):
        title = self.title_entry.get()
        if title:
            success = self.list.delete_book(title)
            if success:
                messagebox.showinfo("Éxito", f"Libro '{title}' eliminado.")
            else:
                messagebox.showinfo("No Encontrado", "El libro no existe en la lista.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduzca el título para eliminar.")

    def show_books(self):
        books = self.list.show_books()
        if books:
            messagebox.showinfo("Lista de Libros", "\n".join(books))
        else:
            messagebox.showinfo("Lista Vacía", "No hay libros en la lista.")

# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = BookManagerApp(root)
    root.mainloop()
