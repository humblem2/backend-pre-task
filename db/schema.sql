-- 기존 데이터베이스 있다면 삭제
DROP DATABASE IF EXISTS AddressBookDB;

-- 데이터베이스 생성
CREATE DATABASE AddressBookDB;

-- 데이터베이스 사용
USE AddressBookDB;

-- 시간 확인
SELECT now() AS `현재시간 확인필요`;

-- 사용자 테이블 생성
CREATE TABLE `User` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '레코드 시퀀스 번호',
    `password` VARCHAR(128) NOT NULL COMMENT '암호화된 사용자 비밀번호',
    `last_login` DATETIME NULL COMMENT '마지막 로그인 시간',
    `is_superuser` BOOLEAN NOT NULL DEFAULT FALSE COMMENT '슈퍼유저 여부',
    `username` VARCHAR(150) NOT NULL UNIQUE COMMENT '유저 이름',
    `first_name` VARCHAR(150) NOT NULL DEFAULT '' COMMENT '유저의 이름',
    `last_name` VARCHAR(150) NOT NULL DEFAULT '' COMMENT '유저의 성',
    `email` VARCHAR(254) NOT NULL UNIQUE COMMENT '유저 이메일(로그인 시 아이디)',
    `is_staff` BOOLEAN NOT NULL DEFAULT FALSE COMMENT '스태프 여부',
    `is_active` BOOLEAN NOT NULL DEFAULT TRUE COMMENT '활성 상태 여부',
    `date_joined` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '가입일',
    `gender` VARCHAR(10) DEFAULT '기타' COMMENT '성별 (예: 남성, 여성, 기타)',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '레코드 생성일',
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '레코드 수정일'
)
;

-- 연락처 테이블 생성
CREATE TABLE `Contact` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '레코드 시퀀스 번호',
    `user_id` INT NOT NULL COMMENT '이 연락처의 소유자. User 테이블 레코드 시퀀스 번호',
    `profile_pic` VARCHAR(2048) COMMENT '연락처의 프로필 사진 URL',
    `name` VARCHAR(200) NOT NULL COMMENT '연락처의 이름',
    `email` VARCHAR(255) COMMENT '연락처의 이메일 주소',
    `phone_number` VARCHAR(15) NOT NULL COMMENT '연락처의 전화번호',
    `company` VARCHAR(200) COMMENT '연락처의 소속 회사',
    `position` VARCHAR(200) COMMENT '연락처의 직책',
    `memo` TEXT COMMENT '연락처에 대한 추가 정보나 메모',
    `address` TEXT COMMENT '연락처의 주소',
    `birthday` DATE COMMENT '연락처의 생일',
    `website` VARCHAR(2048) COMMENT '연락처의 웹사이트 URL',
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '레코드 생성일',
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '레코드 수정일',
    FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE
)
;

-- 라벨 테이블 생성
CREATE TABLE `Label` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '레코드 시퀀스 번호',
    `user_id` INT NOT NULL COMMENT '이 라벨의 소유자. User 테이블 레코드 시퀀스 번호',
    `name` VARCHAR(200) NOT NULL COMMENT '라벨의 이름',
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '레코드 생성일',
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '레코드 수정일',
    FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE
)
;

-- 연락처<->라벨 중간테이블 생성
CREATE TABLE `ContactLabel` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '레코드 시퀀스 번호',
    `contact_id` INT COMMENT 'Contact 테이블 레코드 시퀀스 번호 ',
    `label_id` INT COMMENT 'Label 테이블 레코드 시퀀스 번호',
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '레코드 생성일',
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '레코드 수정일',
    FOREIGN KEY (`contact_id`) REFERENCES `Contact`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`label_id`) REFERENCES `Label`(`id`) ON DELETE CASCADE,
    UNIQUE (`contact_id`, `label_id`)
)
;

-- 인코딩 설정
ALTER TABLE `User` DEFAULT CHARACTER SET = utf8mb4;
ALTER TABLE `Contact` DEFAULT CHARACTER SET = utf8mb4;
ALTER TABLE `Label` DEFAULT CHARACTER SET = utf8mb4;
ALTER TABLE `ContactLabel` DEFAULT CHARACTER SET = utf8mb4;

-- 테이블 별 간단설명
DESC `User`;
DESC `Contact`;
DESC `Label`;
DESC `ContactLabel`;

-- 테이블 별 상세설명
SHOW FULL COLUMNS FROM `User`;
SHOW FULL COLUMNS FROM `Contact`;
SHOW FULL COLUMNS FROM `Label`;
SHOW FULL COLUMNS FROM `ContactLabel`;

-- 테이블 전체 한번에 상세설명
SELECT
    `TABLE_NAME`,
    `COLUMN_NAME`,
    `COLUMN_TYPE`,
    `IS_NULLABLE`,
    `COLUMN_DEFAULT`,
    `COLUMN_COMMENT`,
    `COLUMN_KEY`,
    `EXTRA`,
    `PRIVILEGES`
FROM
    `INFORMATION_SCHEMA`.`COLUMNS`
WHERE
    `TABLE_SCHEMA` = 'AddressBookDB'
    AND `TABLE_NAME` IN ('User', 'Contact', 'Label', 'ContactLabel')
ORDER BY
    `TABLE_NAME`, `ORDINAL_POSITION`
;
