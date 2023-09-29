from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Address-book RESTful API",
        default_version='v1',
        description=(
            ": 사용자의 연락처 정보를 관리하고 조회하기 위한 API 서비스입니다.\n\n"
            "- **'연락처(Contact)'**, **'라벨(Label)'** 에 대하여 `추가`, `목록 조회`, `상세 조회`, `전체 수정`, `부분 수정`, `삭제` 기능을 제공합니다.\n\n"
            "- **'연락처(Contact)'** 에 다수의 **'라벨(Label)'** 을 `연결`하거나 `해제`할 수 있습니다.\n"
            "- 특정 **'라벨(Label)'** 과 연결된 다수의 **'연락처(Contact)'** 를 `목록 조회`할 수 있습니다."
        ),
        terms_of_service="https://www.<서비스도메인>.com/terms/",
        contact=openapi.Contact(
            name="Backend Team",
            email="humblem2@naver.com",
            url="https://www.<서비스도메인>.com/support/teamblog/주소록"
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    authentication_classes=[],
)
