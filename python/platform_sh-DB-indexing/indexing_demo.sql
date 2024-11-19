-- Create table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    age INT,
    bio TEXT
);

-- Populate `users` table
INSERT INTO users (name, email, age, bio) VALUES
('Alice Johnson', 'alice.johnson@example.com', 28, 'Alice loves hiking, reading, and exploring data science.'),
('Bob Smith', 'bob.smith@example.com', 35, 'Bob is a software engineer with a passion for AI.'),
('Charlie Brown', 'charlie.brown@example.com', 22, 'Charlie is a student interested in machine learning.'),
('Diana Prince', 'diana.prince@example.com', 31, 'Diana works in cybersecurity and enjoys running.'),
('Ethan Hunt', 'ethan.hunt@example.com', 40, 'Ethan is an adventure seeker and works as a field agent.'),
('Fiona Apple', 'fiona.apple@example.com', 29, 'Fiona is a musician who loves composing songs.'),
('George Miller', 'george.miller@example.com', 25, 'George is a movie enthusiast who reviews films.'),
('Hannah Montana', 'hannah.montana@example.com', 27, 'Hannah is a singer and songwriter with a global fanbase.'),
('Ian Wright', 'ian.wright@example.com', 33, 'Ian enjoys writing technical blogs and traveling.'),
('Jane Doe', 'jane.doe@example.com', 30, 'Jane is a data analyst exploring new analytics tools.'),
('Kyle Reese', 'kyle.reese@example.com', 37, 'Kyle is a fitness coach and amateur photographer.'),
('Laura Croft', 'laura.croft@example.com', 29, 'Laura loves archaeology and discovering ancient history.'),
('Michael Scott', 'michael.scott@example.com', 45, 'Michael is a manager at a paper company.'),
('Nancy Drew', 'nancy.drew@example.com', 24, 'Nancy is a detective who enjoys solving mysteries.'),
('Oliver Twist', 'oliver.twist@example.com', 21, 'Oliver is a student learning about literature and drama.'),
('Pam Beesly', 'pam.beesly@example.com', 31, 'Pam is an artist and office administrator.'),
('Quentin Blake', 'quentin.blake@example.com', 50, 'Quentin is a renowned illustrator and author.'),
('Rachel Green', 'rachel.green@example.com', 34, 'Rachel works in fashion and loves shopping.'),
('Steve Rogers', 'steve.rogers@example.com', 100, 'Steve is a veteran who enjoys history and classic films.'),
('Tina Fey', 'tina.fey@example.com', 43, 'Tina is a comedian and scriptwriter. A true creative mind.');

--------------------------------------------------------------------------
-- B-Tree Index and its queries

-- Create B-Tree index on the `age` field.
CREATE INDEX idx_age ON users(age);

-- Range query on `age` field.
SELECT * FROM users WHERE age BETWEEN 25 AND 35;

--------------------------------------------------------------------------
-- Hash Index and its queries (PostgreSQL)

-- Create Hash index on the `email` field.
CREATE INDEX idx_email_hash ON users USING hash(email);

-- Search query on the `email` field.
SELECT * FROM users WHERE email = 'jane.doe@example.com';

--------------------------------------------------------------------------
-- Full-Text Index and its queries

-- PostgreSQL: Create Index
CREATE INDEX idx_bio_fulltext ON users USING GIN (to_tsvector('english', bio));

-- MySQL: Create Index
CREATE FULLTEXT INDEX idx_bio_fulltext ON users(bio);

-- Full Text search without index
SELECT * FROM users WHERE bio LIKE '%films%';

-- PostgreSQL: Full-Text search with Index
SELECT * FROM users WHERE to_tsvector('english', bio) @@ to_tsquery('films');

-- MySQL: Full-Text search with Index
SELECT * FROM users WHERE MATCH(bio) AGAINST ('films' IN NATURAL LANGUAGE MODE);

--------------------------------------------------------------------------
