<div style="margin-bottom: -38px;"> 

![Code Coverage Badge](https://img.shields.io/badge/Coverage-96.00%25-brightgreen?logo=pytest&logoColor=white)
![Swagger Badge](https://img.shields.io/badge/Swagger-used-8A2BE2?logo=swagger&logoColor=white)
![DRF Badge](https://img.shields.io/badge/DRF-used-1E90FF?logo=django&logoColor=white)
![MySQL Badge](https://img.shields.io/badge/MySQL-used-orange?logo=mysql&logoColor=white)
![API Version Badge](https://img.shields.io/badge/API%20Version-1.0.0-brightgreen)

</div>

# backend-pre-task

키즈노트 BE개발 사전과제 repository입니다.
***

### 주요 버전
* Python: `3.9.3`
* Django: `3.2.20`
* Django REST Framework: `3.14.0`
* DBMS: MySQL (ver. `8.0.27`)

<p style="display: inline-block; vertical-align: middle;">현재 code coverage는</p> 

  <img alt="Static Badge" src="https://img.shields.io/badge/Coverage-96.00%25-brightgreen" style="vertical-align: middle;">

<p style="display: inline-block; vertical-align: middle;">입니다.</p>

***

### backend-pre-task/backend/README.md
* [바로가기](./backend/README.md)

***

## BE 개발자 사전 과제
```text
안녕하세요
키즈노트 백엔드에 관심을 가지고 지원해 주셔서 감사합니다. 🤗
사전과제는 테스트의 목적이 아닌 지원자 분의 개발 스타일을 사전에 알아보고 맞춰가기 위해 요청드립니다.
팀원과 협업을 한다는 생각으로 작업을 해 주시면 됩니다.
정답이 따로 있지는 않기에 편하게 작업해 주세요. 😄
```
***

### 진행방법
```text
상세 진행 방법은 다음과 같습니다.
```
1. 도메인 요구사항을 읽고 어떤 내용의 작업을 진행하면 되는지 확인해 주세요.
2. 기술적 요구사항에서 구현 시 기술적으로 어떤 점을 고려하면 되는지 확인해 주세요.
3. 과제 repository에서 자신의 github으로 fork 해 주세요.
4. 과제는 DB와 Model 설계, API를 개발하시면 됩니다.
5. 작업이 완료되면 이메일로 개인 repository 링크를 첨부해 회신해 주세요.

***
### 도메인 요구사항

```text
주소록과 연락처 상세 내용을 구현해 주세요.
Google의 주소록(https://contacts.google.com)을 참고해 주시면 이해가 편할 것 같습니다.
```
- 주소록
  - 목록
    - 목록에 출력될 필드는 다음과 같습니다.
      - 프로필 사진
      - 이름
      - 이메일
      - 전화번호
      - 회사 (직책)
      - 라벨
    - 정렬
      - 기본 출력은 등록 순서대로 정렬합니다.
      - 이름, 이메일, 전화번호 중 하나를 선택하여 정렬할 수 있습니다.
      - 정렬은 오름차순/내림차순/해제 순입니다.
    - 페이징
      - 스크롤 페이징 처리가 되도록합니다.
  - 연락처 (상세보기/입력)
    - 입/출력 필드는 다음과 같습니다.
      - 프로필 사진 : url 입력 방식
      - 이름
      - 이메일
      - 전화번호
      - 회사
      - 직책
      - 메모
      - 라벨
        - 사용자 정의 라벨
        - 연락처 1개에 라벨 다수 연결 가능
      - 기타 항목 추가
        - 주소
        - 생일
        - 웹사이트

***
### 기술적 요구사항
```text
기술적 요구사항은 다음과 같습니다.
```
- 환경
  - python : 3.9.3
  - django : 3.2.20
  - django-rest-framework : 3.14.0
  - MySQL or SQLite (택1)
  - 기타 필요한 패키지 사용 가능하며, `requirements.txt`에 추가 
- Backend
  - django ORM의 model을 이용해 주세요.
  - 디렉터리 구조는 본인이 생각하는 Best Practice로 구성해 주세요.
  - **RESTfull** 하게 API를 설계해 주세요.
- Database
  - DB는 MySQL 또는 SQLite를 사용해 주세요.
  - `/db` 디렉터리에 설계한 스키마 및 데이터를 정의해 주세요
    - schema.sql : DB 스키마를 CREATE 문으로 작성해 주세요
    - data.sql : 기본 데이터가 필요하다면 INSERT 문으로 넣어주세요
  - 설계하신 ERD가 있으시면 `/db` 디렉터리 안에 추가해 주시면 도움이 될 것 같습니다. (`선택사항`)
- 기타 (`선택사항`)
  - 선택사항으로 작성하실 경우에만 확인합니다.
    - swagger
    - test code

  
