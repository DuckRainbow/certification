from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    # Пагинатор для отображения 10 элементов на странице
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
