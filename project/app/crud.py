# Rework this crud file to separate the controllers from the DB logic


# @user.get('/users', response_model=List[UserOut])
# async def get_users(db: Session = Depends(get_db)):
#     players = db.query(Users).all()
#     return players
#
#
# @user.get("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
# async def get_user(user_id: int, db: Session = Depends(get_db)):
#     data = db.query(Users).filter(Users.id == user_id).first()
#     if not data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'User with id of {user_id} is not available.')
#     return data
#
#
# @user.post('/users', response_model=User, status_code=status.HTTP_201_CREATED)
# async def create_user(user_request: User, db: Session = Depends(get_db)):
#     user = Users(name=user_request.name,
#                  email=user_request.email,
#                  password=user_request.password)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
#
#
# @user.put("/users/{user_id}", response_model=User, status_code=status.HTTP_202_ACCEPTED)
# async def update_user(user_id: int, user_request: User, db: Session = Depends(get_db)):
#     user = db.query(Users).filter(Users.id == user_id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'User with id of {user_id} is not available.')
#
#     user.update(user_request.dict())  # Why do I need to specify a dict here?
#     db.commit()
#     return user.first()
#
#
# @user.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(Users).filter(Users.id == user_id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'User with id of {user_id} is not available.')
#     user.delete()
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
