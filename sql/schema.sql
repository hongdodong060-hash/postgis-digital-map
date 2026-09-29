-- 数字地图五级瓦片数据库表
-- PostgreSQL / PostGIS

CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS public.tiles (
    id BIGSERIAL PRIMARY KEY,
    z_level INTEGER NOT NULL,
    x_index INTEGER NOT NULL,
    y_index INTEGER NOT NULL,
    tile_name TEXT NOT NULL,
    tile_data BYTEA NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_tiles_zxy
ON public.tiles (z_level, x_index, y_index);
