# -*- coding: utf-8 -*-
"""
Audio Length Node for ComfyUI
功能：计算输入音频的长度（秒），精确到两位小数。
"""


class AudioLength:
    """
    计算音频长度的 ComfyUI 节点。
    输入：AUDIO 类型（ComfyUI 标准音频格式，包含 waveform 和 sample_rate）
    输出：音频长度（秒），精确到两位小数
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
            },
        }

    RETURN_TYPES = ("FLOAT", "STRING")
    RETURN_NAMES = ("duration_seconds", "duration_text")
    FUNCTION = "calculate_length"
    CATEGORY = "utils/audio"
    OUTPUT_NODE = False

    def calculate_length(self, audio):
        """
        计算音频长度。

        ComfyUI 中 AUDIO 类型是一个字典:
        {
            "waveform": Tensor,  # shape: (batch, channels, samples)
            "sample_rate": int
        }

        长度 = 采样点数 / 采样率
        """
        try:
            waveform = audio["waveform"]
            sample_rate = audio["sample_rate"]

            # waveform shape: (batch, channels, samples)
            num_samples = waveform.shape[-1]

            # 计算时长（秒）
            duration = num_samples / sample_rate

            # 精确到两位小数
            duration = round(duration, 2)

            # 格式化文本输出
            duration_text = f"{duration:.2f}"

            return (duration, duration_text)

        except Exception as e:
            # 如果出现异常，返回 0
            return (0.0, f"Error: {str(e)}")


# ComfyUI 节点注册
NODE_CLASS_MAPPINGS = {
    "AudioLength": AudioLength,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AudioLength": "Audio Length (音频长度计算)",
}
