#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动生成 sitemap.xml
扫描 article/ 目录下所有文章页，自动重建完整站点地图。
用法：python3 scripts/gen_sitemap.py
"""
import os
import re
import glob
from datetime import datetime

BASE_URL = "https://xn--hlr9m.xn--fiqs8s"
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLE_DIR = os.path.join(SITE_ROOT, "article")
SITEMAP_PATH = os.path.join(SITE_ROOT, "sitemap.xml")

# 排除的文件（非文章页）
EXCLUDE = {"index.html", "article-template.html"}


def extract_date(html_path):
    """从文章 HTML 中提取 JSON-LD 的 datePublished，失败则用文件修改日期"""
    try:
        with open(html_path, encoding="utf-8") as f:
            content = f.read()
        m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"', content)
        if m:
            return m.group(1)
    except Exception:
        pass
    ts = os.path.getmtime(html_path)
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def extract_title(html_path):
    """提取文章标题（用于日志输出）"""
    try:
        with open(html_path, encoding="utf-8") as f:
            content = f.read()
        m = re.search(r"<title>([^<]+)</title>", content)
        if m:
            return m.group(1).split(" - ")[0].strip()
    except Exception:
        pass
    return os.path.basename(html_path)


def main():
    # 收集文章
    articles = []
    for f in sorted(glob.glob(os.path.join(ARTICLE_DIR, "*.html"))):
        name = os.path.basename(f)
        if name in EXCLUDE:
            continue
        articles.append({
            "file": name,
            "url": f"{BASE_URL}/article/{name}",
            "lastmod": extract_date(f),
            "title": extract_title(f),
        })

    # 按日期倒序（最新在前）
    articles.sort(key=lambda x: x["lastmod"], reverse=True)

    # 生成 XML
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        f'    <loc>{BASE_URL}/</loc>',
        '    <changefreq>daily</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/article/</loc>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.9</priority>',
        '  </url>',
    ]
    for a in articles:
        lines += [
            '  <url>',
            f'    <loc>{a["url"]}</loc>',
            f'    <lastmod>{a["lastmod"]}</lastmod>',
            '    <changefreq>monthly</changefreq>',
            '    <priority>0.8</priority>',
            '  </url>',
        ]
    lines.append('</urlset>')

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"✓ sitemap.xml 已重新生成，共 {len(articles)} 篇文章：")
    for a in articles:
        print(f"  - {a['lastmod']}  {a['file']}  {a['title'][:30]}")


if __name__ == "__main__":
    main()
