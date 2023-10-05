import mysql.connector
from faker import Faker
from random import choice
from datetime import date
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


def gerar_dados_profissionais():
    for i in range(500):

        # Gerar ID
        id_pro_nums = [random.randint(0, 9) for i in range(7)]
        id_profissional = int(''.join(str(n) for n in id_pro_nums))

        # Pegar CPF da tabela 'personal_data'
        pegar_cpf()
        cpf = choice(CPFS)

        # Gerar emprego atual
        emprego = fake.job()

        # Gerar salário atual
        salario = fake.random_int(min=1000, max=50000)

        # Data atual
        data_atual = date.today()

        # Gerar data de ingresso no emprego
        data_ingresso = fake.date_between(start_date="-20y", end_date="today")

        # Gerar anos de experiência na área
        minimo = (data_atual - data_ingresso).days / 365
        anos_experiencia = round(random.uniform(minimo, minimo + 10))

        cursor.execute(f"INSERT INTO profissional VALUES ({id_profissional}, {cpf}, '{emprego}', '{data_ingresso}',"
                       f"{salario}, {anos_experiencia})")
        db.commit()


gerar_dados_profissionais()
cursor.close()
db.close()
