import pandas as pd
from src.transform import limpiar_ventas, total_por_producto
 
def _df_demo():
    return pd.DataFrame({
        "Producto": ["A", "A", None, "B"],
        "Monto":    [10.0, 10.0, 5.0, -3.0],
    })
 
def test_elimina_nulos_duplicados_y_negativos():
    out = limpiar_ventas(_df_demo())
    assert out["producto"].notna().all()
    assert (out["monto"] > 0).all()
    assert len(out) == 1            # solo sobrevive (A, 10.0)
 
def test_total_por_producto():
    tot = total_por_producto(limpiar_ventas(_df_demo()))
    assert tot.loc[tot.producto == "A", "total"].iloc[0] == 10.0
