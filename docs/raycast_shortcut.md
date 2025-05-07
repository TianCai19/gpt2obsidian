# Raycast 快捷操作指南

## 创建 Raycast 脚本

1. 打开 Raycast
2. 进入 "Script Commands" 目录
3. 创建新脚本，命名为 "Convert to Obsidian Format"

## 脚本内容

```bash
#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 检查是否提供了文件参数
if [ -z "$1" ]; then
    # 如果没有文件参数，从剪贴板读取
    python3 "$SCRIPT_DIR/gpt2obsidian.py"
else
    # 如果有文件参数，处理该文件
    python3 "$SCRIPT_DIR/gpt2obsidian.py" "$1" "${1%.*}.obsidian.md"
fi
```

## 配置说明

1. 将脚本保存为 `convert-to-obsidian.sh`
2. 确保脚本具有执行权限：
```bash
chmod +x convert-to-obsidian.sh
```

3. 在 Raycast 中配置脚本：
   - 名称：Convert to Obsidian Format
   - 描述：Convert LaTeX math formulas to Obsidian format
   - 脚本路径：选择保存的脚本路径
   - 快捷键：设置您喜欢的快捷键（如 `⌘⇧O`）

## 使用方法

1. 使用快捷键打开 Raycast
2. 输入 "Convert to Obsidian Format"
3. 选择要转换的文件或直接回车（从剪贴板读取）

## 高级配置

### 添加文件拖放支持

1. 在 Raycast 脚本设置中启用 "Accept files as arguments"
2. 现在您可以直接将文件拖放到 Raycast 中

### 添加快捷键

1. 在 Raycast 偏好设置中
2. 找到 "Keyboard Shortcuts"
3. 为脚本添加快捷键（如 `⌘⇧O`）

## 注意事项

- 确保 Python3 已安装
- 确保 `pyperclip` 包已安装：`pip3 install pyperclip`
- 如果遇到权限问题，请检查脚本的执行权限 