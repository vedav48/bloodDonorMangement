CREATE DATABASE library_db;
USE library_db;
CREATE TABLE book (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    publisher VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT);