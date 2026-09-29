# 数字地图编制与五级地图瓦片制作

## 项目简介

本项目为地理信息科学专业数字地图编制综合实践，围绕空间数据处理、数字地图表达、多级地图瓦片制作与空间数据库管理开展。

项目将数字地图按照地图缩放级别组织为 **5 个级别的 PNG 地图瓦片**，并使用 PostgreSQL/PostGIS 对瓦片数据进行管理，同时提供 Leaflet 本地预览方式。

## 核心成果

- 数字地图编制
- 5 级地图瓦片制作
- XYZ 瓦片目录组织
- PNG 瓦片读取与批量入库
- PostgreSQL / PostGIS 数据库管理
- Leaflet 地图瓦片预览

## 五级瓦片组织方式

```text
tiles/
├── 1/
├── 2/
├── 3/
├── 4/
└── 5/
```

实际瓦片数量较多时，本仓库不提交全部 PNG 文件，主要通过项目截图展示五个级别的成果。

## 数据库设计

瓦片可以存储在 PostgreSQL/PostGIS 的 `public.tiles` 表中：

| 字段 | 类型 | 说明 |
|---|---|---|
| id | BIGSERIAL | 主键 |
| z_level | INTEGER | 瓦片级别 |
| x_index | INTEGER | X 索引 |
| y_index | INTEGER | Y 索引 |
| tile_name | TEXT | 瓦片文件名 |
| tile_data | BYTEA | PNG 瓦片二进制数据 |

建表 SQL：`sql/schema.sql`

## Python 瓦片入库

`python/import_tiles.py` 用于连接 PostgreSQL，按 `z/x/y.png` 目录结构读取 PNG 瓦片，并批量写入 `public.tiles`。

数据库连接参数使用占位符，不包含个人密码。

## Leaflet 本地预览

预览模板：

`tiles/leaflet-preview.html`

## 项目截图

请将实际成果截图放入 `screenshots/`。

建议文件名：

```text
01_数字地图.png
02_第1级瓦片.png
03_第2级瓦片.png
04_第3级瓦片.png
05_第4级瓦片.png
06_第5级瓦片.png
```

## 技术栈

- PostgreSQL
- PostGIS
- Python
- psycopg2
- Leaflet
- PNG Map Tiles
- GIS 数字地图编制

## 项目流程

```text
空间数据处理
    ↓
数字地图编制
    ↓
地图瓦片切分
    ↓
5级瓦片组织
    ↓
PNG 瓦片
    ↓
PostgreSQL / PostGIS 管理
    ↓
Leaflet 地图预览
```

## 运行说明

1. 执行 `sql/schema.sql`
2. 安装依赖：`pip install -r requirements.txt`
3. 将 `python/db_config.example.py` 复制为 `python/db_config.py`
4. 填写自己的 PostgreSQL 参数
5. 运行 `python python/import_tiles.py`

## 数据说明

完整原始空间数据和大量瓦片文件未随仓库提交。GitHub 主要用于展示项目代码、数据库结构、处理流程和成果截图。

## 项目定位

本项目主要体现 GIS 数字地图编制、多级地图瓦片制作、空间数据库管理、Python 数据处理和 Web 地图瓦片组织能力。
