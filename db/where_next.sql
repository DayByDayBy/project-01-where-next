-- DROP TABLE cities;
-- DROP TABLE countries;
-- DROP TABLE users;

-- CREATE TABLE users (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(255),
--   bio VARCHAR(255)
-- );

-- CREATE TABLE countries (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(255), 
--   language VARCHAR(255)
--   currency VARCHAR(255)
-- );

-- CREATE TABLE cities(
--   id SERIAL PRIMARY KEY,
--   country_id INT REFERENCES country(id) ON DELETE CASCADE
-- );