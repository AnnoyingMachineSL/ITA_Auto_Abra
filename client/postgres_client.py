import time
import psycopg2
from models.postgres_models import UserModel
from utils.common_cheker import check_difference_between_objects


class PostgresClient:

    @staticmethod
    def get_instance(request: str):
        connection = psycopg2.connect(database='postgres',
                                      user='test_user',
                                      password='nQhrNsjoajEr',
                                      host='172.212.108.64',
                                      port=6502)  # Открытие bd

        cursor = connection.cursor()  # Обращение к bd
        cursor.execute(request)  # Передаем запрос в файл
        return cursor.fetchall()  # Возвращаем ответ

    def get_user(self, email: str, is_deleted: bool, is_verified: bool):
        request = 'select * from "user" u where email = ' + f"'{email}'"
        result = self.get_instance(request)
        assert len(result) == 1
        actual_model = UserModel(email=result[0][3], is_deleted=result[0][1], is_verified=result[0][0])
        expected_model = UserModel(email=email, is_deleted=is_deleted, is_verified=is_verified)
        check_difference_between_objects(actual_model, expected_model)
