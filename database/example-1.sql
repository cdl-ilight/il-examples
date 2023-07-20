-- You can assume there is a table for users called il_users
-- You can also assume there is a table for groups called il_groups

CREATE TABLE IF NOT EXISTS il_files (
    id            integer NOT NULL PRIMARY KEY,
    userid        integer NOT NULL,
    groupid       integer NOT NULL,
    description   text NOT NULL,
    filename      text NOT NULL,
    filepath      text,
    date_created  real,
    last_modified real,
    md5sum        text,
    size          integer,
    st_mode       integer,
);

CREATE TABLE IF NOT EXISTS il_datasets (
    id             integer NOT NULL PRIMARY KEY,
    userid         integer NOT NULL,
    groupid        integer NOT NULL,
    date_created   real NOT NULL,
    last_modified  real NOT NULL,
    name           text NOT NULL,
    description    text NOT NULL,
);

CREATE TABLE IF NOT EXISTS il_dataset_files (
    datasetid      integer NOT NULL,
    fileid         integer NOT NULL,
    timestep       integer NOT NULL,
    timevalue      real NOT NULL,
    PRIMARY KEY (datasetid, fileid)
);
