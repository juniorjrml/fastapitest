from fastapi import FastAPI


app = FastAPI()

@app.api_route("/user", methods=["GET", "POST", "PUT", "DELETE"])
def user(user_name: str):
    pass