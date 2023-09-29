import re

from rest_framework.exceptions import ValidationError


def is_valid_phone_number(number: str):
    """(KR) 휴대폰번호 또는 일반전화번호 형식인지 검사"""
    mobile_pattern = r'^010-\d{3,4}-\d{4}$'
    landline_pattern = r'^(02|031|032|033|041|042|043|044|051|052|053|054|055|061|062|063|064)-\d{3,4}-\d{4}$'
    if not (re.match(mobile_pattern, number) or re.match(landline_pattern, number)):
        raise ValidationError('This is not a valid phone number format. e.g., 010-1234-5678, 02-123-4567')
