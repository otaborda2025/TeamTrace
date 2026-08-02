from fastapi import HTTPException

from app.jobsites.models import Jobsite
from app.jobsites.constants import GeofenceType
from app.core import security, utils


def get_jobsite(
    jobsite_id: int,
    company_id: int,
    db: Session
) -> Jobsite:
    return utils.get_object(
        db.query(Jobsite).filter(
            Jobsite.id == jobsite_id,
            Jobsite.company_id == company_id
        ),
        "Job site not found"
    )


#Create jobsite
def create_jobsite(
    jobsite_data: JobsiteCreate,
    current_user: User,
    db: Session

):
    existing_jobsite = (
        db.query(Jobsite)
        .filter(Jobsite.company_id == current_user.company_id, Jobsite.name==jobsite_data.name)
        .first()
    )

    if existing_jobsite:
        raise HTTPException(
            status_code=400,
            detail="A jobsite with this name already exists."
        )

    new_jobsite = Jobsite(
        company_id = current_user.company_id,
        name=jobsite_data.name,
        address = jobsite_data.address,
        latitude = jobsite_data.latitude,
        longitude = jobsite_data.longitude
    )

    db.add(new_jobsite)
    db.commit()
    db.refresh(new_jobsite)  
    return 
    
#Update jobsite
def update_jobsite(
    jobsite_id: int,
    jobsite_data: JobsiteUpdate,
    current_user: User,
    db: Session
):
    jobsite = get_jobsite(jobsite_id,current_user.company_id,db)

    if jobsite:
        if jobsite.name!=jobsite_data.name: 
            existing_jobsite = (
                db.query(Jobsite)
                .filter(Jobsite.company_id == current_user.company_id, Jobsite.name==jobsite_data.name)
                .first()
            )

            if existing_jobsite:
                raise HTTPException(
                    status_code=400,
                    detail="A jobsite with this name already exists."
                )

        update_data = jobsite_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(jobsite, field, value)

        db.commit()
        db.refresh(jobsite)

        return jobsite

#Delete jobsite
def delete_jobsite(
    jobsite_id: int,
    current_user: User,
    db: Session
):
    jobsite = get_jobsite(jobsite_id,current_user.company_id,db)

    db.delete(jobsite)
    db.commit()

    return {
        "message": "Jobsite deleted successfully."
    }  

#Get jobsites
def get_jobsites(
    skip: int,
    limit: int,
    current_user,
    db: Session
):
    return (
        db.query(Jobsite)
        .filter(Jobsite.company_id == current_user.company_id)
        .offset(skip)
        .limit(limit)
        .all()
    )      