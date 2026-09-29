import os
import psycopg2
from psycopg2.extras import execute_batch

try:
    from db_config import DB_CONFIG
except ImportError:
    raise SystemExit(
        "请先复制 db_config.example.py 为 db_config.py，并填写自己的 PostgreSQL 参数。"
    )

# 瓦片目录结构：tiles/z/x/y.png
TILE_ROOT = r"./tiles"

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("SELECT current_database();")
print("当前数据库：", cur.fetchone()[0])

cur.execute("""
SELECT EXISTS (
    SELECT 1 FROM pg_tables
    WHERE schemaname = 'public' AND tablename = 'tiles'
);
""")

if not cur.fetchone()[0]:
    raise RuntimeError("未找到 public.tiles 表，请先执行 sql/schema.sql。")

records = []
count = 0

for z in os.listdir(TILE_ROOT):
    z_path = os.path.join(TILE_ROOT, z)
    if not os.path.isdir(z_path):
        continue

    try:
        z_level = int(z)
    except ValueError:
        continue

    for x in os.listdir(z_path):
        x_path = os.path.join(z_path, x)
        if not os.path.isdir(x_path):
            continue

        try:
            x_index = int(x)
        except ValueError:
            continue

        for filename in os.listdir(x_path):
            if not filename.lower().endswith(".png"):
                continue

            try:
                y_index = int(os.path.splitext(filename)[0])
            except ValueError:
                continue

            file_path = os.path.join(x_path, filename)

            with open(file_path, "rb") as f:
                tile_data = f.read()

            records.append(
                (z_level, x_index, y_index, filename, psycopg2.Binary(tile_data))
            )
            count += 1

            if len(records) >= 1000:
                execute_batch(
                    cur,
                    "INSERT INTO public.tiles "
                    "(z_level, x_index, y_index, tile_name, tile_data) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    records,
                    page_size=100,
                )
                conn.commit()
                print(f"已导入 {count} 张")
                records.clear()

if records:
    execute_batch(
        cur,
        "INSERT INTO public.tiles "
        "(z_level, x_index, y_index, tile_name, tile_data) "
        "VALUES (%s, %s, %s, %s, %s)",
        records,
        page_size=100,
    )
    conn.commit()

print(f"导入完成，共 {count} 张瓦片")

cur.close()
conn.close()
