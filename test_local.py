# -*- coding: utf-8 -*-
"""
本地测试脚本（不依赖 ComfyUI，使用模拟的 Tensor 对象）
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class FakeTensor:
    """模拟 torch.Tensor，只实现 shape 属性"""
    def __init__(self, shape):
        self._shape = shape

    @property
    def shape(self):
        return self._shape


def make_audio(sample_rate, num_samples, channels=1, batch=1):
    """构造模拟的 ComfyUI AUDIO 字典"""
    return {
        "waveform": FakeTensor((batch, channels, num_samples)),
        "sample_rate": sample_rate,
    }


def run(desc, audio):
    from audio_length_node import AudioLength
    node = AudioLength()
    duration, text = node.calculate_length(audio)
    print(f"  [{desc}] duration={duration}, text='{text}'")
    return duration, text


if __name__ == "__main__":
    # 测试 1: 5 秒音频, 44100Hz
    d, t = run("5秒 44100Hz", make_audio(44100, 44100 * 5))
    assert d == 5.0 and t == "5.00"

    # 测试 2: 3.5 秒音频, 48000Hz
    d, t = run("3.5秒 48000Hz", make_audio(48000, int(48000 * 3.5)))
    assert d == 3.5 and t == "3.50"

    # 测试 3: 10.25 秒音频, 22050Hz
    d, t = run("10.25秒 22050Hz", make_audio(22050, int(22050 * 10.25)))
    assert d == 10.25 and t == "10.25"

    # 测试 4: 0 长度音频
    d, t = run("0秒", make_audio(44100, 0))
    assert d == 0.0 and t == "0.00"

    # 测试 5: 非常短的音频 (1个采样点)
    d, t = run("1采样点 44100Hz", make_audio(44100, 1))
    assert d == 0.0 and t == "0.00"  # 1/44100 ≈ 0.000023, 四舍五入到 0.00

    # 测试 6: 1秒整
    d, t = run("1秒 48000Hz", make_audio(48000, 48000))
    assert d == 1.0 and t == "1.00"

    # 测试 7: 多通道音频 (立体声)
    d, t = run("立体声 2秒", make_audio(44100, 44100 * 2, channels=2))
    assert d == 2.0 and t == "2.00"

    # 测试 8: 精度测试 - 不整除
    # 100000 samples / 44100 Hz = 2.267573... -> 2.27
    d, t = run("精度测试", make_audio(44100, 100000))
    assert d == 2.27 and t == "2.27"

    print("\n所有测试通过")
