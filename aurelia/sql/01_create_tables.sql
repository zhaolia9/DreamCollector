CREATE DATABASE IF NOT EXISTS aurelia;
USE aurelia;

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE Dreams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    date DATE NOT NULL,
    mood VARCHAR(50),
    vividness INT,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

CREATE TABLE Symbols (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE DreamSymbols (
    dream_id INT NOT NULL,
    symbol_id INT NOT NULL,
    PRIMARY KEY (dream_id, symbol_id),
    FOREIGN KEY (dream_id) REFERENCES Dreams(id) ON DELETE CASCADE,
    FOREIGN KEY (symbol_id) REFERENCES Symbols(id) ON DELETE CASCADE
);

CREATE TABLE Poems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author_id INT NOT NULL,
    dream_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Users(id),
    FOREIGN KEY (dream_id) REFERENCES Dreams(id) ON DELETE CASCADE
);
