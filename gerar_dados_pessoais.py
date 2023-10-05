import mysql.connector
from faker import Faker
from random import choice
import random


def gerar_dados_pessoais():
    for i in range(500):
        fake = Faker('pt_BR')

        # Gerando CPF fictício (apenas números)
        nums = [random.randint(0, 9) for i in range(9)]
        nums_cpf = [str(n) for n in nums]

        # Gerando nome e sobrenome
        nome_completo = fake.name()
        partes_nome = nome_completo.split()

        # Gerar sexo
        sexos = ['M', 'F']

        # Gerar data de nascimento
        data_nascimento = fake.date_of_birth(minimum_age=25, maximum_age=70)

        # Gerar escolaridade
        esclrd = ['superior', 'medio', 'fundamental']

        cpf = ''.join(nums_cpf)
        cpf = int(cpf)
        nome = partes_nome[0]
        sobrenome = partes_nome[1]
        sexo = choice(sexos)
        nascimento = data_nascimento
        qtd_filhos = random.randint(0, 5)
        escolaridade = choice(esclrd)
        email = fake.email()
        telefone = fake.phone_number()

        # Gerar estado civíl
        est_cvl = ['casado', 'solteiro', 'viuvo', 'divorciado', 'casada', 'solteira', 'viuva', 'divorciada']
        if sexo == 'M':
            est_cvl = ['casado', 'solteiro', 'viuvo', 'divorciado']
        elif sexo == 'F':
            est_cvl = ['casada', 'solteira', 'viuva', 'divorciada']

        estado_civil = choice(est_cvl)

        db = mysql.connector.connect(
            host="localhost",
            user="Y0urUs3rn4m3",
            port=3306,
            password="Y0urP455w0rd",
            database="Y0urD4t4B3s3"
        )

        cursor = db.cursor()
        cursor.execute(f"INSERT INTO dados_pessoais VALUES ({cpf}, '{nome}', '{sobrenome}', '{sexo}',"
                       f"'{data_nascimento}', '{estado_civil}', {qtd_filhos}, '{escolaridade}',"
                       f"'{email}', '{telefone}')")

        db.commit()
        cursor.close()
        db.close()


gerar_dados_pessoais()
