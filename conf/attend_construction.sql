-- faceRecAttend数据库, MySQL5.5
CREATE DATABASE IF NOT EXISTS attend;

-- 部门信息表
CREATE TABLE tab_dept(
	deptid INT PRIMARY KEY AUTO_INCREMENT, -- 部门ID
	deptname VARCHAR(20) NOT NULL,         -- 部门名称
	deptintro VARCHAR(100)                 -- 部门介绍
);

-- 岗位信息表
CREATE TABLE tab_post(
	postid INT PRIMARY KEY AUTO_INCREMENT, -- 岗位ID
	postname VARCHAR(20) NOT NULL,         -- 岗位名称
	postintro VARCHAR(100)                 -- 岗位介绍
);

-- 员工信息表
CREATE TABLE tab_emp(
	empid VARCHAR(12) PRIMARY KEY,    -- 员工ID
	NAME VARCHAR(20) NOT NULL,        -- 姓名
	PASSWORD VARCHAR(32) NOT NULL,    -- 密码
	gender CHAR(2) NOT NULL,          -- 性别:男/女
	phone CHAR(18),                   -- Phone number
	deptid INT,                       -- 部门ID
	postid INT,                       -- 岗位ID
	syslevel INT(2) NOT NULL,         -- 系统级别, 1:系统管理员, 0:普通工作人员
	
	-- 创建外键约束
	CONSTRAINT emp_deptid_fk FOREIGN KEY (deptid) REFERENCES tab_dept(deptid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT emp_postid_fk FOREIGN KEY (postid) REFERENCES tab_post(postid) ON DELETE CASCADE ON UPDATE CASCADE 
);


-- 会务信息表, 只设置开始时间, 不考虑结束时间
CREATE TABLE tab_meeting(
	meetingid VARCHAR(32) PRIMARY KEY,         -- 会议ID
	starttime DATETIME NOT NULL,               -- 会议开始时间
	place VARCHAR(32) NOT NULL,                -- 会议地点
	chairman VARCHAR(20) NOT NULL,             -- 会议主持人
	topic VARCHAR(100) NOT NULL,               -- 会议主题内容
	attenders VARCHAR(100) NOT NULL,           -- 参加人员, 固定格式: 张三, 李四, 王五, ...	
	remarks VARCHAR(100)                       -- 备注,default: 会议时间约1小时, 会议提前15分钟签到, 请准时参会!
);


-- 参会考勤信息表
CREATE TABLE tab_attend(
	meetingid VARCHAR(32) NOT NULL,            -- 会议ID
	empid VARCHAR(12) NOT NULL,                -- 员工ID
	arrivaltime DATETIME,                      -- 到会时间
	islate CHAR(4),                            -- 是否迟到, 到会时间 > starttime, 迟到
	PRIMARY KEY(meetingid, empid),             -- 复合主键
	
	-- 创建外键约束
	CONSTRAINT attend_meetingid_fk FOREIGN KEY (meetingid) REFERENCES tab_meeting(meetingid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT attend_empid_fk FOREIGN KEY (empid) REFERENCES tab_emp(empid) ON DELETE CASCADE ON UPDATE CASCADE
);


-- tab_dept 测试数据
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '软件教研室', '信息技术学院教研室,负责软件技术专业的课程教学任务');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '物联网教研室', '信息技术学院教研室,负责物联网技术专业的课程教学任务');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '计应教研室', '信息技术学院教研室,负责计算机应用技术专业的课程教学任务');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '网络教研室', '信息技术学院教研室,负责大网络技术专业的课程教学任务');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '大数据教研室', '信息技术学院大数据教研室,负责大数据专业的课程教学任务');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '计算机基础课程组', '信息技术学院计算机基础课程组,负责苏州经贸学院计算机应用基础课程的教学任务');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '分团委、辅导员办公室', '信息技术学院分团委、辅导员办公室,负责学院学生管理');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '学院行政办公室', '信息技术学院行政办公室,负责学院日常行政及教务事务管理安排');
INSERT INTO tab_dept(deptid, deptname, deptintro) VALUES(NULL, '机房管理办公室', '信息技术学院机房管理办公室,负责机房维护、资产管理与机房教学安排');

SELECT * FROM tab_dept;

-- tab_post 测试数据
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '教师', '负责专业及基础课程的教学、毕业设计, 指导学生竞赛, 承担班主任等工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '实验员', '负责资产及设备管理,机房维护,机房教学安排等工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '办公室主任', '负责学院日学行政事务安排等工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '教学秘书', '负责教师调课、材料收集下发、教学工作量登记等学院日学教学事务安排工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '辅导员', '负责学生思想教育、评优评先、宿舍管理等学生管理安排工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '分团委书记', '负责学生党建、思想教育、评优评先、宿舍管理等学生管理安排工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '书记', '负责教师与学生党建、指导学院整体发展与日常管理工作');
INSERT INTO tab_post(postid, postname, postintro) VALUES(NULL, '院长', '负责学院整体发展、学院人员安排、专业设置、资产管理等工作');

SELECT * FROM tab_post;

-- tab_emp 测试数据
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel) 
VALUES (2006022501, 'admin', '202cb962ac59075b964b07152d234b70', '男', '13333333333', 1, 1, 1);
INSERT INTO tab_emp
(empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel) 
VALUES (2006022504, '董虎胜', '8888', '男', '18914066046', 1, 1, 1);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022505, '翟高粤', '8888', '男', NULL, 1, 1, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022506, '田英', '8888', '女', NULL, 1, 1, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022526, '陆萍', '8888', '女', NULL, 3, 1, 1);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022511, '李林燕', '8888', '女', NULL, 3, 1, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022512, '戴锐青', '8888', '男', NULL, 6, 1, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022513, '冯蓉珍', '8888', '女', NULL, 2, 1, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022507, '吴健', '8888', '男', NULL, 9, 2, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022508, '廖宇', '8888', '男', NULL, 8, 3, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022509, '陆庆生', '8888', '男', NULL, 8, 7, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022510, '李冬', '8888', '男', NULL, 8, 8, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022515, '冯雁', '8888', '女', NULL, 8, 8, 0);
INSERT INTO tab_emp (empid, NAME, PASSWORD, gender, phone, deptid, postid, syslevel)
VALUES (2006022514, '蔡达君', '8888', '男', NULL, 8, 7, 0);

SELECT * FROM tab_emp;

-- tab_meeting测试数据
INSERT INTO tab_meeting (meetingid, starttime, place, chairman, topic, attenders, remarks)
VALUES ('20191208130000', '2019-12-08 13:00:00', '3318会议室','李冬', '讨论下学期培养方案与课程设置', '冯雁, 董虎胜, 宋志强, 施连敏, 方武', '会议时间约1小时, 会议提前15分钟签到, 请准时参会!');
INSERT INTO tab_meeting (meetingid, starttime,  place, chairman, topic, attenders, remarks)
VALUES ('20191209100000', '2019-12-09 10:00:00', '3318会议室', '陆庆生','安排近期党务工作与民主评议', '蔡达君, 柳青, 张香宁, 董虎胜, 宋志强, 施连敏', '会议时间约0.5小时, 会议提前15分钟签到, 请准时参会!');

SELECT * FROM tab_meeting;
