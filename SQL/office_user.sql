create table office_user
(
    id          int auto_increment
        primary key,
    name        varchar(50) not null,
    password    varchar(50) not null,
    update_time datetime    null
);

INSERT INTO smartoffice.office_user (id, name, password, update_time) VALUES (1, 'qmy', 'qmy980902', '2024-04-08 22:06:10');
INSERT INTO smartoffice.office_user (id, name, password, update_time) VALUES (666, 'admin', 'admin', '2024-04-20 19:55:35');
