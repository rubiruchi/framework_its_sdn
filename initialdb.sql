 -- mysql -u root -pwifi -vvv < mininet-wifi/scripts/initialdb.sql 
DROP DATABASE framework;
CREATE DATABASE framework;
USE framework;
CREATE TABLE appkpi (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, class CHARACTER(1), application VARCHAR(20), e2e_latency FLOAT(7), reliability FLOAT(7), data_rate FLOAT(7), protocol VARCHAR(5), port INT(11));
CREATE TABLE infrastructure (ip VARCHAR (40) NOT NULL PRIMARY KEY, app INT(11));
ALTER TABLE infrastructure ADD CONSTRAINT app FOREIGN KEY (app) REFERENCES appkpi (id);
CREATE TABLE rsu (dpid INT (11) NOT NULL PRIMARY KEY, Region INT(11), limite FLOAT, iface_updtip VARCHAR (10));
CREATE TABLE vehicle (mac VARCHAR(20) NOT NULL, app_id INT(11), region INT(11));
ALTER TABLE vehicle ADD CONSTRAINT fk_app FOREIGN KEY (app_id) REFERENCES appkpi (id);
CREATE TABLE redirect (mac VARCHAR(20) NOT NULL, rsu_o VARCHAR (10), rsu_dest VARCHAR (10), bw_value INT(11));

-- INSERT INTO `appkpi` (`id`, `application`, `class`, `e2e_latency`, `reliability`, `data_rate`, `protocol`, `port`) VALUES (NULL, "CCAS", "A", 50, 0.00001, 0, "UDP", 5002);
INSERT INTO `appkpi` (`id`, `application`, `class`, `e2e_latency`, `reliability`, `data_rate`, `protocol`, `port`) VALUES (NULL, "INS", "B", 3000, 0.001, 500000, "UDP", 5003);
INSERT INTO `appkpi` (`id`, `application`, `class`, `e2e_latency`, `reliability`, `data_rate`, `protocol`, `port`) VALUES (NULL, "4KLV", "C", NULL, NULL, 1000000, "UDP", 5004);

-- INSERT INTO `infrastructure` (`ip`, `app`) VALUES ("200.0.10.2", 1);
INSERT INTO `infrastructure` (`ip`, `app`) VALUES ("200.0.10.3", 1);
INSERT INTO `infrastructure` (`ip`, `app`) VALUES ("200.0.10.4", 2);

INSERT INTO `rsu` (`dpid`, `region`, `limite`, `iface_updtip`) VALUES (6, 1, 6, "rsu1-eth3");
INSERT INTO `rsu` (`dpid`, `region`, `limite`, `iface_updtip`) VALUES (7, 1, 6, "rsu2-eth4");
INSERT INTO `rsu` (`dpid`, `region`, `limite`, `iface_updtip`) VALUES (8, 1, 6, "rsu3-eth3");

INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:01", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:02", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:03", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:04", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:05", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:06", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:07", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:08", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:09", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:10", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:11", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:12", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:13", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:14", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:15", 1, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:16", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:17", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:18", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:19", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:20", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:21", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:22", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:23", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:24", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:25", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:26", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:27", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:28", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:29", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:30", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:31", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:32", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:33", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:34", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:35", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:36", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:37", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:38", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:39", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:40", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:41", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:42", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:43", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:44", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:45", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:46", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:47", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:48", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:49", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:50", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:51", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:52", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:53", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:54", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:55", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:56", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:57", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:58", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:59", 1, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:60", 1, 1);

INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:01", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:02", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:03", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:04", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:05", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:06", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:07", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:08", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:09", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:10", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:11", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:12", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:13", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:14", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:15", 2, 1);
INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:16", 2, 1);

-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:17", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:18", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:19", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:20", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:21", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:22", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:23", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:24", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:25", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:26", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:27", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:28", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:29", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:30", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:31", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:32", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:33", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:34", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:35", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:36", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:37", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:38", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:39", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:40", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:41", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:42", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:43", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:44", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:45", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:46", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:47", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:48", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:49", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:50", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:51", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:52", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:53", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:54", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:55", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:56", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:57", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:58", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:59", 2, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:60", 2, 1);

-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:01", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:02", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:03", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:04", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:05", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:06", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:07", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:08", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:09", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:10", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:11", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:12", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:13", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:14", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:15", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:16", 3, 1);

-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:17", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:18", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:19", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:20", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:21", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:22", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:23", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:24", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:25", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:26", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:27", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:28", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:29", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:30", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:31", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:32", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:33", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:34", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:35", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:36", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:37", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:38", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:39", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:40", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:41", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:42", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:43", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:44", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:45", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:46", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:47", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:48", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:49", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:50", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:51", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:52", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:53", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:54", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:55", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:56", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:57", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:58", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:59", 3, 1);
-- INSERT INTO `vehicle` (`mac`, `app_id`, `region`) VALUES ("00:00:00:00:00:60", 3, 1);