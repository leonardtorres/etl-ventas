import argparse, pathlib
import pandas as pd
from src.transform import limpiar_ventas, total_por_producto
 
def main():
    p = argparse.ArgumentParser(description="ETL de ventas")
    p.add_argument("--input",  required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
 
    limpio  = limpiar_ventas(pd.read_csv(args.input))
    resumen = total_por_producto(limpio)
 
    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    limpio.to_csv(out, index=False)
    resumen.to_csv(out.with_name("resumen_" + out.name), index=False)
    print(f"Filas válidas: {len(limpio)} | Productos: {len(resumen)}")
 
if __name__ == "__main__":
    main()
