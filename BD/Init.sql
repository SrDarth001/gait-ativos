CREATE DATABASE IF NOT EXISTS gait;
USE gait;

CREATE TABLE IF NOT EXISTS ativos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipamento VARCHAR(255) NOT NULL,
    horas_uso INT NOT NULL,
    destino_recomendado VARCHAR(100) NOT NULL
);

INSERT INTO ativos (equipamento, horas_uso, destino_recomendado) VALUES
('Servidor GPU NVIDIA H100 - SN001', 12000, 'Reaproveitar (Realocar)'),
('Storage NVMe Array - SN042', 32500, 'Sanitizar e Descartar');
