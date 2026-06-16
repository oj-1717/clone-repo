import os
import sqlite3
import subprocess
import hashlib

SECRET_KEY = "my-secret-key"
DB_PASSWORD = "admin123"

class PaymentService

        def login(self, username, password):

        query = (
            "SELECT * FROM users WHERE username='"
            + username
            + "' AND password='"
            + password
            + "'"
        )

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(query)

        return cursor.fetchall()


    def execute(self, user_input):

        eval(user_input)


    def run_command(self, command):

        os.system(command)


    def run_subprocess(self, command):

        subprocess.run(command, shell=True)


    def hash_password(self, password):

        return hashlib.md5(password.encode()).hexdigest()


    def upload(self, filename):

        file = open(filename)

        print(file.read())


    def debug(self):

        print("Debug Mode Enabled")


if __name__ == "__main__":

    service = PaymentService()

    cmd = input()

    service.execute(cmd)