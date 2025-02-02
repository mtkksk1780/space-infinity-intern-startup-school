-- Drop schema
DROP SCHEMA IF EXISTS app CASCADE;

-- Truncate tables
-- TRUNCATE TABLE app.Feedback, app.Submission, app.Project, app.User CASCADE;

-- Drop tables
-- DROP TABLE IF EXISTS app.Feedback CASCADE;
-- DROP TABLE IF EXISTS app.Submission CASCADE;
-- DROP TABLE IF EXISTS app.Project CASCADE;
-- DROP TABLE IF EXISTS app.User CASCADE;

-- Create schema
CREATE SCHEMA IF NOT EXISTS app;

-- Activate extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create User table
CREATE TABLE app.User (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  password TEXT,
  name TEXT,
  role TEXT NOT NULL
);

-- Create Project table
CREATE TABLE app.Project (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  one_liner TEXT NOT NULL,
  description TEXT NOT NULL,
  register_date TIMESTAMP DEFAULT NOW(),
  user_id UUID NOT NULL,
  CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES app.User (id) ON DELETE CASCADE
);

-- Create Submission table
CREATE TABLE app.Submission (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  project_id UUID NOT NULL,
  week INT NOT NULL,
  progress_rate INT,
  progress_comment TEXT,
  output_url TEXT,
  is_active_week BOOLEAN NOT NULL,
  submission_status TEXT NOT NULL,
  CONSTRAINT fk_project FOREIGN KEY (project_id) REFERENCES app.Project (id) ON DELETE CASCADE
);

-- Create Feedback table
CREATE TABLE app.Feedback (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  submission_id UUID NOT NULL,
  user_id UUID NOT NULL,
  evaluation_rate INT NOT NULL,
  evaluation_comment TEXT NOT NULL,
  is_anonymous BOOLEAN NOT NULL,
  CONSTRAINT fk_submission FOREIGN KEY (submission_id) REFERENCES app.Submission (id) ON DELETE CASCADE,
  CONSTRAINT fk_user_feedback FOREIGN KEY (user_id) REFERENCES app.User (id) ON DELETE CASCADE
);

-- Insert data into User table
INSERT INTO app.User (id, email, password, name, role) VALUES
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'a', 'a', 'Admin', 'Admin'),
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 'b', 'b', 'Intern', 'Member'),
('cccccccc-cccc-cccc-cccc-cccccccccccc', 'c', 'c', 'Feedback user', 'Member');

-- Insert data into Project table
INSERT INTO app.Project (id, name, one_liner, description, user_id) VALUES
(uuid_generate_v4(), 'Making new songs', 'Making next global hits', 'Making next global hits worldwide', (SELECT id FROM app.User WHERE email='a'));

-- Insert data into Submission table
INSERT INTO app.Submission (id, project_id, week, progress_rate, progress_comment, output_url, is_active_week, submission_status) VALUES
(uuid_generate_v4(), (SELECT id FROM app.Project WHERE name='Making new songs'), 1, 5, 'I have made the beat', 'https://www.youtube.com/watch?v=9bZkp7q19f0', TRUE, 'Working'),
(uuid_generate_v4(), (SELECT id FROM app.Project WHERE name='Making new songs'), 2, 8, 'I have written the lyrics', 'https://www.youtube.com/watch?v=9bZkp7q19f0', FALSE, 'Pending'),
(uuid_generate_v4(), (SELECT id FROM app.Project WHERE name='Making new songs'), 3, 9, 'I have recorded the song', 'https://www.youtube.com/watch?v=9bZkp7q19f0', FALSE, 'Pending'),
(uuid_generate_v4(), (SELECT id FROM app.Project WHERE name='Making new songs'), 4, 10, 'I have mixed the song', 'https://www.youtube.com/watch?v=9bZkp7q19f0', FALSE, 'Pending');

-- Insert data into Feedback table
INSERT INTO app.Feedback (submission_id, user_id, evaluation_rate, evaluation_comment, is_anonymous) 
VALUES
((SELECT id FROM app.Submission WHERE project_id = (SELECT id FROM app.Project WHERE name='Making new songs') AND week = 1), 
(SELECT id FROM app.User WHERE email='c'), 5, 'Sounds very cool! But I think you should make the sound quality a bit better, its hard to listen to with the other noise. Keep up the good work!', FALSE),
((SELECT id FROM app.Submission WHERE project_id = (SELECT id FROM app.Project WHERE name='Making new songs') AND week = 2), 
(SELECT id FROM app.User WHERE email='c'), 1, 'I dont like it', FALSE),
((SELECT id FROM app.Submission WHERE project_id = (SELECT id FROM app.Project WHERE name='Making new songs') AND week = 3), 
(SELECT id FROM app.User WHERE email='c'), 4, 'Good job! I like it:)', TRUE),
((SELECT id FROM app.Submission WHERE project_id = (SELECT id FROM app.Project WHERE name='Making new songs') AND week = 4), 
(SELECT id FROM app.User WHERE email='c'), 3, 'This is really impressive, however for me, it was too plain. I would love to hear the base sound more.', FALSE),
((SELECT id FROM app.Submission WHERE project_id = (SELECT id FROM app.Project WHERE name='Making new songs') AND week = 1), 
(SELECT id FROM app.User WHERE email='c'), 5, 'Excellent job', TRUE);