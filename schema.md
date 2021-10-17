# Database: Capstone

| Tables_in_capstone |
|--------------------|
| Evaluations        |
| Group_Mentors      |
| Heads              |
| Mentors            |
| Panel_Group        |
| Panel_Mark         |
| Panel_Parameter    |
| Panelists          |
| Requests           |
| Students           |
| Teams              |


## Evaluations
| Field         | Type    | Null | Key | Default | Extra          |
|---------------|---------|------|-----|---------|----------------|
| evaluation_no | int(11) | NO   | PRI | NULL    | auto_increment |
| max_marks     | int(11) | YES  |     | NULL    |                |
| start_date    | date    | YES  |     | NULL    |                |
| end_date      | date    | YES  |     | NULL    |                |


## Group_Mentors
| Field      | Type    | Null | Key | Default | Extra |
|------------|---------|------|-----|---------|-------|
| group_id   | int(11) | NO   | PRI | NULL    |       |
| mentor1_id | int(11) | NO   | MUL | NULL    |       |
| mentor2_id | int(11) | YES  | MUL | NULL    |       |


### Mentors
| Field     | Type         | Null | Key | Default | Extra          |
|-----------|--------------|------|-----|---------|----------------|
| mentor_id | int(11)      | NO   | PRI | NULL    | auto_increment |
| name      | varchar(100) | NO   |     | NULL    |                |
| email     | varchar(100) | NO   | UNI | NULL    |                |
| password  | varchar(300) | NO   |     | NULL    |                |

## Panelists
| Field     | Type    | Null | Key | Default | Extra |
|-----------|---------|------|-----|---------|-------|
| panel_no  | int(11) | NO   | PRI | NULL    |       |
| panel_id  | int(11) | NO   | PRI | NULL    |       |
| mentor_id | int(11) | NO   | PRI | NULL    |       |
| head      | int(11) | YES  |     | NULL    |       |

## Panel_Group
| Field    | Type    | Null | Key | Default | Extra |
|----------|---------|------|-----|---------|-------|
| panel_no | int(11) | NO   | PRI | NULL    |       |
| panel_id | int(11) | NO   | PRI | NULL    |       |
| group_id | int(11) | NO   | PRI | NULL    |       |

## Panel_Marks
| Field             | Type    | Null | Key | Default | Extra |
|-------------------|---------|------|-----|---------|-------|
| roll_no           | int(11) | NO   | PRI | NULL    |       |
| panel_no          | int(11) | NO   | PRI | NULL    |       |
| parameter1_marks  | int(11) | YES  |     | NULL    |       |
| parameter2_marks  | int(11) | YES  |     | NULL    |       |
| parameter3_marks  | int(11) | YES  |     | NULL    |       |
| parameter4_marks  | int(11) | YES  |     | NULL    |       |
| parameter5_marks  | int(11) | YES  |     | NULL    |       |
| parameter6_marks  | int(11) | YES  |     | NULL    |       |
| parameter7_marks  | int(11) | YES  |     | NULL    |       |
| parameter8_marks  | int(11) | YES  |     | NULL    |       |
| parameter9_marks  | int(11) | YES  |     | NULL    |       |
| parameter10_marks | int(11) | YES  |     | NULL    |       |



## Panel_Parameter
| Field        | Type        | Null | Key | Default | Extra |
|--------------|-------------|------|-----|---------|-------|
| panel_no     | int(11)     | NO   | PRI | NULL    |       |
| parameter_no | int(11)     | NO   | PRI | NULL    |       |
| name         | varchar(30) | YES  |     | NULL    |       |
| max_marks    | int(11)     | YES  |     | NULL    |       |


## Requests
| Field            | Type         | Null | Key | Default | Extra          |
|------------------|--------------|------|-----|---------|----------------|
| group_id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| leader_roll_no   | int(11)      | NO   |     | NULL    |                |
| title            | varchar(100) | NO   |     | NULL    |                |
| student2_roll_no | int(11)      | NO   |     | NULL    |                |
| student3_roll_no | int(11)      | YES  |     | NULL    |                |
| student4_roll_no | int(11)      | YES  |     | NULL    |                |
| email            | varchar(100) | NO   |     | NULL    |                |
| leader_name      | varchar(100) | NO   |     | NULL    |                |
| student2_name    | varchar(100) | NO   |     | NULL    |                |
| student3_name    | varchar(100) | YES  |     | NULL    |                |
| student4_name    | varchar(100) | YES  |     | NULL    |                |
| phone            | varchar(100) | NO   |     | NULL    |                |
| mentor_id        | int(11)      | NO   | MUL | NULL    |                |



## Students
| Field             | Type         | Null | Key | Default | Extra |
|-------------------|--------------|------|-----|---------|-------|
| group_id          | int(11)      | NO   | PRI | NULL    |       |
| roll_no           | int(11)      | NO   | PRI | NULL    |       |
| name              | varchar(100) | NO   |     | NULL    |       |
| evaluation1_marks | int(11)      | YES  |     | NULL    |       |
| evaluation2_marks | int(11)      | YES  |     | NULL    |       |
| evaluation3_marks | int(11)      | YES  |     | NULL    |       |
| evaluation4_marks | int(11)      | YES  |     | NULL    |       |
| evaluation5_marks | int(11)      | YES  |     | NULL    |       |
| evaluation6_marks | int(11)      | YES  |     | NULL    |       |



## Teams
| Field            | Type         | Null | Key | Default | Extra          |
|------------------|--------------|------|-----|---------|----------------|
| group_id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| leader_roll_no   | int(11)      | NO   |     | NULL    |                |
| title            | longtext     | NO   |     | NULL    |                |
| student2_roll_no | int(11)      | NO   |     | NULL    |                |
| student3_roll_no | int(11)      | YES  |     | NULL    |                |
| student4_roll_no | int(11)      | YES  |     | NULL    |                |
| email            | varchar(100) | NO   |     | NULL    |                |
| phone            | varchar(100) | NO   |     | NULL    |                |




