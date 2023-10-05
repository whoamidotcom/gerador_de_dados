import mysql.connector
from faker import Faker
from random import choice
import random


CPFS = []
fake = Faker('pt_BR')
db = mysql.connector.connect(
        host="localhost",
        user="Y0urUs3rn4m3",
        port=3306,
        password="Y0urP455w0rd",
        database="Y0urD4t4B3s3"
    )
cursor = db.cursor()


def pegar_cpf():
    cursor.execute("SELECT CPF FROM dados_pessoais")
    resultados = cursor.fetchall()

    for resultado in resultados:
        CPFS.append(resultado[0])


def gerar_localizacao():
    for i in range(500):

        # Gerar CEP fictício
        cep = [random.randint(0, 9) for i in range(7)]
        cep_nums = ''.join(str(c) for c in cep)
        cep = int(cep_nums)

        # Gerar número de residência
        num_res = [random.randint(0, 9) for i in range(7)]
        numero_residencia = ''.join(str(c) for c in num_res)

        # Gerar rua aleatória
        rua = fake.street_name()

        # Gerar bairro
        bairro = fake.neighborhood()

        # Gerar cidade
        cidade = fake.city()

        # Gerar estado
        estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI',
                   'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
        estado = choice(estados)

        # Pegar CPF da tabela 'personal_data'
        pegar_cpf()
        cpf = choice(CPFS)

        # Gerar ID
        id_loc_nums = [random.randint(0, 9) for i in range(7)]
        id_localizacao = int(''.join(str(n) for n in id_loc_nums))

        cursor.execute(f"INSERT INTO localizacao VALUES ({id_localizacao}, {cpf}, {cep}, '{numero_residencia}',"
                       f"'{rua}', '{bairro}', '{cidade}', '{estado}')")

        db.commit()


gerar_localizacao()
cursor.close()
db.close()
