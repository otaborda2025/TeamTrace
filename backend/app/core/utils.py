from fastapi import HTTPException, status

def get_object(query, detail: str = "Resource not found"):
    obj = query.first()

    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

    return obj