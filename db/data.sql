-- 데이터베이스 사용
USE AddressBookDB;

-- ===========================================
-- User 테이블에 대한 더미데이터 총 4개
-- ===========================================

INSERT INTO `user` (password, username, email, gender) VALUES ('pbkdf2_sha256$260000$tA9uanCJCRZ5R9CGkOBi2l$AZk3EDoB953tBq7m9yJkNtNinht0t+Z4Y4hOliiSWxY=','테스트성명1','test1@test.com','남성');
INSERT INTO `user` (password, username, email, gender) VALUES ('pbkdf2_sha256$260000$031CZSo94Vb2l3XmXKE4Yu$WB2fESnFYblJuXO1QAPNPXRlCgKQGE97FokGugMvtC0=','테스트성명2','test2@test.com','여성');
INSERT INTO `user` (password, username, email, gender) VALUES ('pbkdf2_sha256$260000$52kpjevhj5zrhuOWwNIzbR$vgeT4pD/kLDjMDecRQiNxoj9ES+QOIAq0iFn/wrD/rc=','테스트성명3','test3@test.com','남성');
INSERT INTO `user` (password, username, email) VALUES ('pbkdf2_sha256$260000$kVFRWh2yDh0oHA2hDliLLN$8fbvsR15oWk4/j74XgVCX4RENQfq1UAFA9T1EhZ0RbA=','테스트성명4','test4@test.com');

-- ===========================================
-- Contact 테이블에 대한 더미데이터 총 50개
-- ===========================================

INSERT INTO `Contact` (`user_id`, `profile_pic`, `name`, `email`, `phone_number`, `company`, `position`, `memo`, `address`, `birthday`, `website`)
VALUES
-- 1번 사용자에 대한 더미데이터 20개
(1, 'https://example.com/profile1.jpg', '조영희', 'younghee1@example.com', '010-1234-5671', 'ABC Corp', '과장', '코드 좋아함', '서울시 강남구 A동', '1990-01-01', 'https://younghee.com'),
(1, 'https://example.com/profile2.jpg', '이철수', 'cheolsoo2@example.com', '010-1234-5672', 'XYZ Corp', '개발자', '등산 좋아함', '서울시 서초구 B동', '1992-02-02', 'https://cheolsoo.com'),
(1, 'https://example.com/profile3.jpg', '박지영', 'jiyoung3@example.com', '010-1234-5673', 'OPQ Corp', '디자이너', '여행 좋아함', '경기도 수원시 C동', '1988-03-03', 'https://jiyoung.com'),
(1, 'https://example.com/profile4.jpg', '최민수', 'minsoo4@example.com', '010-1234-5674', 'LMN Corp', '매니저', '게임 좋아함', '인천시 연수구 D동', '1986-04-04', 'https://minsoo.com'),
(1, 'https://example.com/profile5.jpg', '정수진', 'soojin5@example.com', '010-1234-5675', 'KLM Corp', '부장', '독서 좋아함', '부산시 해운대구 E동', '1987-05-05', 'https://soojin.com'),
(1, 'https://example.com/profile6.jpg', '김영희', 'kimyounghui86@example.com', '02-1234-5686', 'Hanbok Corp', '대표', '한복 전문점', '서울시 종로구 A동', '1975-01-11', 'https://kimyounghui.com'),
(1, 'https://example.com/profile7.jpg', '박철수', 'parkcheolsoo87@example.com', '02-1234-5687', 'Farming Corp', '대표', '농작물 판매', '서울시 강남구 B동', '1969-02-12', 'https://parkcheolsoo.com'),
(1, 'https://example.com/profile8.jpg', '이순자', 'leesoonja88@example.com', '031-1234-5688', 'Handicraft Corp', '대표', '전통 공예품 제작', '경기도 성남시 C동', '1978-03-13', 'https://leesoonja.com'),
(1, 'https://example.com/profile9.jpg', '최봉준', 'choibongjoon89@example.com', '032-1234-5689', 'OldBook Corp', '대표', '고전 서적 판매', '인천시 부평구 D동', '1972-04-14', 'https://choibongjoon.com'),
(1, 'https://example.com/profile10.jpg', '정희숙', 'jungheesook90@example.com', '033-1234-5690', 'Hanji Corp', '대표', '한지 제작 및 판매', '강원도 춘천시 E동', '1973-05-15', 'https://jungheesook.com'),
(1, 'https://example.com/profile11.jpg', '윤명숙', 'yoonmyungsook91@example.com', '041-1234-5691', 'TeaHouse Corp', '대표', '전통 찻집 운영', '충청북도 청주시 F동', '1974-06-16', 'https://yoonmyungsook.com'),
(1, 'https://example.com/profile12.jpg', '송옥순', 'songoksoon92@example.com', '042-1234-5692', 'Tradition Corp', '대표', '전통 의상 제작', '충청남도 대전시 G동', '1976-07-17', 'https://songoksoon.com'),
(1, 'https://example.com/profile13.jpg', '조영남', 'joyoungnam93@example.com', '051-1234-5693', 'Classic Corp', '대표', '고전 음악 연주', '부산시 동래구 H동', '1977-08-18', 'https://joyoungnam.com'),
(1, 'https://example.com/profile14.jpg', '황순영', 'hwangsoonyoung94@example.com', '052-1234-5694', 'History Corp', '대표', '역사 강연 및 출판', '울산시 중구 I동', '1979-09-19', 'https://hwangsoonyoung.com'),
(1, 'https://example.com/profile15.jpg', '심희선', 'shimheesun95@example.com', '053-1234-5695', 'TraditionArt Corp', '대표', '전통 미술 강좌 운영', '대구시 수성구 J동', '1980-10-20', 'https://shimheesun.com'),
(1, 'https://example.com/profile16.jpg', '송지아', 'jia59@example.com', '010-1234-5689', 'RST Corp', '과장', '요리 좋아함', '대전시 중구 I동', '1991-09-09', 'https://jia.com'),
(1, 'https://example.com/profile17.jpg', '남지우', 'jiwoo60@example.com', '010-1234-5690', 'UVW Corp', '팀장', '운동 좋아함', '울산시 남구 J동', '1989-10-10', 'https://jiwoo.com'),
(1, 'https://example.com/profile18.jpg', '김하준', 'kimhajun61@example.com', '010-1234-5691', 'NOV Corp', '과장', '피아노 좋아함', '서울시 마포구 A동', '1995-01-11', 'https://kimhajun.com'),
(1, 'https://example.com/profile19.jpg', '박서아', 'parkseoah62@example.com', '010-1234-5692', 'PRW Corp', '개발자', '요가 좋아함', '서울시 서초구 B동', '1996-02-12', 'https://parkseoah.com'),
(1, 'https://example.com/profile20.jpg', '이시우', 'leesiwoo63@example.com', '010-1234-5693', 'XYZ Corp', '디자이너', '사진촬영 좋아함', '경기도 고양시 C동', '1993-03-13', 'https://leesiwoo.com'),
-- 2번 사용자에 대한 더미데이터 15개
(2, 'https://example.com/profile21.jpg', '최유준', 'choiyujun64@example.com', '010-1234-5694', 'ZBC Corp', '매니저', '바둑 좋아함', '인천시 연수구 D동', '1992-04-14', 'https://choiyujun.com'),
(2, 'https://example.com/profile22.jpg', '정하린', 'jungharin65@example.com', '010-1234-5695', 'OPQ Corp', '팀장', '서핑 좋아함', '부산시 해운대구 E동', '1994-05-15', 'https://jungharin.com'),
(2, 'https://example.com/profile23.jpg', '윤서진', 'yoonseojin66@example.com', '010-1234-5696', 'LMN Corp', '부장', '드라이브 좋아함', '대구시 중구 F동', '1993-06-16', 'https://yoonseojin.com'),
(2, 'https://example.com/profile24.jpg', '송지호', 'songjiho67@example.com', '010-1234-5697', 'RST Corp', '과장', '캠핑 좋아함', '광주시 북구 G동', '1996-07-17', 'https://songjiho.com'),
(2, 'https://example.com/profile25.jpg', '조민재', 'jominjae68@example.com', '010-1234-5698', 'UVW Corp', '사장', '등산 좋아함', '울산시 동구 H동', '1991-08-18', 'https://jominjae.com'),
(2, 'https://example.com/profile26.jpg', '황은우', 'hwangeunwoo69@example.com', '010-1234-5699', 'XYZ Corp', '부사장', '테니스 좋아함', '대전시 서구 I동', '1992-09-19', 'https://hwangeunwoo.com'),
(2, 'https://example.com/profile27.jpg', '심하율', 'simhayul70@example.com', '010-1234-5610', 'ABC Corp', '대리', '골프 좋아함', '세종시 도담동 J동', '1993-10-20', 'https://simhayul.com'),
(2, 'https://example.com/profile28.jpg', '김밥천국', 'kimbapheaven71@example.com', '02-1234-5671', 'Food Corp', '대표', '맛있는 김밥', '서울시 강북구 A동', '2000-01-11', 'https://kimbapheaven.com'),
(2, 'https://example.com/profile29.jpg', '이삭토스트', 'isaac72@example.com', '02-1234-5672', 'Toast Corp', '대표', '토스트 전문점', '서울시 강남구 B동', '1999-02-12', 'https://isaactoast.com'),
(2, 'https://example.com/profile30.jpg', '박가네 집밥', 'parkhome73@example.com', '031-1234-5673', 'HomeFood Corp', '대표', '집밥 뷔페', '경기도 성남시 C동', '2001-03-13', 'https://parkhomefood.com'),
(2, 'https://example.com/profile31.jpg', '최씨네 떡볶이', 'choittok74@example.com', '032-1234-5674', 'Snack Corp', '대표', '매운 떡볶이', '인천시 부평구 D동', '2002-04-14', 'https://choittok.com'),
(2, 'https://example.com/profile32.jpg', '정식당', 'jungdining75@example.com', '033-1234-5675', 'Dining Corp', '대표', '한식 레스토랑', '강원도 춘천시 E동', '2003-05-15', 'https://jungdining.com'),
(2, 'https://example.com/profile33.jpg', '윤밀당', 'yoonmildang76@example.com', '041-1234-5676', 'Bakery Corp', '대표', '빵집', '충청북도 청주시 F동', '2004-06-16', 'https://yoonbakery.com'),
(2, 'https://example.com/profile34.jpg', '송식당', 'songdining77@example.com', '042-1234-5677', 'Food Corp', '대표', '양식 전문점', '충청남도 대전시 G동', '2005-07-17', 'https://songdining.com'),
(2, 'https://example.com/profile35.jpg', '조국장집', 'jokukjang78@example.com', '051-1234-5678', 'Sauce Corp', '대표', '간장·된장 전문', '부산시 동래구 H동', '2006-08-18', 'https://jokukjang.com'),
-- 3번 사용자에 대한 더미데이터 10개
(3, 'https://example.com/profile36.jpg', '황수제비', 'hwangsoojebi79@example.com', '052-1234-5679', 'Noodle Corp', '대표', '수제비 전문', '울산시 중구 I동', '2007-09-19', 'https://hwangsoojebi.com'),
(3, 'https://example.com/profile37.jpg', '심국수집', 'shimnoodle80@example.com', '053-1234-5610', 'Noodle Corp', '대표', '칼국수 맛집', '대구시 수성구 J동', '2008-10-20', 'https://shimnoodle.com'),
(3, 'https://example.com/profile38.jpg', '오성식품', 'osungfood101@example.com', '02-4567-1101', 'Food Corp', '대표', '순대 전문점', '서울시 동대문구 A동', '1985-01-11', 'https://osungfood.com'),
(3, 'https://example.com/profile39.jpg', '나라밥상', 'narafood102@example.com', '02-4567-1102', 'Restaurant Corp', '대표', '한식 레스토랑', '서울시 강서구 B동', '1980-02-12', 'https://narafood.com'),
(3, 'https://example.com/profile40.jpg', '백송식당', 'baeksong103@example.com', '031-4567-1103', 'Dining Corp', '대표', '백반집', '경기도 안양시 C동', '1988-03-13', 'https://baeksongdining.com'),
(3, 'https://example.com/profile41.jpg', '탄방국수', 'tanbang104@example.com', '032-4567-1104', 'Noodle Corp', '대표', '국수 전문점', '인천시 연수구 D동', '1975-04-14', 'https://tanbangnoodle.com'),
(3, 'https://example.com/profile42.jpg', '금산콩나물', 'geumsan105@example.com', '033-4567-1105', 'Food Corp', '대표', '콩나물 요리 전문', '강원도 원주시 E동', '1990-05-15', 'https://geumsanbean.com'),
(3, 'https://example.com/profile43.jpg', '풍년식당', 'poongnyeon106@example.com', '041-4567-1106', 'Dining Corp', '대표', '퓨전 한식 레스토랑', '충청북도 청주시 F동', '1982-06-16', 'https://poongnyeondining.com'),
(3, 'https://example.com/profile44.jpg', '동해해물', 'donghaeseafood107@example.com', '042-4567-1107', 'Seafood Corp', '대표', '해물탕 전문점', '충청남도 아산시 G동', '1983-07-17', 'https://donghaeseafood.com'),
(3, 'https://example.com/profile45.jpg', '서산집', 'seosanhouse108@example.com', '051-4567-1108', 'Restaurant Corp', '대표', '전통 한식 레스토랑', '부산시 남구 H동', '1979-08-18', 'https://seosanhouse.com'),
-- 4번 사용자에 대한 더미데이터 5개
(4, 'https://example.com/profile46.jpg', '제주바다', 'jejusea109@example.com', '052-4567-1109', 'Seafood Corp', '대표', '회 전문점', '울산시 남구 I동', '1989-09-19', 'https://jejuseafood.com'),
(4, 'https://example.com/profile47.jpg', '함평떡집', 'hampyeongrice110@example.com', '053-4567-1110', 'Dessert Corp', '대표', '떡 전문 판매', '대구시 동구 J동', '1978-10-20', 'https://hampyeongricecake.com'),
(4, 'https://example.com/profile48.jpg', '경북삼계탕', 'gyeongbukchicken111@example.com', '054-4567-1111', 'Restaurant Corp', '대표', '삼계탕 전문점', '경상북도 경산시 K동', '1981-11-21', 'https://gyeongbukchicken.com'),
(4, 'https://example.com/profile49.jpg', '전북비빔밥', 'jeonbukbibimbap112@example.com', '063-4567-1112', 'Restaurant Corp', '대표', '비빔밥 전문점', '전라북도 전주시 L동', '1977-07-14', 'https://jeonbukbibimbap.com'),
(4, 'https://example.com/profile50.jpg', '충청도보신탕', 'chungcheongdogoback113@example.com', '043-4567-1113', 'Restaurant Corp', '대표', '보신탕 전문점', '충청북도 청주시 M동', '1982-09-25', 'https://chungcheongdogoback.com')
;

-- ===========================================
-- Label 테이블에 더미데이터 총 25개
-- ===========================================

-- 1번 유저가 라벨 생성 10개
INSERT INTO `Label` (`user_id`, `name`)
VALUES
(1, '식당'),
(1, '회사동료'),
(1, '여자'),
(1, '남자'),
(1, '중학교'),
(1, '고등학교'),
(1, '초등학교'),
(1, '대학교'),
(1, '가족'),
(1, '기타')
;

-- 2번 유저가 라벨 생성 7개
INSERT INTO `Label` (`user_id`, `name`)
VALUES
(2, '중학교'),
(2, '고등학교'),
(2, '초등학교'),
(2, '대학교'),
(2, '회사동료'),
(2, '여자'),
(2, '남자')
;

-- 3번 유저가 라벨 생성 5개
INSERT INTO `Label` (`user_id`, `name`)
VALUES
(3, '대학교'),
(3, '가족'),
(3, '식당'),
(3, '여자'),
(3, '남자')
;

-- 4번 유저가 라벨 생성 3개
INSERT INTO `Label` (`user_id`, `name`)
VALUES
(4, '대학교'),
(4, '가족'),
(4, '기타')
;

-- ===========================================
-- ContactLabel 테이블에 대한 더미데이터 생성
-- ===========================================

-- 1번유저의 연락처에 대한 라벨 매핑
INSERT INTO `ContactLabel` (`contact_id`, `label_id`)
VALUES
(1, 1), (1, 2), (1, 3), (2, 1), (2, 4), (2, 5), (2, 6), (3, 2), (3, 3), (3, 5), (4, 1), (4, 4), (5, 3), (5, 5), (5, 6), (6, 1), (6, 7), (6, 9), (7, 8), (7, 9), (8, 1), (8, 4), (8, 5), (9, 1), (9, 3), (9, 6), (9, 7), (10, 2), (10, 5), (11, 1), (11, 3), (12, 1), (12, 4), (12, 5), (13, 6), (13, 8), (14, 2), (14, 7), (14, 9), (15, 3), (15, 10), (16, 4), (16, 6), (16, 8), (17, 2), (17, 5), (17, 7), (18, 1), (18, 3), (18, 9), (19, 2), (19, 10), (20, 4), (20, 6), (20, 8), (20, 10)
;

-- 2번유저의 연락처에 대한 라벨 매핑
INSERT INTO `ContactLabel` (`contact_id`, `label_id`)
VALUES
(21, 11), (21, 12), (22, 13), (22, 14), (23, 15), (23, 16), (24, 11), (24, 13), (25, 14), (25, 15), (26, 11), (26, 16), (27, 13), (27, 17), (28, 12), (28, 14), (29, 16), (29, 17), (30, 11), (30, 15), (31, 13), (31, 14), (32, 15), (32, 16), (33, 12), (33, 17), (34, 11), (34, 13), (35, 14), (35, 16)
;

-- 3번유저의 연락처에 대한 라벨 매핑
INSERT INTO `ContactLabel` (`contact_id`, `label_id`)
VALUES
(36, 18), (36, 19), (37, 19), (37, 20), (38, 20), (38, 21), (39, 18), (39, 21), (40, 19), (40, 22), (41, 18), (41, 22), (42, 20), (42, 21), (43, 19), (43, 22), (44, 18), (44, 19), (45, 21), (45, 22)
;

-- 4번유저의 연락처에 대한 라벨 매핑
INSERT INTO `ContactLabel` (`contact_id`, `label_id`)
VALUES
(46, 23), (46, 24), (47, 23), (47, 25), (48, 24), (48, 25), (49, 23), (49, 24), (50, 24), (50, 25)
;
