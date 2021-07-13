CREATE DATABASE IF NOT EXISTS weather;

CREATE TABLE info ( 
    id INT,
    main VARCHAR(255) default NULL,
    description VARCHAR(255) default NULL,
    icon VARCHAR(255) default NULL
);
