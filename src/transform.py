import pandas as pd
 
def limpiar_ventas(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza columnas, elimina nulos, duplicados y montos inválidos."""
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.dropna(subset=["producto", "monto"])
    df = df.drop_duplicates()
    df["monto"] = df["monto"].astype(float)
    return df[df["monto"] > 0]
 
def total_por_producto(df: pd.DataFrame) -> pd.DataFrame:
    return (df.groupby("producto", as_index=False)["monto"]
              .sum()
              .rename(columns={"monto": "total"}))
 