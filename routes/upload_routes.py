from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from services.data_services import save_data

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV allowed")

    try:
        df = pd.read_csv(file.file)

        df = df.drop_duplicates()
        df = df.dropna(how="all")

        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].mean())
            else:
                df[col] = df[col].fillna("unknown")

        df = df.replace([float("inf"), -float("inf")], 0)
        df = df.fillna(0)

        save_data(df)

        return {"msg": "Uploaded successfully", "rows": len(df)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))