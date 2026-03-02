@app.get("/items", response_model=List[schemas.ItemResponse])
def get_items(
    search: Optional[str] = Query(None, description="Search by title"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(models.Item)

    #  Search by title substring
    if search:
        query = query.filter(models.Item.title.ilike(f"%{search}%"))

    #  Pagination
    items = query.offset(offset).limit(limit).all()

    return items