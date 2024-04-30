create table office_user_log
(
    id           int auto_increment,
    user_id      int      not null,
    start_time_1 datetime not null,
    start_time_2 datetime not null,
    end_time_1   datetime not null,
    end_time_2   datetime not null,
    primary key (id, user_id)
);

INSERT INTO smartoffice.office_user_log (id, user_id, start_time_1, start_time_2, end_time_1, end_time_2) VALUES (1, 1, '2024-04-20 09:00:00', '2024-04-20 14:00:00', '2024-04-20 12:00:00', '2024-04-20 18:00:00');
INSERT INTO smartoffice.office_user_log (id, user_id, start_time_1, start_time_2, end_time_1, end_time_2) VALUES (2, 666, '2024-04-20 09:11:04', '2024-04-20 14:11:19', '2024-04-20 11:11:25', '2024-04-20 17:11:37');
