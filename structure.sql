create table commit_comments
(
	id int auto_increment
		primary key,
	comment_id int null,
	commit_id varchar(45) charset latin1 null,
	project_name varchar(255) charset latin1 null,
	author varchar(255) null,
	path longtext charset latin1 null,
	line int null,
	position int null,
	body_text longtext null,
	body_html longtext null,
	created_at datetime null,
	updated_at datetime null,
	downloaded_at datetime null,
	constraint commit_comments_UN
		unique (comment_id, project_name)
)
collate=utf8mb4_unicode_ci;

create table commits
(
	id int auto_increment
		primary key,
	sha varchar(45) charset latin1 null,
	message mediumtext collate utf8mb4_unicode_ci null,
	author varchar(255) collate utf8mb4_unicode_ci null,
	created_at datetime null,
	committer varchar(255) collate utf8mb4_unicode_ci null,
	committed_at datetime null,
	project_name varchar(255) charset latin1 null,
	downloaded_at datetime null,
	constraint sha_UNIQUE
		unique (sha)
)
charset=utf8mb4;

create table issue_comments
(
	issue_id int null,
	issue_comment_id int not null,
	issue_number int null,
	project_name varchar(255) not null,
	author varchar(255) null,
	body_text longtext collate utf8mb4_unicode_ci null,
	body_html longtext collate utf8mb4_unicode_ci null,
	created_at datetime null,
	updated_at datetime null,
	downloaded_at datetime null,
	primary key (issue_comment_id, project_name)
);

create table issues
(
	issue_id int not null comment 'Issue id for a particular project',
	project_name varchar(255) not null,
	issue_number int null,
	title longtext collate utf8mb4_unicode_ci null,
	reporter varchar(255) null,
	created_at datetime null,
	downloaded_at datetime null,
	body_text longtext collate utf8mb4_unicode_ci null,
	body_html longtext collate utf8mb4_unicode_ci null,
	primary key (issue_id, project_name)
);


