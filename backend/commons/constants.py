from enum import Enum

from django.utils.translation import gettext_lazy as _


def enum_to_choice(clazz):
    return [(e[0], e[1].value) for e in clazz.__members__.items()]


class YourAddressBookStatus(Enum):
    """
    예시: 주소록 API에서 사용하는 상태값

    이 클래스는 단순 예시
    이러한 **Code Convention**으로 **상태값을 관리**하면, 코드의 가독성이 높아지고, 유지보수가 쉬워짐

    Attributes 예시:
    - start: 상태 시작
    - complete: 상태 완료
    - problem: 문제 상태
    """

    start = _('Start')
    complete = _('Complete')
    problem = _('Problem')


class Gender(Enum):
    man = _('남성')
    female = _('여성')
    etc = _('기타')
