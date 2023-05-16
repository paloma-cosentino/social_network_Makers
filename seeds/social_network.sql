-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name TEXT,
    user_account TEXT,
    user_post TEXT
);
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title TEXT,
    post_content TEXT,
    post_read TEXT,
    post_viewed INTEGER,

    -- The foreign key name is always {other_table_singular}_id
    post_id int,
    constraint fk_post foreign key(post_id)
        references posts(id)
        on delete cascade
);


INSERT INTO users (user_account, user_name, user_post) VALUES ('henry@email', 'henry', 'hello world');
INSERT INTO posts (post_title, post_content, post_read, post_viewed
) VALUES ('Monday', 'hello world', 'emily', 5);