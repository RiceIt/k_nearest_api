from sqlalchemy.orm import Session

import models
import schemas


def get_user(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_k_nearest(user: models.User, k: int, radius: float, db: Session):
    rows = db.execute("SELECT * FROM users WHERE coord <-> :coord < :radius AND users.id != :user_id "
                      "ORDER BY coord <-> :coord LIMIT :limit",
                      {'coord': user.coord, 'user_id': user.id, 'limit': k, 'radius': radius})
    return list(rows)
