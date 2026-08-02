from fastapi import HTTPException
from app.users.models import User
from app.users.constants import UserRole
from app.core import security, utils


def get_user(
    user_id: int,
    company_id: int,
    db: Session
) -> User:
    return utils.get_object(
        db.query(User).filter(
            User.id == user_id,
            User.company_id == company_id
        ),
        "User not found"
    )


#Register user
def register_user(
    user_data: UserCreate,
    current_user: User,
    db: Session

):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = security.get_password_hash(
        user_data.password
    )

    new_user = User(
        company_id = current_user.company_id,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password_hash=hashed_password,
        role=UserRole.EMPLOYEE,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)  
    return new_user


#Get users
def get_users(
    skip: int,
    limit: int,
    current_user,
    db: Session
):
    return (
        db.query(User)
        .filter(User.company_id == current_user.company_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

#Update user
def update_user(
    user_id: int,
    user_data: UserUpdate,
    current_user,
    db: Session

):
    existing_user = get_user(user_id, current_user.company_id, db)

    updates = user_data.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(existing_user, field, value)

    db.commit()
    db.refresh(existing_user)

    return existing_user


#Delete user
def delete_user(
    user_id: int,
    current_user: User,
    db: Session
):
    user = get_user(user_id, current_user.company_id, db)

    if user.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot delete your own account."
    )    

    if user.role == UserRole.OWNER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The company owner cannot be deleted."
    )


    db.delete(user)
    db.commit()


#Deactivate user
def deactivate_user(
    user_id: int,
    current_user: User,
    db: Session
):
    user = get_user(user_id, current_user.company_id, db)

    if user.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot deactivate your own account."
    )    

    if user.role == UserRole.OWNER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The company owner cannot be deactivate."
    )

    user.is_active = False

    db.commit()
    db.refresh(user)

    return user


#Activate user
def activate_user(
    user_id: int,
    current_user: User,
    db: Session
):
    user = get_user(user_id, current_user.company_id, db)

    user.is_active = True

    db.commit()
    db.refresh(user)

    return user


#Update user role
def update_user_role(
    user_id: int,
    new_role: UserRole,
    current_user: User,
    db: Session
):
    user = (user_id, current_user.company_id, db)

    if user.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot update role for your own account."
    )    

    user.role = new_role

    db.commit()
    db.refresh(user)

    return user