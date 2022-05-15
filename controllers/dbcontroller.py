
from threading import local
from databases import Database
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv("app/.env")


class DbController:
    dbuser = os.getenv('DB_USER')
    dbpassword = os.getenv('DB_PASSWORD')

    dbname = os.getenv('DB_NAME')
    database = Database(
        f"postgresql://{dbuser}:{dbpassword}@localhost:5432/{dbname}")

    async def read_all(self, query):
        # openconnection
        await self.database.connect()
        data = await self.database.fetch_all(query)
        # close connection and so on
        await self.database.disconnect()
        return data

    async def read_one(self, query):
        await self.database.connect()
        data = await self.database.fetch_one(query)

        return data

    async def create(self, query, values):
        await self.database.connect()
        data = await self.database.execute(query=query, values=values)
        await self.database.disconnect()
        return data

    async def update(self, query, values):
        await self.database.connect()
        data = await self.database.execute(query=query, values=values)
        await self.database.disconnect()
        return data

    async def delete(self, query):
        await self.database.connect()
        data = await self.database.execute(query)
        await self.database.disconnect()
        return data
