
from fastapi import FastAPI
from app.controllers.dbcontroller import DbController
from app.models.users import User
users = FastAPI()

db = DbController()


# function for creatitng a user


@users.post("/users/create")
async def create_user(info: User):
    values = {"name": info.username,
              "email": info.email, "password": info.password}
    query = """INSERT INTO fuser(user_name, user_email,user_password) VALUES (:name,:email,:password)"""
    await db.create(query, values)
    return {'message': 'user created'}


# function for getting users


@users.get("/users/read")
async def read_users():
    query = """SELECT * FROM fuser"""
    data = await db.read_all(query)
    return data, {'message': 'all users'}

# getting one user


@users.get("/user/{user_key}")
async def read_user(user_key: int):
    if(user_key) == "":
        return {"message": "enter user id"}

    query = f"SELECT user_name, user_email, user_password FROM fuser WHERE user_id={user_key}"

    data = await db.read_one(query)
    return data, {"message": "user found"}


# update


@users.put("/users/update/{user_key}")
async def update_user(user: User, user_key: int):
    values = {"name": user.username,
              "email": user.email, "password": user.password}
    query = """UPDATE fuser SET user_name= :name, user_email = :email, user_password = :password WHERE user_id = :user_key"""
    await db.update(query, values)
    return {"message": "user updated"}


# function to delete user


@users.delete("/users/delete/{user_key}")
async def delete_user(user_key: int):
    query = f"DELETE FROM fuser WHERE user_id = {user_key}"
    data = await db.delete(query)
    return {"message": "user deleted"}
