import sqlite3
from config import DB_PATH

def mostrar_respuestas(tipo=None, resultado=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT id, tipo, categoria_usuario, resultado, substr(contenido_generado, 1, 100) || '...' as preview, fecha FROM respuestas_exitosas"
    filtros = []

    if tipo:
        query += " WHERE tipo=?"
        filtros.append(tipo)

        if resultado:
            query += " AND resultado=?"
            filtros.append(resultado)
    elif resultado:
        query += " WHERE resultado=?"
        filtros.append(resultado)

    query += " ORDER BY fecha DESC"

    cursor.execute(query, filtros)
    rows = cursor.fetchall()
    conn.close()

    print(f"{'ID':<4} {'Tipo':<10} {'Cat. Usuario':<12} {'Resultado':<15} {'Vista previa':<60} {'Fecha'}")
    print("-" * 110)
    for row in rows:
        print(f"{row[0]:<4} {row[1]:<10} {row[2]:<12} {row[3]:<15} {row[4]:<60} {row[5]}")

# Ejecución desde terminal
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Explorar respuestas exitosas guardadas")
    parser.add_argument("--tipo", help="Tipo de respuesta: ppv, engagement, welcome...")
    parser.add_argument("--resultado", help="Resultado esperado: venta_exitosa, respuesta_alta...")

    args = parser.parse_args()
    mostrar_respuestas(tipo=args.tipo, resultado=args.resultado)
