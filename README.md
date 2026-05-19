# ComfyUI-AudioLength

一个 ComfyUI 自定义节点，用于**计算音频的时长**（秒），精确到两位小数。

## 功能

- **输入**：`audio`（AUDIO 类型，ComfyUI 标准音频格式）
- **输出**：
  - `duration_seconds`（FLOAT）：音频长度，单位为秒，精确到两位小数
  - `duration_text`（STRING）：音频长度的文本形式，方便显示

## 原理

ComfyUI 中 AUDIO 类型是一个字典，包含：
- `waveform`：音频波形张量，shape 为 `(batch, channels, samples)`
- `sample_rate`：采样率（Hz）

计算公式：`时长 = 采样点数 / 采样率`

## 安装

### 方式一：ComfyUI Manager（推荐）

1. 打开 ComfyUI Manager
2. 点击 **Install via Git URL**
3. 粘贴：`https://github.com/1946242666/ComfyUI-AudioLength.git`
4. 重启 ComfyUI

### 方式二：手动安装

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/1946242666/ComfyUI-AudioLength.git
```

重启 ComfyUI 即可。

## 使用

安装后在节点菜单的 `utils/audio` 分类下找到 **Audio Length (音频长度计算)**。

将任意 AUDIO 类型的输出连接到本节点的 `audio` 输入端，即可获取音频长度。

## 示例

| 输入音频 | 采样率 | 采样点数 | 输出时长 |
|---------|--------|---------|---------|
| 5秒音频 | 44100 Hz | 220500 | 5.00 |
| 3.5秒音频 | 48000 Hz | 168000 | 3.50 |
| 10.25秒音频 | 22050 Hz | 226013 | 10.25 |

## 许可证

MIT License
