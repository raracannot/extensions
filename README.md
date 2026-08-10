# RARA Blender Extensions

RARA 的 Blender 扩展分发仓库。

## 🚀 小白一键配置（推荐）

1. 打开 Blender（4.2 及以上版本）
2. 打开 **脚本编辑器**（顶部菜单栏切换编辑器类型，或按 `Shift+F11`）
3. 将本仓库 [`scripts/add_repo.py`](scripts/add_repo.py) 的全部代码复制粘贴进去
4. 点击运行按钮（▶）或按 `Alt+P`

脚本会自动完成：添加远程仓库 → 同步插件列表 → 启用筛选并切换到 RARA 插件库 → 保存偏好设置。

之后在 `偏好设置 → Get Extensions` 即可直接安装本仓库的全部插件。

> 也可以直接从 `https://raw.githubusercontent.com/raracannot/extensions/main/scripts/add_repo.py` 复制代码。

## 手动添加远程仓库

在 Blender 中打开 `偏好设置 → Get Extensions → Repositories`，点击 `+` 选择 `Add Remote Repository`，填入：

```
https://raracannot.github.io/extensions/index.json
```

然后即可在线浏览、安装和更新以下扩展：

| 扩展 | 版本 | 说明 |
| --- | --- | --- |
| Better_Experie[更好的体验] | 1.0.1 | 优化原生体验、扩展功能的 Blender 插件合集 |
| MoI 3D Bridge | 0.0.1 | 通过 MoI 3D 后台转换并导入 STP 和 3DM 文件 |
| 专业灯光 HUD | 0.0.1 | 优化界面灯光HUD，还你最纯净的打光体验 |
| 导入PDF | 1.0.0 | 导入PDF为曲线 |

## 更新索引

1. 在插件仓库发布新的 Release zip
2. 计算新 zip 的 sha256：`Get-FileHash <zip> -Algorithm SHA256`
3. 更新本仓库 `index.json` 中对应条目的 `version`、`archive_url`、`archive_size`、`archive_hash`
4. 推送，GitHub Pages 自动更新
