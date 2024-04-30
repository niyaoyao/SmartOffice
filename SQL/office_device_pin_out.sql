create table office_device_pin_out
(
    id          int auto_increment
        primary key,
    name        varchar(50) not null,
    state       varchar(50) not null,
    pin0        varchar(50) not null,
    pin1        varchar(50) not null,
    pin2        varchar(50) not null,
    pin3        varchar(50) not null,
    pin4        varchar(50) not null,
    pin5        varchar(50) not null,
    pin6        varchar(50) not null,
    pin7        varchar(50) not null,
    pin8        varchar(50) not null,
    pin9        varchar(50) not null,
    pin10       varchar(50) not null,
    pin11       varchar(50) not null,
    pin12       varchar(50) not null,
    pin13       varchar(50) not null,
    pin14       varchar(50) not null,
    update_time datetime    null
);

INSERT INTO smartoffice.office_device_pin_out (id, name, state, pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, update_time) VALUES (1, 'zone1_light', 'off', '0', '0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', '2024-04-09 22:52:00');
INSERT INTO smartoffice.office_device_pin_out (id, name, state, pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, update_time) VALUES (2, 'zone1_light', 'low', '1', '0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', '2024-04-09 22:52:00');
