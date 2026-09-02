# 号卡·中国 站点说明

> 域名：号卡.中国（Punycode：`xn--hlr9m.xn--fiqs8s`）
> 定位：号卡/流量卡「信息科普 + 官方入口导航」静态站（SEO 引流）

## 一、文件结构

```
haoka-site/
├── index.html              # 首页：导航落地页（运营商入口+虚商导航+工具+文章引流）
├── article/
│   ├── index.html          # 文章列表页
│   ├── chunliuliangka.html # 纯流量卡是什么
│   ├── bikeng.html         # 办卡避坑指南
│   ├── xiehaozhuanyun.html # 携号转网全攻略
│   ├── xueshengka.html     # 学生党选卡
│   ├── 19yuan.html         # 19/29元流量卡套路拆解
│   └── fuka.html           # 副卡办理
├── css/style.css           # 统一样式（响应式）
├── js/main.js              # 交互脚本
├── CNAME                   # 域名绑定文件（内容：xn--hlr9m.xn--fiqs8s）
├── sitemap.xml             # 站点地图
├── robots.txt              # 爬虫规则
└── 404.html                # 404 页
```

## 二、部署到 GitHub Pages

1. 在 GitHub 新建一个公开仓库（建议仓库名 `haoka`），把 `haoka-site` 目录内**所有文件**上传到仓库根目录。
2. 进入仓库 **Settings → Pages**：
   - Source 选择 `Deploy from a branch`
   - Branch 选择 `main`，目录选择 `/ (root)`，点 Save。
3. 部署完成后，站点会先以 `https://你的用户名.github.io/haoka/` 形式访问（几分钟内生效）。

## 三、绑定中文域名 号卡.中国

1. **域名解析（二选一）**，到你的域名注册商控制台操作：
   - CNAME 方式：主机记录填 `@`，解析到 `你的用户名.github.io`
   - A 记录方式：解析到 GitHub 的四个 IP（`185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153`）
2. 回到 **Settings → Pages → Custom domain**，填入：
   ```
   xn--hlr9m.xn--fiqs8s
   ```
   （中文域名在 GitHub 中需填 Punycode 形式，`号卡.中国` 对应的就是这个。）点 Save。
3. 勾选 **Enforce HTTPS**，等待证书生成（通常几分钟到几小时）。
4. 如需让 `www.号卡.中国` 也能访问，在域名解析里把 `www` 也 CNAME 到 `你的用户名.github.io`。

> 仓库根目录的 `CNAME` 文件已写好 Punycode 域名，部署时 GitHub 会自动读取。

## 四、日常维护与扩展

- **加文章**：复制 `article/bikeng.html` 作模板，改标题/内容/时间，然后同步更新 `article/index.html`、`index.html` 的文章列表和 `sitemap.xml`。
- **改导航入口**：首页 `index.html` 里的 `.link-item`（虚商导航）可直接增删，搜索框会自动适配。
- **建议持续产出的文章方向**（SEO 长尾词）：老年机选卡、短视频创作者大流量卡、WiFi 共享、5G 手机卡怎么选、移动/联通/电信怎么选等。
- **合规红线**：本站在线**不办卡、不代办、不卖卡**。后续若做办卡变现，必须通过有电信业务经营资质的正规渠道导流，避免在站内做在线开卡/收款。

## 五、本地预览

```bash
cd haoka-site && python3 -m http.server 8090
# 浏览器打开 http://127.0.0.1:8090/index.html
```
