# 环境配置

## PostgreSQL / PostGIS

项目使用 PostgreSQL 管理瓦片数据，并可启用 PostGIS 扩展。

## Python

```bash
python -m venv .venv
pip install -r requirements.txt
```

## 数据

Python 程序默认读取：

```text
tiles/{z}/{x}/{y}.png
```

并将 PNG 瓦片二进制数据批量写入 `public.tiles`。

真实数据库账号、密码和本地路径不要提交到 GitHub。
