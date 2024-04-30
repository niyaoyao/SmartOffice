create table office_user_info
(
    user_id       int         not null
        primary key,
    zone1_light   varchar(50) not null,
    zone1_fancoil varchar(50) not null,
    zone2_light   varchar(50) not null,
    zone2_fancoil varchar(50) not null,
    office_pau    varchar(50) not null,
    update_time   datetime    null
);

INSERT INTO smartoffice.office_user_info (user_id, zone1_light, zone1_fancoil, zone2_light, zone2_fancoil, office_pau, update_time) VALUES (1, 'off', 'mid', 'low', 'high', 'low', '2024-04-20 21:17:11');
INSERT INTO smartoffice.office_user_info (user_id, zone1_light, zone1_fancoil, zone2_light, zone2_fancoil, office_pau, update_time) VALUES (666, 'low', 'mid', 'low', 'mid', 'low', '2024-04-20 22:10:45');
