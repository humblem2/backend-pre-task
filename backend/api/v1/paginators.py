from rest_framework.pagination import PageNumberPagination


class DefaultContactPagination(PageNumberPagination):
    """연락처 테이블에 대한 기본 페이징"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    last_page_strings = ['last']


class DefaultContactLabelPagination(PageNumberPagination):
    """연락처-라벨 테이블에 대한 기본 페이징"""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    last_page_strings = ['last']

