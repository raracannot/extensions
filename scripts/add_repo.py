# -*- coding: utf-8 -*-
"""
一键添加 RARA 扩展远程仓库 (raracannot/extensions)
用法：Blender → 脚本编辑器 → 粘贴此脚本 → 运行。
运行后：偏好设置 → Get Extensions → Repositories 会出现 "RARA 插件库"，
插件列表将自动刷新，可直接浏览/安装全部插件。
"""

import bpy

REPO_NAME = "RARA Extensions"
REPO_MODULE = "rara_extensions"
REPO_URL = "https://raracannot.github.io/extensions/index.json"


def find_repo():
    for repo in bpy.context.preferences.extensions.repos:
        if repo.remote_url == REPO_URL:
            return repo
    return None


def add_repo():
    repo = find_repo()
    if repo is not None:
        print(f"仓库已存在: {repo.name}")
        return repo

    repo = bpy.context.preferences.extensions.repos.new(
        name=REPO_NAME,
        module=REPO_MODULE,
        remote_url=REPO_URL,
        source='USER',
    )
    repo.use_cache = True
    print(f"已添加仓库: {repo.name} ({REPO_URL})")
    return repo


def sync_repo(repo):
    bpy.ops.extensions.repo_sync(repo_directory=repo.directory)
    print("仓库已同步，插件列表已刷新。")


def main():
    repo = add_repo()
    if repo is not None:
        sync_repo(repo)
        # 启用筛选并切换至 RARA 仓库
        wm = bpy.data.window_managers["WinMan"]
        wm.extension_use_filter = True  # 启用筛选
        wm.extension_type = 'ADDON'     # 仅显示插件
        wm.extension_repo_filter = REPO_MODULE  # 仅显示 rara 库
        print(f"已启用筛选并切换至仓库: {REPO_MODULE}")

        bpy.ops.wm.save_userpref()
        print("完成！偏好设置已保存。可打开 偏好设置 → Get Extensions 查看插件。")


if __name__ == "__main__":
    main()
