from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #Нельзя добавить одну и ту же книгу дважды
    def test_add_same_book_twice_false(self):
        collector = BooksCollector()
        collector.add_new_book('Сказки Пушкина')
        collector.add_new_book('Сказки Пушкина')
        assert len(collector.get_books_rating()) == 1

    #Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_rating_books_from_list_false(self):
        collector = BooksCollector()
        collector.set_book_rating('Как заработать миллион проблем', 6)
        assert collector.books_rating == {}

    #Нельзя выставить рейтинг меньше 1
    def test_set_rating_less_then_one_false(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби' : 1}

    #Нельзя выставить рейтинг больше 10
    def test_set_rating_more_then_ten_false(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 11)
        assert collector.get_books_rating() == {'Что делать, если ваш кот хочет вас убить' : 1}

    #У не добавленной книги нет рейтинга.
    def test_get_book_not_in_list_false(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Преступление и наказание') is None

    #Добавление книги в избранное
    def test_add_book_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Атлант расправил плечи')
        collector.add_book_in_favorites('Атлант расправил плечи')
        assert collector.favorites == ['Атлант расправил плечи']

    #Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_which_not_in_dict_false(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert collector.favorites == []

    #Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Aтлант расправил плечи')
        collector.add_book_in_favorites('Атлант расправил плечи')
        collector.delete_book_from_favorites('Атлант расправил плечи')
        assert collector.favorites == []
