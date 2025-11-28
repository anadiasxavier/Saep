
DROP DATABASE saep_db;
CREATE DATABASE saep_db;

USE saep_db;
SHOW TABLES;


INSERT INTO produto 
(NOME_PRODUTO, DESCRICAO, PRECO, QUANTIDADE_ESTOQUE, ESTOQUE_MINIMO) VALUES
('Mouse Gamer Redragon Cobra', 'Mouse gamer com RGB e 10000 DPI', 129.90, 25, 5),
('Teclado Mecânico RGB Husky', 'Teclado mecânico switch blue', 199.90, 18, 4),
('Headset HyperX Cloud Stinger', 'Headset gamer com microfone ajustável', 249.00, 12, 3),
('Monitor LG 24 polegadas', 'Monitor Full HD 75Hz', 799.00, 7, 2),
('Webcam Logitech C920', 'Webcam Full HD com microfone', 349.00, 10, 2),
('Cadeira Gamer MX5', 'Cadeira ergonômica com ajuste reclinável', 899.00, 5, 1),
('Notebook Lenovo i5', 'Notebook Intel i5, 8GB RAM e SSD 256GB', 2999.00, 6, 2),
('Mousepad Gamer Grande', 'Mousepad estendido 90cm antiderrapante', 49.90, 40, 10),
('Pen Drive 32GB Sandisk', 'Pen Drive USB 3.0 de alta velocidade', 29.90, 50, 15),
('HD Externo 1TB Seagate', 'HD externo portátil 1TB USB 3.0', 299.00, 9, 2),
('SSD Kingston 240GB', 'SSD interno SATA 2.5"', 189.00, 22, 6),
('Roteador TP-Link 300Mbps', 'Roteador Wi-Fi 2 antenas', 99.90, 15, 3),
('Caixa de Som JBL GO 3', 'Caixa de som portátil Bluetooth', 239.00, 20, 5),
('Fonte ATX 500W Corsair', 'Fonte 500W 80 Plus White', 289.90, 14, 3),
('Placa de Vídeo GTX 1650', 'Placa de vídeo Nvidia GTX 1650 4GB', 1299.00, 4, 1);

INSERT INTO movimentacao_estoque
 (TIPO_MOVIMENTACAO, QUANTIDADE, DATA_MOVIMENTACAO, ID_PRODUTO, ID_USUARIO)
 VALUES
 ('ENTRADA', 10, '2025-02-01', 1, 1),
 ('SAIDA', 3, '2025-02-02', 1, 1),

 ('ENTRADA', 5, '2025-02-03', 2, 1),
 ('SAIDA', 2, '2025-02-04', 2, 1),

 ('ENTRADA', 8, '2025-02-05', 3, 1),
 ('SAIDA', 1, '2025-02-06', 3, 1),

 ('SAIDA', 2, '2025-02-06', 4, 1),

 ('ENTRADA', 15, '2025-02-07', 8, 1),
 ('SAIDA', 5, '2025-02-07', 8, 1),

 ('SAIDA', 4, '2025-02-08', 9, 1),
 ('ENTRADA', 10, '2025-02-08', 9, 1),

 ('ENTRADA', 3, '2025-02-08', 10, 1),
 ('SAIDA', 1, '2025-02-09', 10, 1);
