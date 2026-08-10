# RARA Blender Extensions

RARA 的 Blender 扩展分发仓库。

## 添加远程仓库

在 Blender 中打开 `偏好设置 → Get Extensions → Repositories`，点击 `+` 选择 `Add Remote Repository`，填入：

```
https://raracannot.github.io/extensions/index.json
```

然后即可在线浏览、安装和更新以下扩展：

| 扩展 | 版本 | 说明 |
| --- | --- | --- |
| MoI 3D Bridge | 0.0.1 | 通过 MoI 3D 后台转换并导入 STP 和 3DM 文件 |
| 专业灯光 HUD | 0.0.1 | 优化界面灯光HUD，还你最纯净的打光体验 |
| 导入PDF | 1.0.0 | 导入PDF为曲线 |

## 更新索引

1. 在插件仓库发布新的 Release zip
2. 计算新 zip 的 sha256：`Get-FileHash <zip> -Algorithm SHA256`
3. 更新本仓库 `index.json` 中对应条目的 `version`、`archive_url`、`archive_size`、`archive_hash`
4. 推送，GitHub Pages 自动更新
