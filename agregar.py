#---Tomando en cuenta la siguiente carga---

pq = pl.read_parquet("pq.parquet")
# --- Crear columna Inicio_viaje ---
if "Fecha_Retiro" in pq.columns and "Hora_Retiro" in pq.columns:
    pq = pq.with_columns(
        pl.concat_str([
            pl.col("Fecha_Retiro").cast(pl.Utf8).str.strip_chars(),
            pl.lit(" "),
            pl.col("Hora_Retiro").cast(pl.Utf8).str.strip_chars()
        ])
        .str.strptime(pl.Datetime, format="%d/%m/%Y %H:%M:%S", strict=False)
        .alias("Inicio_viaje")
    )

# --- Crear columna Fin_viaje ---
if "Fecha_Arribo" in pq.columns and "Hora_Arribo" in pq.columns:
    pq = pq.with_columns(
        pl.concat_str([
            pl.col("Fecha_Arribo").cast(pl.Utf8).str.strip_chars(),
            pl.lit(" "),
            pl.col("Hora_Arribo").cast(pl.Utf8).str.strip_chars()
        ])
        .str.strptime(pl.Datetime, format="%d/%m/%Y %H:%M:%S", strict=False)
        .alias("Fin_viaje")
    )

print("Procesado correctamente con Polars")
