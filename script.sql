CREATE DATABASE Y0urD4t4B3s3;

USE Y0urD4t4B3s3;

CREATE TABLE dados_pessoais (
    CPF INT NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    sobrenome VARCHAR(50) NOT NULL,
    sexo ENUM('M', 'F') NOT NULL,
    ano_nascimento DATE NOT NULL,
    estado_civil ENUM('casado','solteiro','viuvo','divorciado','casada','solteira','viuva','divorciada') NOT NULL,
    qtd_filhos INT NOT NULL,
    escolaridade ENUM('superior','medio','fundamental') NOT NULL,
    email VARCHAR(50),
    telefone VARCHAR(50)
);

CREATE TABLE profissional (
    id_profissional INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    CPF INT NOT NULL,
    emprego_atual VARCHAR(50) NOT NULL,
    data_ingresso_emprego_atual DATE NOT NULL,
    salario_em_reais INT NOT NULL,
    anos_experiencia_na_area INT NOT NULL,
    FOREIGN KEY (CPF) REFERENCES dados_pessoais(CPF)
);

CREATE TABLE localizacao (
    id_localizacao INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    CPF INT NOT NULL,
    CEP INT NOT NULL,
    numero_residencia INT,
    rua VARCHAR(50) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    FOREIGN KEY (CPF) REFERENCES dados_pessoais(CPF)
);