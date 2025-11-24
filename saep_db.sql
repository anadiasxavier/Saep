CREATE DATABASE IF NOT EXISTS saep_db;
USE saep_db;


--  usuários
CREATE TABLE USUARIO (
    ID_USUARIO INT PRIMARY KEY AUTO_INCREMENT,
    NOME VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(120) NOT NULL UNIQUE,
    SENHA VARCHAR(255) NOT NULL
);

-- tabela de produtos
CREATE TABLE PRODUTO (
    ID_PRODUTO INT PRIMARY KEY AUTO_INCREMENT,
    NOME_PRODUTO VARCHAR(120) NOT NULL,
    DESCRICAO TEXT,
    PRECO DECIMAL(10,2) NOT NULL,
    QUANTIDADE_ESTOQUE INT NOT NULL,
    ESTOQUE_MINIMO INT NOT NULL
);

--  movimentação de estoque
CREATE TABLE MOVIMENTACAO_ESTOQUE (
    ID_MOVIMENTACAO INT PRIMARY KEY AUTO_INCREMENT,
    ID_PRODUTO INT NOT NULL,
    ID_USUARIO INT NOT NULL,
    TIPO_MOVIMENTACAO ENUM('entrada', 'saida') NOT NULL,
    QUANTIDADE INT NOT NULL,
    DATA_MOVIMENTACAO DATE NOT NULL,
    
    FOREIGN KEY (ID_PRODUTO) REFERENCES PRODUTO(ID_PRODUTO),
    FOREIGN KEY (ID_USUARIO) REFERENCES USUARIO(ID_USUARIO)
);


--  usuários
INSERT INTO USUARIO (NOME, EMAIL, SENHA) VALUES
('João Silva', 'joao@email.com', '12345'),
('Maria Santos', 'maria@email.com', 'abcd123'),
('Carlos Souza', 'carlos@email.com', 'senha456'),
('Ana Pereira', 'ana@email.com', 'ana2025'),
('Ricardo Lima', 'ricardo@email.com', 'rl98765');

-- produtos
INSERT INTO PRODUTO (NOME_PRODUTO, DESCRICAO, PRECO, QUANTIDADE_ESTOQUE, ESTOQUE_MINIMO) VALUES
('Mouse USB', 'Mouse óptico com fio', 39.90, 50, 10),
('Teclado Mecânico', 'Teclado RGB switch blue', 249.90, 20, 5),
('Monitor 24"', 'Monitor Full HD LED', 899.00, 8, 2),
('Headset Gamer', 'Headset com microfone e som surround', 199.90, 15, 3),
('Webcam Full HD', 'Câmera USB 1080p para videoconferência', 149.50, 30, 8);

-- movimentações de estoque
INSERT INTO MOVIMENTACAO_ESTOQUE (ID_PRODUTO, ID_USUARIO, TIPO_MOVIMENTACAO, QUANTIDADE, DATA_MOVIMENTACAO) VALUES
(1, 1, 'entrada', 10, '2025-02-01'),
(2, 2, 'saida', 3, '2025-02-03'),
(3, 1, 'entrada', 5, '2025-02-05'),
(1, 3, 'saida', 7, '2025-02-06'),
(2, 1, 'entrada', 4, '2025-02-07'),
(3, 2, 'saida', 2, '2025-02-08'),
(4, 4, 'entrada', 12, '2025-02-10'),
(5, 5, 'saida', 6, '2025-02-11');
