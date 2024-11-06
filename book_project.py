import tkinter as tk
from tkinter import messagebox, simpledialog

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

class DoublyNode:
    def __init__(self, book):
        self.book = book
        self.next = None
        self.prev = None

class DoublyList:
    def __init__(self):
        self.head = None

    def add_book(self, book):
        new_node = DoublyNode(book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current:
                if (book.year < current.book.year or
                    (book.year == current.book.year and book.author < current.book.author) or
                    (book.year == current.book.year and book.author == current.book.author and book.title < current.book.title)):
                    if current == self.head:
                        new_node.next = self.head
                        self.head.prev = new_node
                        self.head = new_node
                        new_node.prev = None
                    else:
                        new_node.prev = current.prev
                        new_node.next = current
                        current.prev.next = new_node
                        current.prev = new_node
                    return
                if not current.next:  # Si llegamos al final de la lista
                    break
                current = current.next

            # Si el libro es el más grande, lo añadimos al final
            current.next = new_node
            new_node.prev = current
            new_node.next = None

    def search_book(self, title):
        current = self.head
        while current:
            if current.book.title == title:
                return current.book
            current = current.next
        return None

    def delete_book(self, title):
        current = self.head
        while current:
            if current.book.title == title:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return True
            current = current.next
        return False

    def show_books(self):
        current = self.head
        books = []
        while current:
            books.append(f"{current.book.title} by {current.book.author} ({current.book.year})")
            current = current.next
        return books

class CircularNode:
    def __init__(self, book):
        self.book = book
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None

    def add_book(self, book):
        new_node = CircularNode(book)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def search_book(self, title):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.book.title == title:
                return current.book
            current = current.next
            if current == self.head:
                break
        return None