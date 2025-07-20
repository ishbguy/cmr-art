# CMR-ART: Pictures and ASCII arts of the Classic of Mountains and Rivers

《山海经》插画及其通过转换后的ASCII arts文件。

## 如何使用（How to use）

相关[插画](./images)、[ASCII arts](./ascii-arts)文件可按需直接使用，如：代码编写、终端输出、[终端屏保](https://github.com/ishbguy/lock.sh)等。

```bash
git clone https://github.com/ishbguy/cmr-art /path/to/cmr-art
```

## 配套工具（Contributing）

仓库内包含图片转ASCII art的Python程序`image-to-ascii.py`，可按需使用，基于`uv`进行管理，Python相关依赖可查看[pyproject.toml](./pyproject.toml), 大体如下：

1. pillow: 主要的图片处理库
2. click: 命令行处理库

依赖安装及升级优化步骤：

```bash
pip install uv # 或者：pipx install uv
uv sync
```

## 作者（Authors）

Herbert Shen ([ishbguy](https://github.com/ishbguy))

## 许可（License）

本项目在[MIT](./LICENSE)许条款下发布。
