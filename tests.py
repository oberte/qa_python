
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Kniga_1')
        assert 'Kniga_1' in collector.books_genre

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_2")
        collector.set_book_genre("Kniga_2", "Детективы")
        assert collector.get_book_genre("Kniga_2") == "Детективы"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_3")
        collector.set_book_genre("Kniga_3", "Комедии")
        collector.add_new_book("Kniga_4")
        collector.set_book_genre("Kniga_4", "Комедии")
        assert collector.get_books_with_specific_genre("Комедии") == ["Kniga_3", "Kniga_4"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_5")
        collector.set_book_genre("Kniga_5", "Мультфильмы")
        collector.add_new_book("Kniga_6")
        collector.set_book_genre("Kniga_6", "Ужасы")
        assert collector.get_books_for_children() == ["Kniga_5"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_6")
        collector.add_book_in_favorites("Kniga_6")
        assert "Kniga_6" in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_7")
        collector.add_book_in_favorites("Kniga_7")
        collector.delete_book_from_favorites("Kniga_7")
        assert "Kniga_7" not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_8")
        collector.add_new_book("Kniga_9")
        collector.add_book_in_favorites("Kniga_8")
        collector.add_book_in_favorites("Kniga_9")
        assert collector.get_list_of_favorites_books() == ["Kniga_8", "Kniga_9"]

    def test_limitation_on_book_name(self):
        collector = BooksCollector()
        book_name = "A" * 41
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_only_once(self):
        collector = BooksCollector()
        collector.add_new_book("Kniga_10")
        collector.add_new_book("Kniga_10")
        assert len(collector.books_genre) == 1