from fastapi import APIRouter, Depends, status #, HTTPException, status

from app.auth.dependencies import  require_role
from app.database.session import get_db 
from app.jobsites import service as jobsites_service
from app.jobsites.schemas import JobsiteCreate, JobsiteResponse, JobsiteUpdate
from app.users.constants import UserRole


router=APIRouter(
    prefix="/jobsites",
    tags=["Jobsites"]
)


#Create a jobsite
@router.post(
    "/create",
    response_model=JobsiteResponse
)    
def create_jobsite(
    jobsite_data: JobsiteCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return jobsites_service.create_jobsite(jobsite_data, current_user, db)

#Update Jobsite
@router.put(
    "/{jobsite_id}",
    response_model=JobsiteResponse
)
def update_jobsite(
    jobsite_id: int,
    jobsite_data: JobsiteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.OWNER, UserRole.ADMIN])
    )
):
    return jobsites_service.update_jobsite(jobsite_id,jobsite_data,current_user,db)

#Delete jobsite
@router.delete(
    "/{jobsite_id}"
)
def delete_jobsite(
    jobsite_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.OWNER, UserRole.ADMIN])
    )
):
    return jobsites_service.delete_jobsite(jobsite_id, current_user, db )
    

#List jobsites
@router.get(
    "/",
    response_model=list[JobsiteResponse]
)    
def get_jobsites(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user=Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return jobsites_service.get_jobsites(skip, limit, current_user, db)
